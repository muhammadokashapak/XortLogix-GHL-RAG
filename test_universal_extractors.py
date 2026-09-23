import io
import openpyxl
import zipfile
from universal_file_reader import extract_file_content

def test_all():
    # 1. XLSX
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Feasibility"
    ws.append(["Feature", "Native GHL", "Custom Needed"])
    ws.append(["Blog Proofreading", "Yes (AI Assistant)", "No"])
    ws.append(["Headless Next.js Portal", "No", "Yes (OAuth + Custom API)"])
    xlsx_io = io.BytesIO()
    wb.save(xlsx_io)
    res_xl = extract_file_content("ghl_matrix.xlsx", xlsx_io.getvalue())
    assert res_xl["file_type"] == "excel"
    assert "Feasibility" in res_xl["text"]
    assert "Blog Proofreading" in res_xl["text"]
    print("PASS: Excel (.xlsx) extraction")

    # 2. ZIP
    zip_io = io.BytesIO()
    with zipfile.ZipFile(zip_io, "w") as z:
        z.writestr("readme.md", "# GHL Webhook Guide\nSend payload via POST to webhook endpoint.")
        z.writestr("config.json", '{"app": "GHL RAG"}')
    res_zip = extract_file_content("ghl_package.zip", zip_io.getvalue())
    assert res_zip["file_type"] == "archive"
    assert "readme.md" in res_zip["text"]
    assert "GHL Webhook Guide" in res_zip["text"]
    print("PASS: ZIP archive extraction")

    # 3. Code & Config
    code_bytes = b'def ghl_webhook_handler(req):\n    return {"status": 200}'
    res_code = extract_file_content("handler.py", code_bytes)
    assert res_code["file_type"] == "code_text"
    assert "ghl_webhook_handler" in res_code["text"]
    print("PASS: Code/Script (.py) extraction")

    # 4. CSV
    csv_bytes = b"lead_id,first_name,ghl_tag\n101,John,hot-lead\n102,Sara,appointment-booked"
    res_csv = extract_file_content("contacts.csv", csv_bytes)
    assert res_csv["file_type"] == "csv"
    assert "appointment-booked" in res_csv["text"]
    print("PASS: CSV tabular extraction")

    # 5. Media check (multimodal flags)
    res_img = extract_file_content("screenshot.png", b"\x89PNG\r\n\x1a\nfakecontent")
    assert res_img["is_multimodal"] == True
    assert res_img["file_type"] == "image"
    print("PASS: Image recognition & multimodal flag")

    res_aud = extract_file_content("call_recording.mp3", b"ID3fakeaudio")
    assert res_aud["is_multimodal"] == True
    assert res_aud["file_type"] == "audio"
    print("PASS: Audio recognition & multimodal flag")

    print("\nAll 5 universal file extraction tests passed successfully!")

if __name__ == "__main__":
    test_all()
