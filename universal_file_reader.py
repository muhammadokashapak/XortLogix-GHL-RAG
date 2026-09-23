"""
Universal File Reader & Processor for XortLogix High Level
===========================================================
Supports extraction, OCR fallback, and structured reading of:
1. PDF Documents (.pdf) via pypdf
2. Word Documents (.docx, .doc) via python-docx / XML extraction
3. Excel Spreadsheets (.xlsx, .xls, .csv, .tsv) via openpyxl / pandas / csv
4. PowerPoint Presentations (.pptx) via XML slide parser
5. Text, Code, Markup & Config (.txt, .md, .py, .js, .ts, .json, .yaml, .yml, .xml, .html, .css, .sql, .log, .env, .ini, .sh, .bat, etc.)
6. Archive / Compressed Files (.zip) extracting file tree and textual contents
7. Images (.png, .jpg, .jpeg, .webp, .gif, .bmp, .svg) via PIL & Gemini Vision
8. Audio Recordings (.mp3, .wav, .m4a, .ogg, .webm, .flac, .aac)
9. Video Clips (.mp4, .mov, .webm, .avi, .mkv)
10. Fallback for any other binary / unknown formats via printable string extraction
"""

import os
import io
import re
import csv
import zipfile
import xml.etree.ElementTree as ET
from typing import Dict, Any, Tuple, Optional


