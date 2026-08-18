# Care Reach Marketing — Website

A 9-page static site for Care Reach Marketing (carerm.co.uk), a digital marketing
agency for the UK care sector.

## Structure

- `index.html`, `about.html`, `services.html`, `case-studies.html`, `pricing.html`,
  `industries.html`, `resources.html`, `faq.html`, `contact.html` — the site pages
- `assets/css/styles.css` — shared stylesheet (colours, type, layout all live here)
- `assets/js/main.js` — mobile nav toggle, FAQ accordion, contact form demo handler
- `assets/images/` — free-to-use stock photos (Pexels, no attribution required)
- `pages.py` — the actual copy/content for every page, as Python strings
- `build.py` — assembles the final HTML from `pages.py` + shared header/footer

## To edit content

Edit the relevant variable in `pages.py` (e.g. `HOME`, `PRICING`, `FAQ`), then run:

```
python3 build.py
```

This regenerates all HTML files from the templates. You don't need to touch the
HTML files directly, though you can if you prefer — they're just static output.

## Before this goes live, please check

- **Pricing** (`pricing.html`): the three tiers (Visibility £449, Growth £895,
  Partner £1,495) are draft figures based on market research, not confirmed
  pricing. Adjust to whatever you actually want to charge.
- **Case studies** (`case-studies.html`): these are clearly-labelled illustrative
  examples, not real client results, since the agency is newly launched. Swap
  these out for real results as soon as you have them.
- **Contact details**: the phone number in `contact.html` is a placeholder
  (0161 000 0000). Update with your real number.
- **Contact form**: the form currently just shows a "thanks" message in the
  browser (no backend). Wire it up to an email service, GoHighLevel, or
  Formspree-style handler before relying on it for real enquiries.
- **"Ltd" in the footer**: the footer currently says "Care Reach Marketing Ltd".
  Only keep this once the company is actually registered at Companies House
  under that name — otherwise drop the "Ltd".
- **Domain**: carerm.co.uk appeared unregistered when checked, but confirm and
  purchase it directly through a registrar before announcing the brand publicly.

## Fonts

Uses Google Fonts (Fraunces for headings, Inter for body) loaded via CDN link
in each page's `<head>`. Requires internet access to render correctly; falls
back to system serif/sans-serif otherwise.
