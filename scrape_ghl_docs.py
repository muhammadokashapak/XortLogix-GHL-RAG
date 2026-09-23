"""
GoHighLevel (GHL) Master Documentation & API Scraper (Sitemap-Powered)
=======================================================================
This script automatically discovers ALL official HighLevel documentation pages
from the official sitemap (3,800+ pages), filters for the latest active API v2 & OAuth docs,
and uses multi-threaded concurrent workers to scrape, clean, and convert everything into Markdown.
"""

import os
import re
import sys
import time
import json
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Set, Dict, List, Any, Optional
import requests
from bs4 import BeautifulSoup

# Base Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "scraped_ghl_docs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MASTER_MD_FILE = os.path.join(OUTPUT_DIR, "ghl_master_scraped_documentation.md")
MASTER_JSON_FILE = os.path.join(OUTPUT_DIR, "ghl_api_scraped_data.json")
SITEMAP_URL = "https://marketplace.gohighlevel.com/docs/sitemap.xml"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# High-Value Keyword Filters (to prioritize relevant REST API v2 & OAuth pages)
CORE_TOPIC_KEYWORDS = [
    "oauth", "authorization", "token", "scope",
    "contact", "opportunity", "pipeline", "workflow", "trigger",
    "location", "sub-account", "conversation", "message", "sms", "email",
    "calendar", "appointment", "webhook", "custom-field", "custom-value",
    "payment", "invoice", "form", "survey", "marketplace", "snapshot",
    "user", "integration", "developer", "api"
]


def fetch_all_sitemap_urls() -> List[str]:
    """Fetches the official sitemap.xml and extracts all URLs."""
    print(f"📡 Fetching official HighLevel Documentation Sitemap: {SITEMAP_URL} ...")
    try:
        resp = requests.get(SITEMAP_URL, headers=HEADERS, timeout=20)
        if resp.status_code == 200:
            urls = re.findall(r'<loc>(.*?)</loc>', resp.text)
            print(f"✅ Discovered {len(urls)} total documentation pages in sitemap!")
            return urls
    except Exception as e:
        print(f"❌ Error fetching sitemap: {e}")
    return []


def filter_relevant_urls(all_urls: List[str], max_limit: int = 400) -> List[str]:
    """Filters out blog tags, duplicate old version archives, and prioritizes core API topics."""
    prioritized: List[str] = []
    seen: Set[str] = set()

    for url in all_urls:
        clean = urllib.parse.urldefrag(url)[0].rstrip('/')
        if clean in seen or not clean.startswith("https://marketplace.gohighlevel.com/docs"):
            continue

        # Skip generic blog tags or pagination noise
        if any(skip in clean.lower() for skip in ["/blog/tags", "/page/", "/markdown-page"]):
            continue

        # Check if URL matches any core GHL developer topics
        url_lower = clean.lower()
        if any(kw in url_lower for kw in CORE_TOPIC_KEYWORDS) or "/ghl/" in url_lower:
            prioritized.append(clean)
            seen.add(clean)

        if len(prioritized) >= max_limit:
            break

    print(f"🎯 Filtered down to {len(prioritized)} high-priority developer documentation pages.")
    return prioritized


def clean_filename(title: str) -> str:
    """Sanitizes titles for saving files."""
    clean = re.sub(r'[^\w\-_.]', '_', title).strip('_')
    return clean[:70] or "ghl_doc"


def scrape_page(url: str, session: requests.Session) -> Optional[Dict[str, Any]]:
    """Scrapes a single documentation page and converts HTML into clean Markdown."""
    try:
        resp = session.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return None

        soup = BeautifulSoup(resp.text, "html.parser")

        # Strip navigation, footer, scripts, styles
        for tag in soup(["script", "style", "nav", "footer", "header", "noscript", "svg", "button"]):
            tag.extract()

        title_tag = soup.find("h1") or soup.find("title")
        raw_title = title_tag.get_text().strip() if title_tag else "GHL Documentation"
        title = re.sub(r'\s*\|\s*HighLevel.*$', '', raw_title)

        # Locate Docusaurus main content article/container
        main_content = (
            soup.find("article")
            or soup.find("main")
            or soup.find("div", class_=re.compile(r"markdown|docItemContainer|theme-doc-markdown", re.I))
            or soup.find("body")
        )

        if not main_content:
            return None

        md_lines = [
            f"# {title}",
            f"**Source URL:** `{url}`",
            "---\n"
        ]

        endpoints = []

        for el in main_content.find_all(["h1", "h2", "h3", "h4", "p", "pre", "code", "table", "ul", "ol"]):
            tag_name = el.name.lower()
            text = el.get_text().strip()

            if not text:
                continue

            if tag_name == "h1":
                md_lines.append(f"\n# {text}\n")
            elif tag_name == "h2":
                md_lines.append(f"\n## {text}\n")
            elif tag_name == "h3":
                md_lines.append(f"\n### {text}\n")
            elif tag_name == "h4":
                md_lines.append(f"\n#### {text}\n")
            elif tag_name == "p":
                api_match = re.search(r'\b(GET|POST|PUT|DELETE|PATCH)\s+([/\w\-{}:]+)', text)
                if api_match:
                    endpoints.append(f"{api_match.group(1)} {api_match.group(2)}")
                md_lines.append(f"\n{text}\n")
            elif tag_name in ["pre", "code"]:
                code_text = el.get_text()
                if len(code_text.splitlines()) > 1 or "{" in code_text or "http" in code_text:
                    lang = "json" if "{" in code_text else "bash"
                    md_lines.append(f"\n```{lang}\n{code_text.strip()}\n```\n")
            elif tag_name in ["ul", "ol"]:
                for li in el.find_all("li"):
                    li_text = li.get_text().strip()
                    if li_text:
                        md_lines.append(f"* {li_text}")
                md_lines.append("")

        markdown_text = "\n".join(md_lines)
        markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)

        if len(markdown_text.strip()) < 120:
            return None

        return {
            "title": title,
            "url": url,
            "markdown": markdown_text,
            "endpoints": list(set(endpoints))
        }

    except Exception as e:
        return None