def extract_file_content(file_name: str, raw_bytes: bytes, mime_type: str = "") -> Dict[str, Any]:
    """
    Extracts text, structured data, or multimodal representation from ANY file.
    """
    name_lower = file_name.lower().strip()
    m_type = (mime_type or "application/octet-stream").lower().strip()
    
    result = {
        "text": "",
        "mime_type": m_type,
        "file_type": "unknown",
        "is_multimodal": False,
        "details": ""
    }

    # Normalize common audio/video mime types
    if name_lower.endswith(".m4a") or m_type == "audio/x-m4a":
        result["mime_type"] = "audio/mp4"
    elif name_lower.endswith(".mp3") or m_type == "audio/mp3":
        result["mime_type"] = "audio/mpeg"
    elif name_lower.endswith(".wav"):
        result["mime_type"] = "audio/wav"
    elif name_lower.endswith(".webm") and ("audio" in m_type or name_lower.startswith("voice_")):
        result["mime_type"] = "audio/webm"

    # 1. Images
    if m_type.startswith("image/") or name_lower.endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.svg')):
        result["file_type"] = "image"
        result["is_multimodal"] = True
        result["details"] = f"Image file: {file_name} ({len(raw_bytes)} bytes)"
        return result

    # 2. Audio Recordings
    if m_type.startswith("audio/") or name_lower.endswith(('.mp3', '.wav', '.m4a', '.ogg', '.webm', '.flac', '.aac')):
        result["file_type"] = "audio"
        result["is_multimodal"] = True
        result["details"] = f"Audio recording: {file_name} ({len(raw_bytes)} bytes)"
        return result

    # 3. Video Clips
    if m_type.startswith("video/") or name_lower.endswith(('.mp4', '.mov', '.webm', '.avi', '.mkv')):
        result["file_type"] = "video"
        result["is_multimodal"] = True
        result["details"] = f"Video clip: {file_name} ({len(raw_bytes)} bytes)"
        return result

    # 4. PDF Documents
    if name_lower.endswith(".pdf") or m_type == "application/pdf":
        result["file_type"] = "pdf"
        result["mime_type"] = "application/pdf"
        result["is_multimodal"] = True  # Can also be passed to Gemini as PDF bytes
        try:
            import pypdf
            reader = pypdf.PdfReader(io.BytesIO(raw_bytes))
            pages = []
            for idx, page in enumerate(reader.pages):
                txt = page.extract_text()
                if txt and txt.strip():
                    pages.append(f"[Page {idx+1}]:\n{txt.strip()}")
            if pages:
                result["text"] = "\n\n".join(pages)
                result["details"] = f"PDF with {len(reader.pages)} pages extracted"
        except Exception as e_pdf:
            result["details"] = f"PDF extraction note: {e_pdf}"
        return result

    # 5. Microsoft Word Documents (.docx, .doc)
    if name_lower.endswith(('.docx', '.doc')) or "word" in m_type:
        result["file_type"] = "word"
        try:
            import docx
            doc = docx.Document(io.BytesIO(raw_bytes))
            parts = []
            for p in doc.paragraphs:
                if p.text.strip():
                    parts.append(p.text.strip())
            for t in doc.tables:
                for row in t.rows:
                    row_txt = " | ".join(c.text.strip() for c in row.cells if c.text.strip())
                    if row_txt:
                        parts.append(row_txt)
            if parts:
                result["text"] = "\n\n".join(parts)
                result["details"] = f"Word document with {len(parts)} sections/paragraphs extracted"
                return result
        except Exception:
            pass

        # Fallback: XML extraction for DOCX
        try:
            with zipfile.ZipFile(io.BytesIO(raw_bytes)) as z:
                if "word/document.xml" in z.namelist():
                    xml_content = z.read("word/document.xml")
                    root = ET.fromstring(xml_content)
                    texts = [n.text for n in root.iter() if n.tag.endswith('}t') and n.text]
                    if texts:
                        result["text"] = "\n".join(texts)
                        result["details"] = f"Word document (XML parsed): {len(texts)} text nodes"
                        return result
        except Exception:
            pass

    # 6. Microsoft Excel Spreadsheets (.xlsx, .xls) & Tabular (.csv, .tsv)
    if name_lower.endswith(('.xlsx', '.xls')):
        result["file_type"] = "excel"
        try:
            import openpyxl
            wb = openpyxl.load_workbook(io.BytesIO(raw_bytes), data_only=True)
            sheet_blocks = []
            for sname in wb.sheetnames:
                sheet = wb[sname]
                rows_text = [f"### [Sheet: {sname}]"]
                for r in sheet.iter_rows(values_only=True):
                    line = " | ".join(str(val) if val is not None else "" for val in r)
                    if line.strip(" |"):
                        rows_text.append(line)
                if len(rows_text) > 1:
                    sheet_blocks.append("\n".join(rows_text[:500]))
            if sheet_blocks:
                result["text"] = "\n\n".join(sheet_blocks)
                result["details"] = f"Excel workbook with {len(wb.sheetnames)} sheets extracted"
                return result
        except Exception as e_xl:
            result["details"] = f"Excel parsing note: {e_xl}"

    if name_lower.endswith(('.csv', '.tsv')):
        result["file_type"] = "csv"
        try:
            delim = '\t' if name_lower.endswith('.tsv') else ','
            decoded = raw_bytes.decode('utf-8', errors='replace')
            reader = csv.reader(io.StringIO(decoded), delimiter=delim)
            rows = [" | ".join(r) for r in reader if any(r)]
            result["text"] = "\n".join(rows[:1000])
            result["details"] = f"CSV/TSV table with {len(rows)} rows"
            return result
        except Exception:
            pass

    # 7. Microsoft PowerPoint Presentations (.pptx)
    if name_lower.endswith('.pptx') or "presentation" in m_type:
        result["file_type"] = "powerpoint"
        try:
            with zipfile.ZipFile(io.BytesIO(raw_bytes)) as z:
                slide_files = sorted([n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")])
                slides = []
                for s_idx, s_file in enumerate(slide_files, 1):
                    xml_data = z.read(s_file)
                    root = ET.fromstring(xml_data)
                    slide_texts = [n.text for n in root.iter() if n.tag.endswith('}t') and n.text]
                    if slide_texts:
                        slides.append(f"### [Slide {s_idx}]:\n" + " ".join(slide_texts))
                if slides:
                    result["text"] = "\n\n".join(slides)
                    result["details"] = f"PowerPoint presentation with {len(slides)} slides extracted"
                    return result
        except Exception as e_ppt:
            result["details"] = f"PowerPoint parsing note: {e_ppt}"

    # 8. ZIP Archive (.zip)
    if name_lower.endswith('.zip') or m_type in ("application/zip", "application/x-zip-compressed"):
        result["file_type"] = "archive"
        try:
            with zipfile.ZipFile(io.BytesIO(raw_bytes)) as z:
                file_list = z.namelist()
                sections = [f"### [ZIP Archive: {file_name}] - Contains {len(file_list)} files:\n" + "\n".join(f"- {fn}" for fn in file_list[:80])]
                
                # Extract text from supported files inside archive
                extracted_count = 0
                for fn in file_list:
                    if extracted_count >= 12:
                        break
                    fn_lower = fn.lower()
                    if fn_lower.endswith(('.txt', '.md', '.py', '.js', '.json', '.csv', '.html', '.css', '.yaml', '.yml', '.xml', '.sql', '.sh')):
                        try:
                            content_sample = z.read(fn).decode('utf-8', errors='replace')[:3000]
                            sections.append(f"\n--- [Nested File: {fn}] ---\n{content_sample}\n--- [End of {fn}] ---")
                            extracted_count += 1
                        except Exception:
                            pass
                result["text"] = "\n".join(sections)
                result["details"] = f"ZIP archive containing {len(file_list)} files"
                return result
        except Exception as e_zip:
            result["details"] = f"ZIP parsing note: {e_zip}"

    # 9. Plain Text, Code, Markup & Config Files
    text_code_exts = (
        '.txt', '.md', '.py', '.pyw', '.js', '.jsx', '.ts', '.tsx', '.html', '.htm',
        '.css', '.scss', '.sass', '.json', '.jsonl', '.yaml', '.yml', '.xml',
        '.sql', '.log', '.env', '.ini', '.toml', '.sh', '.bash', '.bat', '.ps1',
        '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.php', '.rb', '.go', '.rs',
        '.swift', '.kt', '.dart', '.r', '.m', '.tex', '.rtf', '.dockerfile', '.lock'
    )
    if m_type.startswith("text/") or name_lower.endswith(text_code_exts) or "json" in m_type or "xml" in m_type or "javascript" in m_type:
        result["file_type"] = "code_text"
        for enc in ('utf-8', 'utf-16', 'latin-1', 'cp1252'):
            try:
                decoded = raw_bytes.decode(enc)
                result["text"] = decoded
                result["details"] = f"Text document ({enc}): {len(decoded)} characters"
                return result
            except Exception:
                continue

    # 10. Generic Binary / Unknown File Fallback
    try:
        decoded = raw_bytes.decode('utf-8', errors='ignore')
        if len(decoded) > 20 and sum(1 for c in decoded if c.isprintable()) / len(decoded) > 0.75:
            result["file_type"] = "text_fallback"
            result["text"] = decoded
            result["details"] = f"Generic text decoded: {len(decoded)} characters"
            return result
    except Exception:
        pass

    # Extract clean printable strings from unknown binary
    printable_strings = re.findall(rb'[ -~]{4,}', raw_bytes)
    if printable_strings:
        extracted = [s.decode('ascii', errors='ignore') for s in printable_strings[:500]]
        result["file_type"] = "binary_strings"
        result["text"] = "\n".join(extracted)
        result["details"] = f"Extracted {len(extracted)} printable text strings from binary file"
        return result

    result["details"] = f"Binary file: {file_name} ({len(raw_bytes)} bytes) - no readable text detected"
    return result
