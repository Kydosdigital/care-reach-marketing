#!/usr/bin/env python3
"""Assembles final HTML pages from a shared head/header/footer and per-page body content."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Launch switches — the two values you change when the real domain is ready.
# ---------------------------------------------------------------------------

# Drives canonical URLs, Open Graph tags and the sitemap.
# Change to "https://carerm.co.uk" once that domain is connected in Vercel.
SITE_URL = "https://care-reach-marketing.vercel.app"

# While False, every page carries <meta name="robots" content="noindex, nofollow">
# and robots.txt disallows crawling. This stops Google indexing the temporary
# *.vercel.app address and competing with carerm.co.uk later.
# Flip to True only once the real domain is live and you want to be found.
SITE_LIVE = False

# Where the contact form posts. Empty means "not wired up yet", and the form
# then tells people to email instead of pretending their message was sent.
# Paste a Formspree endpoint (https://formspree.io/f/xxxxxxx) or any handler
# that accepts a POST of form fields and returns 2xx.
FORM_ENDPOINT = ""

# Real, published phone number. Left empty deliberately: a placeholder number
# in structured data is worse than no number at all, because search engines
# treat it as your official contact detail. Fill in to restore it sitewide.
BUSINESS_PHONE = ""

CONTACT_EMAIL = "hello@carerm.co.uk"

# Only true once "Care Reach Marketing Ltd" is registered at Companies House.
# Until then the footer says "Care Reach Marketing" with no suffix.
IS_LIMITED_COMPANY = False

COMPANY_NAME = "Care Reach Marketing Ltd" if IS_LIMITED_COMPANY else "Care Reach Marketing"

# Default social share image, served from our own domain rather than hotlinked.
SOCIAL_IMAGE = f"{SITE_URL}/assets/images/social-card.jpg"

# Intrinsic size of every content image, so the browser can reserve space and
# avoid layout shift. Regenerate if you swap the artwork.
IMAGE_SIZES = {
    "analytics-graph.webp": (1200, 800),
    "handshake-partnership.webp": (1200, 800),
    "handshake.webp": (1200, 801),
    "healthcare-professionals.webp": (1200, 800),
    "hero-caregiver.webp": (1200, 800),
    "laptop-data.webp": (1200, 799),
    "marketing-desk.webp": (1200, 900),
    "medical-reception.webp": (1200, 1800),
    "nurses-smiling.webp": (1200, 800),
    "person-laptop.webp": (1200, 1800),
    "phone-social.webp": (1200, 800),
    "reception-interior.webp": (1200, 1600),
    "team-discussion.webp": (1200, 900),
    "team-meeting.webp": (1200, 900),
    "wheelchair-companion.webp": (1200, 1800),
    "wheelchair-woman.webp": (1200, 1800),
}

# Sitewide business schema (helps eligibility for knowledge-panel style rich results).
_phone_line = f'\n  "telephone": "{BUSINESS_PHONE}",' if BUSINESS_PHONE else ""
ORG_SCHEMA = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Care Reach Marketing",
  "url": "{SITE_URL}",
  "logo": "{SITE_URL}/assets/images/logo.png",
  "image": "{SOCIAL_IMAGE}",
  "description": "Digital marketing agency for UK care homes, home care agencies and private clinics.",
  "email": "{CONTACT_EMAIL}",{_phone_line}
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Manchester",
    "addressCountry": "GB"
  }},
  "areaServed": "GB",
  "priceRange": "££"
}}
</script>"""

# Resources is deliberately out of the primary nav while every article still
# reads "Coming soon" — it stays reachable from the footer and the sitemap.
NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("case-studies.html", "Case Studies"),
    ("industries.html", "Industries"),
    ("pricing.html", "Pricing"),
    ("faq.html", "FAQ"),
]


def url_path(filename):
    """Clean, extensionless URL for a built page (vercel.json sets cleanUrls)."""
    return "/" if filename == "index.html" else "/" + filename[:-len(".html")]


def render_nav(active):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ''
        aria = ' aria-current="page"' if href == active else ''
        links.append(f'<li><a href="{url_path(href)}"{cls}{aria}>{label}</a></li>')
    return "\n        ".join(links)


