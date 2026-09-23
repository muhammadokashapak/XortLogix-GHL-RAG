"""
Scrape all 35 blog articles from all 9 pages of https://xortlogix.com/blog
========================================================================
Extracts:
- Article Title
- Slug & Canonical URL
- Author & Bio
- Categories / Tags
- Full article markdown / structured content
Saves output as:
- Individual Markdown files in `scraped_xortlogix_blogs/`
- Master JSON catalog in `scraped_xortlogix_blogs/xortlogix_blogs.json`
"""

import os
import sys
import re
import json
import time
import urllib.request
from bs4 import BeautifulSoup

# Ensure UTF-8 output
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "scraped_xortlogix_blogs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
JSON_OUTPUT_FILE = os.path.join(OUTPUT_DIR, "xortlogix_blogs.json")

# Complete list of 35 blog post URLs extracted from all 9 pages of xortlogix.com/blog
ALL_BLOG_URLS = [
    # Page 1
    "https://xortlogix.com/post/ai-workflow-eliminate-meta-ad-duplicates",
    "https://xortlogix.com/post/eliminate-data-risks-b2b-crm-deployments",
    "https://xortlogix.com/post/gohighlevel-training-mentorship-case-study",
    "https://xortlogix.com/post/building-technical-hub-xortlogix",
    # Page 2
    "https://xortlogix.com/post/gohighlevel-charter-booking-crm-case-study",
    "https://xortlogix.com/post/automate-field-operations-gohighlevel-dripjobs",
    "https://xortlogix.com/post/xortlogix-team-culture-mango-party",
    "https://xortlogix.com/post/case-study-eliminating-zapier-failures-via-direct-webhook-architecture-seamlessai-gohighlevel",
    # Page 3
    "https://xortlogix.com/post/case-study-engineering-a-custom-secure-client-portal-inside-gohighlevel-where-others-failed",
    "https://xortlogix.com/post/boost-speed-to-lead-with-vas-automation",
    "https://xortlogix.com/post/beyond-kpis-building-a-culture-of-excellence-healthy-ambition-and-unshakeable-faith",
    "https://xortlogix.com/post/new-blog-post-4406",
    # Page 4
    "https://xortlogix.com/post/new-blog-post-9236",
    "https://xortlogix.com/post/outcome-based-architecture-vs-technical-competence",
    "https://xortlogix.com/post/onsite-infrastructure-vs-freelancer-chaos",
    "https://xortlogix.com/post/gohighlevel-manual-reviews-update",
    # Page 5
    "https://xortlogix.com/post/client-portal-in-gohighlevel",
    "https://xortlogix.com/post/gohighlevel-mastery-course",
    "https://xortlogix.com/post/new-blog-post-sales-dashboard-track-agents-targets",
    "https://xortlogix.com/post/new-blog-post-gohighlevel-quiz-update",
    # Page 6
    "https://xortlogix.com/post/new-blog-smart-tags-in-gohighlevel",
    "https://xortlogix.com/post/new-blog-post-gohighlevel-custom-objects",
    "https://xortlogix.com/post/new-blog-post-gohighlevel-certified-admin-v2",
    "https://xortlogix.com/post/new-blog-post-gohighlevel-real-estate-dashboard",
    # Page 7
    "https://xortlogix.com/post/new-blog-post-investment-portal-inside-ghl",
    "https://xortlogix.com/post/new-blog-post-gohighlevels-new-centralized-schedules",
    "https://xortlogix.com/post/new-blog-post-gohighlevels-new-built-in-image-editor",
    "https://xortlogix.com/post/new-blog-post-Centralized-Multi-Day-Course-Booking-in-GoHighLevel",
    # Page 8
    "https://xortlogix.com/post/new-blog-post-Referral-Dashboard-for-Agencies",
    "https://xortlogix.com/post/new-blog-post-Custom-Sales-Dashboard",
    "https://xortlogix.com/post/new-blog-post-What-is-GoHighLevel",
    "https://xortlogix.com/post/Organize-Workflows-in-GoHighLevel",
    # Page 9
    "https://xortlogix.com/post/new-blog-post-gohighlevel-gbp-optimization",
    "https://xortlogix.com/post/new-blog-post-2489",
    "https://xortlogix.com/post/new-blog-post-3809",
]

def fetch_html(url: str, retries: int = 3) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read().decode("utf-8", errors="ignore")
        except Exception as e:
            if attempt == retries - 1:
                print(f"❌ Failed to fetch {url} after {retries} attempts: {e}")
                return ""
            time.sleep(1.5 * (attempt + 1))
    return ""


def clean_node_to_markdown(elem) -> str:
    """Recursively converts HTML elements inside blog body into clean Markdown."""
    if elem is None:
        return ""
    
    parts = []
    for child in elem.children:
        if child.name is None:
            text = str(child).strip()
            if text:
                parts.append(text)
        elif child.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            level = int(child.name[1])
            header_text = child.get_text().strip()
            if header_text:
                parts.append(f"\n\n{'#' * level} {header_text}\n\n")
        elif child.name == "p":
            p_text = child.get_text().strip()
            if p_text:
                parts.append(f"\n\n{p_text}\n\n")
        elif child.name in ["ul", "ol"]:
            list_items = []
            for li_idx, li in enumerate(child.find_all("li", recursive=False)):
                prefix = f"{li_idx + 1}." if child.name == "ol" else "-"
                list_items.append(f"{prefix} {li.get_text().strip()}")
            if list_items:
                parts.append("\n\n" + "\n".join(list_items) + "\n\n")
        elif child.name == "blockquote":
            b_text = child.get_text().strip()
            if b_text:
                parts.append(f"\n\n> {b_text}\n\n")
        elif child.name == "pre" or child.name == "code":
            c_text = child.get_text().strip()
            if c_text:
                parts.append(f"\n\n```\n{c_text}\n```\n\n")
        else:
            sub = clean_node_to_markdown(child)
            if sub:
                parts.append(sub)

    res = " ".join(parts)
    # Normalize multiple linebreaks and spaces
    res = re.sub(r'\n{3,}', '\n\n', res)
    res = re.sub(r'[ \t]+', ' ', res)
    return res.strip()


