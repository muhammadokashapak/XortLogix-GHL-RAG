import os
import sys
import time
from playwright.sync_api import sync_playwright
import pypdf

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, "documentation.html")
PDF_PATH = os.path.join(BASE_DIR, "XortLogix_High_Level_Documentation.pdf")

print("Compiling publication-grade PDF from documentation.html...")
start_time = time.time()

if not os.path.exists(HTML_PATH):
    print(f"❌ Error: {HTML_PATH} does not exist!")
    sys.exit(1)

with sync_playwright() as p:
    browser = p.chromium.launch(args=["--disable-gpu", "--no-sandbox"])
    page = browser.new_page()
    
    file_url = f"file:///{HTML_PATH.replace(os.sep, '/')}"
    page.goto(file_url, wait_until="networkidle")
    
    page.pdf(
        path=PDF_PATH,
        format="A4",
        print_background=True,
        margin={"top": "12mm", "bottom": "14mm", "left": "12mm", "right": "12mm"},
        display_header_footer=True,
        header_template='<div style="font-size: 7pt; color: #94a3b8; width: 100%; text-align: right; padding-right: 14mm; font-family: sans-serif;">XortLogix High Level Enterprise AI Platform • Technical Manual</div>',
        footer_template='<div style="font-size: 7pt; color: #94a3b8; width: 100%; display: flex; justify-content: space-between; padding-left: 14mm; padding-right: 14mm; font-family: sans-serif;"><span>Confidential • XortLogix Solutions Architecture</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
    )
    browser.close()

elapsed = round(time.time() - start_time, 2)
print(f"🎉 PDF successfully compiled in {elapsed}s: {PDF_PATH}")

if os.path.exists(PDF_PATH):
    file_size_kb = round(os.path.getsize(PDF_PATH) / 1024, 2)
    reader = pypdf.PdfReader(PDF_PATH)
    num_pages = len(reader.pages)
    print("=" * 60)
    print("✅ PDF VERIFICATION REPORT:")
    print(f"   - Destination: {PDF_PATH}")
    print(f"   - Page Count:  {num_pages} Pages")
    print(f"   - File Size:   {file_size_kb} KB")
    print("=" * 60)
else:
    print("❌ Error: Output PDF file not found!")
    sys.exit(1)
