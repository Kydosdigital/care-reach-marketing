# Care Reach Marketing — Website

An 11-page static site for Care Reach Marketing (carerm.co.uk), a digital marketing
agency for the UK care sector. Deployed on Vercel.

## Structure

- `index.html`, `about.html`, `services.html`, `case-studies.html`, `pricing.html`,
  `industries.html`, `resources.html`, `faq.html`, `privacy.html`, `contact.html`,
  `404.html` — the built site pages
- `assets/css/styles.css` — shared stylesheet (colours, type, layout all live here)
- `assets/js/main.js` — mobile nav, FAQ accordion, contact form submission
- `assets/images/` — free-to-use stock photos (Pexels, no attribution required),
  served as WebP from our own domain
- `pages.py` — the actual copy/content for every page, as Python strings
- `build.py` — assembles the final HTML, plus `robots.txt`, `sitemap.xml` and
  `site.webmanifest`
- `vercel.json` — clean URLs, cache headers, security headers

## To edit content

Edit the relevant variable in `pages.py` (e.g. `HOME`, `PRICING`, `FAQ`), then run:

```
python3 build.py
```

This regenerates all HTML files from the templates. Don't edit the `.html` files
directly — they're build output and your changes will be overwritten.

## Before this goes live — required

Four switches at the top of `build.py` control launch readiness. All four need
attention:

### 1. `FORM_ENDPOINT` — the contact form is not connected

**This is the most important one.** The form currently has nowhere to send
enquiries. It says so honestly on the page and refuses to pretend a message was
sent, but that means every enquiry is a lost lead until you wire it up.

Set up a handler (Formspree, GoHighLevel, Vercel serverless function — anything
accepting a `POST` of form fields and returning 2xx), then:

```python
FORM_ENDPOINT = "https://formspree.io/f/xxxxxxx"
```

Rebuild, redeploy, and send yourself a test enquiry. Once set, the form posts for
real, shows a sending state, and only shows the "thanks" confirmation after the
handler actually accepts the message. Failures tell the person to email instead
rather than silently swallowing their enquiry.

### 2. `SITE_LIVE` — the site is deliberately hidden from Google

While `SITE_LIVE = False`, every page carries `noindex, nofollow` and
`robots.txt` disallows crawling. This is intentional: if Google indexes the
temporary `care-reach-marketing.vercel.app` address, it will compete with
carerm.co.uk for your own brand terms later.

Once the real domain is connected, set `SITE_URL = "https://carerm.co.uk"` and
`SITE_LIVE = True`, then rebuild. Only then submit the sitemap to Search Console.

### 3. `BUSINESS_PHONE` — currently empty on purpose

The old placeholder (`0161 000 0000`) has been removed from the page and from the
`ProfessionalService` structured data. A fake number in structured data is worse
than none, because search engines treat it as your official contact detail. Add
your real number here and it reappears sitewide.

### 4. `IS_LIMITED_COMPANY` — the footer no longer says "Ltd"

Set to `True` only once "Care Reach Marketing Ltd" is actually registered at
Companies House. Until then the footer reads "Care Reach Marketing".

## Also worth checking

- **Privacy policy** (`privacy.html`): a solid template, but it still has bracketed
  placeholders for your registered address, ICO registration number and data
  retention period. Get it reviewed before launch — it's a starting point, not
  legal advice.
- **Pricing** (`pricing.html`): the three tiers (Visibility £449, Growth £895,
  Partner £1,495) are draft figures based on market research, not confirmed
  pricing. Adjust to whatever you actually want to charge.
- **Case studies** (`case-studies.html`): clearly-labelled illustrative examples,
  not real client results. Swap them for real results as soon as you have them.
- **Resources** (`resources.html`): every article still reads "Coming soon", so the
  page has been taken out of the main navigation. It's still linked from the footer
  and in the sitemap. Put it back in `NAV_ITEMS` in `build.py` once you've published
  a real article.
- **Domain**: confirm and purchase carerm.co.uk through a registrar before
  announcing the brand publicly.

## Deployment

The Vercel project should be connected to this Git repository so that pushing to
`main` deploys automatically. Without that link, deploys happen by manual upload
and production drifts away from the code in this repo — which is exactly what had
happened before this branch (production was serving hotlinked Pexels images while
the repo had local ones).

`vercel.json` sets `cleanUrls`, so pages are served without the `.html` extension
(`/about`, not `/about.html`). All internal links use those clean paths.

## Images

Content images are WebP, resized to a maximum width of 1200px and served from our
own domain. Every `<img>` carries explicit `width`/`height` so the browser reserves
space and the layout doesn't jump while loading; everything below the fold is
lazy-loaded.

If you add new photos, resize and convert them, and add their dimensions to
`IMAGE_SIZES` in `build.py`. WebP is supported by all current browsers; there is
no JPEG fallback. The one exception is `assets/images/social-card.jpg`, kept as
JPEG at 1200×630 because some social platforms still prefer it for link previews.

## Fonts

Uses Google Fonts (Manrope for headings, Inter for body) loaded via CDN link in
each page's `<head>`. Requires internet access to render as designed; falls back
to system sans-serif otherwise. Note that this sends visitors' IP addresses to
Google — the privacy policy discloses it.