def run_full_site_scraper(max_pages: int = 250, max_workers: int = 10):
    """Orchestrates sitemap discovery, parallel multi-threaded scraping, and consolidation."""
    all_sitemap_urls = fetch_all_sitemap_urls()
    if not all_sitemap_urls:
        print("⚠️ Could not read sitemap. Falling back to default seed URLs.")
        target_urls = [
            "https://marketplace.gohighlevel.com/docs/",
            "https://marketplace.gohighlevel.com/docs/oauth/GettingStarted",
            "https://marketplace.gohighlevel.com/docs/Authorization/authorization_doc",
            "https://marketplace.gohighlevel.com/docs/ghl/contacts/contacts",
            "https://marketplace.gohighlevel.com/docs/ghl/opportunities/opportunities",
            "https://marketplace.gohighlevel.com/docs/ghl/workflows/workflows",
            "https://marketplace.gohighlevel.com/docs/ghl/locations/locations",
            "https://marketplace.gohighlevel.com/docs/ghl/conversations/conversations",
            "https://marketplace.gohighlevel.com/docs/ghl/calendars/calendars",
        ]
    else:
        target_urls = filter_relevant_urls(all_sitemap_urls, max_limit=max_pages)

    print(f"\n⚡ Starting Multi-Threaded Scraping with {max_workers} worker threads...")
    start_time = time.time()
    
    results: List[Dict[str, Any]] = []
    session = requests.Session()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(scrape_page, url, session): url for url in target_urls}
        completed = 0
        total = len(target_urls)

        for future in as_completed(future_to_url):
            url = future_to_url[future]
            completed += 1
            try:
                data = future.result()
                if data:
                    results.append(data)
                    # Save individual document file
                    fname = f"{clean_filename(data['title'])}_{completed}.md"
                    fpath = os.path.join(OUTPUT_DIR, fname)
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(data["markdown"])
                    print(f"[{completed}/{total}] ✅ Saved: {data['title'][:45]}")
                else:
                    print(f"[{completed}/{total}] ⏩ Skipped (empty or error): {url}")
            except Exception as e:
                print(f"[{completed}/{total}] ❌ Failed {url}: {e}")

    # Compile Consolidated Master File
    print(f"\n📦 Compiling Master Documentation File ({len(results)} pages captured)...")
    with open(MASTER_MD_FILE, "w", encoding="utf-8") as f_master:
        f_master.write("# GoHighLevel Master Complete API & Developer Documentation\n\n")
        f_master.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f_master.write(f"Total Pages Scraped: {len(results)}\n\n")
        f_master.write("=" * 80 + "\n\n")

        for item in results:
            f_master.write(item["markdown"])
            f_master.write("\n\n" + "=" * 80 + "\n\n")

    # Save Indexed JSON for Vector DB Ingestion
    with open(MASTER_JSON_FILE, "w", encoding="utf-8") as f_json:
        json.dump(results, f_json, indent=2)

    elapsed = round(time.time() - start_time, 2)
    print("\n" + "=" * 70)
    print("🎉 FULL DOCUMENTATION SCRAPING SUCCESSFULLY COMPLETED!")
    print(f"⏱️ Time Taken: {elapsed} seconds")
    print(f"📑 Total Docs Saved: {len(results)} pages")
    print(f"📁 Output Directory: {OUTPUT_DIR}")
    print(f"📄 Master Markdown File: {MASTER_MD_FILE}")
    print(f"📊 Indexed JSON File: {MASTER_JSON_FILE}")
    print("=" * 70)


if __name__ == "__main__":
    # Scrapes up to 250 core API/OAuth pages in parallel
    run_full_site_scraper(max_pages=250, max_workers=12)