def parse_blog_article(url: str, html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    slug = url.rstrip("/").split("/")[-1]

    # 1. Title
    h1 = soup.find("h1")
    title = ""
    if h1:
        title = h1.get_text().strip()
    if not title:
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text().replace("| XortLogix", "").replace("- XortLogix", "").strip()
    if not title:
        title = slug.replace("-", " ").replace("new blog post", "").strip().title()

    # 2. Author & Bio
    author_name = "XortLogix Team"
    author_bio = ""
    author_container = soup.find(class_=re.compile(r'blog-author-details|blog-author-container'))
    if author_container:
        author_text = author_container.get_text(separator="\n").strip()
        lines = [l.strip() for l in author_text.split("\n") if l.strip()]
        if lines:
            author_name = lines[0]
            if len(lines) > 1:
                author_bio = " ".join(lines[1:])
    else:
        # Check meta tags
        meta_author = soup.find("meta", attrs={"name": "author"})
        if meta_author and meta_author.get("content"):
            author_name = meta_author.get("content").strip()

    # 3. Publish Date
    date_str = ""
    date_elem = soup.find(class_=re.compile(r'publish-date|blog-date|post-date'))
    if date_elem:
        date_str = date_elem.get_text().strip()
    if not date_str:
        meta_date = soup.find("meta", property="article:published_time")
        if meta_date and meta_date.get("content"):
            date_str = meta_date.get("content").strip()

    # 4. Tags / Categories
    tags = []
    tag_elems = soup.find_all(class_=re.compile(r'blog.*tag|category-tag'))
    for te in tag_elems:
        t_text = te.get_text().strip()
        if t_text and t_text not in tags:
            tags.append(t_text)

    # 5. Main Body
    body_elem = soup.find(class_=re.compile(r'blog-html|c-blog-content|blog-content'))
    if not body_elem:
        # Fallback to article or main
        body_elem = soup.find("article") or soup.find("main")

    markdown_body = clean_node_to_markdown(body_elem) if body_elem else ""

    # Check if tags were embedded at the top of the body
    if markdown_body and not tags:
        first_line = markdown_body.split("\n")[0].strip()
        if "," in first_line and len(first_line) < 120:
            potential_tags = [x.strip() for x in first_line.split(",") if x.strip()]
            if len(potential_tags) >= 2:
                tags = potential_tags

    # Build structured article markdown
    full_markdown = f"""# {title}

**Source URL:** {url}  
**Author:** {author_name}  
{f'**Published Date:** {date_str}  ' if date_str else ''}{f'**Categories/Tags:** {", ".join(tags)}  ' if tags else ''}

---

{markdown_body}

---
### About Author:
**{author_name}**  
{author_bio}
"""

    return {
        "title": title,
        "slug": slug,
        "url": url,
        "author": author_name,
        "author_bio": author_bio,
        "date": date_str,
        "tags": tags,
        "category": tags[0] if tags else "XortLogix Case Studies",
        "markdown": full_markdown.strip(),
        "plain_text": markdown_body.strip(),
        "char_count": len(markdown_body)
    }


def scrape_all_blogs():
    print("=" * 70)
    print("🚀 SCRAPING ALL 35 BLOG ARTICLES FROM XORTLOGIX.COM/BLOG (9 PAGES)")
    print("=" * 70)

    articles = []
    success_count = 0

    for idx, url in enumerate(ALL_BLOG_URLS, 1):
        print(f"[{idx}/{len(ALL_BLOG_URLS)}] Fetching: {url} ...", flush=True)
        html = fetch_html(url)
        if not html:
            print(f"⚠️ Skipped: {url}")
            continue

        data = parse_blog_article(url, html)
        articles.append(data)
        success_count += 1

        # Save individual markdown file
        safe_slug = re.sub(r'[^a-zA-Z0-9_-]', '_', data["slug"])
        file_path = os.path.join(OUTPUT_DIR, f"{safe_slug}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(data["markdown"])

        print(f"   ✅ Saved: '{data['title'][:55]}' ({data['char_count']} chars, Author: {data['author']})", flush=True)
        time.sleep(0.3)  # Polite crawl rate

    # Save Master JSON catalog
    with open(JSON_OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 70)
    print(f"🎉 SCRAPING COMPLETE! Successfully scraped {success_count}/{len(ALL_BLOG_URLS)} blog articles.")
    print(f"📁 Markdown files saved to: {OUTPUT_DIR}")
    print(f"📄 Master JSON index saved to: {JSON_OUTPUT_FILE}")
    print("=" * 70)


if __name__ == "__main__":
    scrape_all_blogs()