def head(title, description, filename, indexable=True):
    canonical = SITE_URL if filename == "index.html" else f"{SITE_URL}{url_path(filename)}"
    full_title = f"{title} | Care Reach Marketing"
    robots = ""
    if not SITE_LIVE or not indexable:
        robots = '\n<meta name="robots" content="noindex, nofollow">'
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Care Reach Marketing">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SOCIAL_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{full_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SOCIAL_IMAGE}">
<meta name="theme-color" content="#0F4C46">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/css/styles.css">
<script>window.CRM_CONFIG={{formEndpoint:"{FORM_ENDPOINT}",contactEmail:"{CONTACT_EMAIL}"}};</script>
{ORG_SCHEMA}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
"""


def header(active):
    return f"""<header class="site-header">
  <div class="container header-inner">
    <a href="/" class="logo">
      <img src="/assets/images/logo.png" alt="Care Reach Marketing" class="logo-img" width="180" height="40">
    </a>
    <nav class="main-nav" aria-label="Primary">
      <ul class="nav-links" id="primary-nav">
        {render_nav(active)}
        <li class="mobile-only-cta"><a href="/contact" class="btn btn-primary btn-block">Book a Free Audit</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a href="/contact" class="btn btn-primary">Book a Free Audit</a>
      <button class="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false" aria-controls="primary-nav"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="main">
"""


FOOTER = f"""</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">Care Reach Marketing</div>
        <p>The digital marketing agency built for UK care providers. We help care homes, home care agencies and clinics get found, get trusted, and get more enquiries.</p>
      </div>
      <div>
        <h4>Company</h4>
        <ul class="footer-links">
          <li><a href="/about">About Us</a></li>
          <li><a href="/case-studies">Case Studies</a></li>
          <li><a href="/pricing">Pricing</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul class="footer-links">
          <li><a href="/services">Google Business Profile</a></li>
          <li><a href="/services">Websites &amp; SEO</a></li>
          <li><a href="/services">Content &amp; Social</a></li>
          <li><a href="/services">CRM &amp; Automation</a></li>
          <li><a href="/services">Paid Advertising</a></li>
        </ul>
      </div>
      <div>
        <h4>Resources</h4>
        <ul class="footer-links">
          <li><a href="/resources">Guides</a></li>
          <li><a href="/industries">Industries We Serve</a></li>
          <li><a href="/faq">FAQ</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 {COMPANY_NAME}. All rights reserved.</span>
      <span>Manchester, United Kingdom &middot; <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></span>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js"></script>
</body>
</html>
"""


def build(filename, title, description, active, body, indexable=True):
    html = head(title, description, filename, indexable) + header(active) + body + FOOTER
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {filename} ({len(html)} bytes)")


def build_manifest():
    manifest = """{
  "name": "Care Reach Marketing",
  "short_name": "Care Reach",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FAF6F0",
  "theme_color": "#0F4C46",
  "icons": [
    { "src": "/assets/images/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }
  ]
}
"""
    with open(os.path.join(ROOT, "site.webmanifest"), "w", encoding="utf-8") as f:
        f.write(manifest)
    print("Built site.webmanifest")


def build_robots_and_sitemap(pages_list, lastmod):
    robots_path = os.path.join(ROOT, "robots.txt")
    if SITE_LIVE:
        robots = f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    else:
        robots = (
            "# Pre-launch: this temporary vercel.app address must not be indexed,\n"
            "# or it will compete with the real domain later. Set SITE_LIVE = True\n"
            "# in build.py and rebuild once carerm.co.uk is connected.\n"
            "User-agent: *\nDisallow: /\n"
        )
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots)
    print(f"Built robots.txt ({'indexable' if SITE_LIVE else 'noindex — pre-launch'})")

    urls = []
    for filename, *_ in pages_list:
        loc = SITE_URL if filename == "index.html" else f"{SITE_URL}{url_path(filename)}"
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
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"Built sitemap.xml ({len(pages_list)} URLs)")


if __name__ == "__main__":
    import datetime
    import pages

    for p in pages.PAGES:
        build(*p)
    # Kept out of the sitemap and out of the index.
    build("404.html", "Page Not Found", "Sorry, that page doesn't exist. Find care marketing services, pricing and contact details for Care Reach Marketing.", None, pages.NOT_FOUND, indexable=False)
    build_manifest()
    build_robots_and_sitemap(pages.PAGES, datetime.date.today().isoformat())
