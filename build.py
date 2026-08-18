#!/usr/bin/env python3
"""Assembles final HTML pages from a shared head/header/footer and per-page body content."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Update this once the carerm.co.uk custom domain is connected in Vercel —
# it drives canonical URLs, Open Graph tags and the sitemap.
SITE_URL = "https://care-reach-marketing.vercel.app"

# Page-specific social share image (falls back to the logo if not listed).
OG_IMAGES = {
    "index.html": "https://images.pexels.com/photos/6129145/pexels-photo-6129145.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "about.html": "https://images.pexels.com/photos/7651819/pexels-photo-7651819.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "services.html": "https://images.pexels.com/photos/3862130/pexels-photo-3862130.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "case-studies.html": "https://images.pexels.com/photos/7551591/pexels-photo-7551591.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "industries.html": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "contact.html": "https://images.pexels.com/photos/3861958/pexels-photo-3861958.jpeg?auto=compress&cs=tinysrgb&w=1200",
}

# Sitewide business schema (helps eligibility for knowledge-panel style rich results).
ORG_SCHEMA = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Care Reach Marketing",
  "url": "{SITE_URL}",
  "logo": "{SITE_URL}/assets/images/logo.png",
  "image": "{SITE_URL}/assets/images/logo.png",
  "description": "Digital marketing agency for UK care homes, home care agencies and private clinics.",
  "email": "hello@carerm.co.uk",
  "telephone": "+44-161-000-0000",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Manchester",
    "addressCountry": "GB"
  }},
  "areaServed": "GB",
  "priceRange": "££"
}}
</script>"""

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("case-studies.html", "Case Studies"),
    ("industries.html", "Industries"),
    ("pricing.html", "Pricing"),
    ("resources.html", "Resources"),
    ("faq.html", "FAQ"),
]

def render_nav(active):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ''
        links.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    return "\n        ".join(links)

def head(title, description, filename):
    canonical = SITE_URL if filename == "index.html" else f"{SITE_URL}/{filename}"
    og_image = OG_IMAGES.get(filename, f"{SITE_URL}/assets/images/logo.png")
    full_title = f"{title} | Care Reach Marketing"
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Care Reach Marketing">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{full_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/css/styles.css">
{ORG_SCHEMA}
</head>
<body>
"""

def header(active):
    return f"""<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">
      <img src="assets/images/logo.png" alt="Care Reach Marketing" class="logo-img">
    </a>
    <nav class="main-nav">
      <ul class="nav-links">
        {render_nav(active)}
        <li class="mobile-only-cta"><a href="contact.html" class="btn btn-primary btn-block">Book a Free Audit</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a href="contact.html" class="btn btn-primary">Book a Free Audit</a>
      <button class="nav-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""

FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">Care Reach Marketing</div>
        <p>The digital marketing agency built for UK care providers. We help care homes, home care agencies and clinics get found, get trusted, and get more enquiries.</p>
      </div>
      <div>
        <h4>Company</h4>
        <ul class="footer-links">
          <li><a href="about.html">About Us</a></li>
          <li><a href="case-studies.html">Case Studies</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul class="footer-links">
          <li><a href="services.html">Google Business Profile</a></li>
          <li><a href="services.html">Websites &amp; SEO</a></li>
          <li><a href="services.html">Content &amp; Social</a></li>
          <li><a href="services.html">CRM &amp; Automation</a></li>
          <li><a href="services.html">Paid Advertising</a></li>
        </ul>
      </div>
      <div>
        <h4>Resources</h4>
        <ul class="footer-links">
          <li><a href="resources.html">Blog</a></li>
          <li><a href="industries.html">Industries We Serve</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="contact.html">Get in Touch</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Care Reach Marketing Ltd. All rights reserved.</span>
      <span>Manchester, United Kingdom &middot; hello@carerm.co.uk</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

def build(filename, title, description, active, body):
    html = head(title, description, filename) + header(active) + body + FOOTER
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {filename} ({len(html)} bytes)")

def build_robots_and_sitemap(pages_list, lastmod):
    robots_path = os.path.join(ROOT, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    print(f"Built robots.txt")

    urls = []
    for filename, *_ in pages_list:
        loc = SITE_URL if filename == "index.html" else f"{SITE_URL}/{filename}"
        priority = "1.0" if filename == "index.html" else "0.7"
        urls.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <priority>{priority}</priority>\n  </url>"
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"Built sitemap.xml ({len(pages_list)} URLs)")

if __name__ == "__main__":
    import datetime
    import pages
    for p in pages.PAGES:
        build(*p)
    build_robots_and_sitemap(pages.PAGES, datetime.date.today().isoformat())
