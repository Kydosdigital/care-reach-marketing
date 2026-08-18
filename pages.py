# -*- coding: utf-8 -*-
# Body content for each page. Tuple: (filename, title, description, active_nav, body_html)

HOME = """
<section class="hero container">
  <div class="hero-copy">
    <span class="eyebrow">Digital Marketing for UK Care Providers</span>
    <h1>More families finding the right care, sooner.</h1>
    <p class="lede">Care Reach Marketing is a full-service digital marketing agency built specifically for UK care homes, home care agencies and private clinics. We handle your Google presence, website, content and enquiry follow-up, so your team can focus on care.</p>
    <div class="hero-actions">
      <a href="/contact" class="btn btn-primary">Book a Free Audit</a>
      <a href="/services" class="btn btn-outline" style="color:#1F2421;">See Our Services</a>
    </div>
    <div class="hero-stats">
      <div class="hero-stat"><strong>Care-Only</strong><span>Sector specialism, not a side project</span></div>
      <div class="hero-stat"><strong>5</strong><span>Core services under one roof</span></div>
      <div class="hero-stat"><strong>UK-Based</strong><span>Team who understand CQC context</span></div>
    </div>
  </div>
  <div class="hero-media">
    <img src="/assets/images/hero-caregiver.webp" alt="A carer supporting an elderly resident in a UK care setting" width="1200" height="800" loading="eager" fetchpriority="high">
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="text-center" style="max-width:700px;margin:0 auto;">
      <span class="eyebrow">What We Do</span>
      <h2>Everything your care business needs to be found and chosen</h2>
      <p class="lede center">Most care providers don't need more marketing jargon. They need more enquiries, fewer empty beds, and a website that doesn't embarrass them. That's what we build.</p>
    </div>
    <div class="grid grid-3" style="margin-top:2.5rem;">
      <div class="card service-card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg></div>
        <h3>Google Business Profile</h3>
        <p>Get found first when families search "care home near me". We optimise, monitor and manage your listing and reviews.</p>
        <a href="/services">Learn more &rarr;</a>
      </div>
      <div class="card service-card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
        <h3>Websites &amp; SEO</h3>
        <p>Fast, mobile-first websites built to convert visitors into enquiries, with local SEO that keeps you visible.</p>
        <a href="/services">Learn more &rarr;</a>
      </div>
      <div class="card service-card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg></div>
        <h3>Content &amp; Social Media</h3>
        <p>Warm, trustworthy content for families and prospective staff alike, written with your sector in mind.</p>
        <a href="/services">Learn more &rarr;</a>
      </div>
      <div class="card service-card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg></div>
        <h3>CRM &amp; Enquiry Automation</h3>
        <p>Never lose an enquiry to a missed call again. Automated follow-up that respects families' time and urgency.</p>
        <a href="/services">Learn more &rarr;</a>
      </div>
      <div class="card service-card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></div>
        <h3>Paid Advertising</h3>
        <p>Targeted Google and Meta campaigns built around occupancy goals, not vanity clicks.</p>
        <a href="/services">Learn more &rarr;</a>
      </div>
      <div class="card service-card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg></div>
        <h3>Reporting &amp; Strategy</h3>
        <p>Plain-English monthly reporting and a named contact who actually understands your sector.</p>
        <a href="/pricing">See pricing &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center" style="max-width:700px;margin:0 auto;">
      <span class="eyebrow">Why Care Providers Choose Us</span>
      <h2>We only work with one sector, so we know it properly</h2>
    </div>
    <div class="grid grid-2" style="margin-top:2.5rem;align-items:center;">
      <img src="/assets/images/team-discussion.webp" alt="Marketing team reviewing a care client's campaign performance" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="900" loading="lazy" decoding="async">
      <div>
        <div style="margin-bottom:1.5rem;">
          <h4>We speak your language</h4>
          <p>CQC ratings, occupancy targets, safeguarding-aware content and staff recruitment pressure are part of our daily vocabulary, not an afterthought.</p>
        </div>
        <div style="margin-bottom:1.5rem;">
          <h4>Transparent, no jargon</h4>
          <p>You'll always know what we're doing, why, and what it's likely to achieve. Monthly reports written in plain English, not agency-speak.</p>
        </div>
        <div>
          <h4>Flexible commitment</h4>
          <p>No lengthy lock-ins by default. We'd rather earn a renewal every quarter than trap you in a contract.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="text-center" style="max-width:700px;margin:0 auto;">
      <span class="eyebrow">How It Works</span>
      <h2>A straightforward process, start to finish</h2>
    </div>
    <div class="steps" style="margin-top:2.5rem;">
      <div class="step"><h4>Free Audit</h4><p>We review your Google presence, website and current enquiry process and flag the quickest wins.</p></div>
      <div class="step"><h4>Strategy</h4><p>You get a plain-English plan built around your occupancy or enquiry goals, not generic marketing theory.</p></div>
      <div class="step"><h4>Launch</h4><p>We build and launch the agreed services, from your Google profile to your website and campaigns.</p></div>
      <div class="step"><h4>Grow</h4><p>Ongoing content, optimisation and monthly reporting, with a named contact who knows your account.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band">
      <h2>Ready to turn more enquiries into move-ins?</h2>
      <p class="lede center" style="color:rgba(255,255,255,0.85);">Book a free, no-obligation audit of your current Google presence and website. We'll tell you exactly what's costing you enquiries.</p>
      <div class="hero-actions" style="justify-content:center;">
        <a href="/contact" class="btn btn-primary">Book Your Free Audit</a>
        <a href="/case-studies" class="btn btn-outline">See Example Results</a>
      </div>
    </div>
  </div>
</section>
"""

ABOUT = """
<section class="page-hero container">
  <span class="eyebrow">About Care Reach Marketing</span>
  <h1>Built by marketers who understand care.</h1>
  <p class="lede center">We started Care Reach Marketing because too many good care providers were losing enquiries to worse ones with better websites. That felt like a fixable problem.</p>
</section>

<section class="section-sm section-alt">
  <div class="container grid grid-2" style="align-items:center;">
    <div>
      <span class="eyebrow">Our Story</span>
      <h2>Care marketing, done properly</h2>
      <p>Most marketing agencies treat the care sector like any other local business: a plumber, a dentist, a care home, all run through the same generic playbook. We think that's a mistake. Care decisions are emotional, urgent and high-stakes, and the marketing around them has to reflect that.</p>
      <p>Care Reach Marketing exists to bring proper digital marketing discipline, the kind used by well-resourced consumer brands, to an industry that's often stretched too thin to focus on it. We handle the Google listings, the websites, the content and the follow-up systems, so care teams can stay focused on the people in front of them.</p>
    </div>
    <img src="/assets/images/team-meeting.webp" alt="Care Reach Marketing team planning a client campaign" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="900" loading="lazy" decoding="async">
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center" style="max-width:700px;margin:0 auto;">
      <span class="eyebrow">What Drives Us</span>
      <h2>The principles behind every account we run</h2>
    </div>
    <div class="grid grid-4" style="margin-top:2.5rem;">
      <div class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg></div>
        <h4>Sector specialism</h4>
        <p>We only work with care providers. That focus means less time explaining the basics and more time on what actually moves the needle.</p>
      </div>
      <div class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/></svg></div>
        <h4>Compliance-aware</h4>
        <p>We write and design with safeguarding, dignity and CQC context in mind, not just conversion rate.</p>
      </div>
      <div class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></div>
        <h4>Results-focused</h4>
        <p>Every service ties back to enquiries, occupancy or staff applications. Vanity metrics don't pay the bills.</p>
      </div>
      <div class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
        <h4>Straight-talking</h4>
        <p>No jargon, no inflated reports. If something isn't working, we'll tell you and change course.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container text-center">
    <span class="eyebrow" style="background:rgba(255,255,255,0.15);color:#fff;">How We Work</span>
    <h2>A small, senior team, not a call centre</h2>
    <p class="lede center" style="color:rgba(255,255,255,0.85);">You'll work directly with the people running your account, not a rotating cast of junior account managers. Every client gets a named contact who understands their business.</p>
    <div class="hero-actions" style="justify-content:center;">
      <a href="/contact" class="btn btn-primary">Talk To Us</a>
    </div>
  </div>
</section>
"""

SERVICES = """
<section class="page-hero container">
  <span class="eyebrow">What We Do</span>
  <h1>Five services. One goal: more of the right enquiries.</h1>
  <p class="lede center">Every service below exists to move one number: qualified enquiries into your care business. We build them individually or as a full-service package.</p>
</section>

<section class="section-alt section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <img src="/assets/images/phone-social.webp" alt="Google Business Profile shown on a mobile phone" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="800" loading="lazy" decoding="async">
    <div>
      <span class="eyebrow">01</span>
      <h2>Google Business Profile Optimisation</h2>
      <p>Most families start their search on Google Maps, not your website. We make sure your profile is complete, accurate and working hard: photos, categories, services, opening information and a steady stream of genuine reviews.</p>
      <ul class="price-features">
        <li>Full profile audit and optimisation</li>
        <li>Genuine review generation system</li>
        <li>Photo and update scheduling</li>
        <li>Ongoing monitoring and response management</li>
      </ul>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <div>
      <span class="eyebrow">02</span>
      <h2>Websites &amp; Local SEO</h2>
      <p>Your website is often the deciding factor once a family has found you. We design fast, mobile-first sites that build trust quickly and make enquiring easy, backed by local SEO so you show up for the searches that matter.</p>
      <ul class="price-features">
        <li>Conversion-focused design and copy</li>
        <li>Mobile-first, fast-loading build</li>
        <li>Local SEO and service-area pages</li>
        <li>Ongoing technical maintenance</li>
      </ul>
    </div>
    <img src="/assets/images/laptop-data.webp" alt="Website analytics displayed on a laptop screen" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="799" loading="lazy" decoding="async">
  </div>
</section>

<section class="section-alt section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <img src="/assets/images/marketing-desk.webp" alt="Content creation for a care provider's social media" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="900" loading="lazy" decoding="async">
    <div>
      <span class="eyebrow">03</span>
      <h2>Content &amp; Social Media</h2>
      <p>Warm, honest content that reassures families and attracts the staff you need. We plan and produce a steady content calendar so your channels never go quiet, without you having to think about it.</p>
      <ul class="price-features">
        <li>Monthly content calendar</li>
        <li>Photography and video coordination</li>
        <li>Family-facing and recruitment-facing content</li>
        <li>Consistent posting across key channels</li>
      </ul>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <div>
      <span class="eyebrow">04</span>
      <h2>CRM &amp; Enquiry Automation</h2>
      <p>A missed call or a slow reply can cost you a placement. We set up simple, reliable systems that capture every enquiry, follow up automatically, and make sure nothing falls through the cracks.</p>
      <ul class="price-features">
        <li>Enquiry capture from web, phone and forms</li>
        <li>Automated follow-up sequences</li>
        <li>Clear enquiry pipeline for your team</li>
        <li>Monthly enquiry reporting</li>
      </ul>
    </div>
    <img src="/assets/images/analytics-graph.webp" alt="Enquiry pipeline data shown as a graph" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="800" loading="lazy" decoding="async">
  </div>
</section>

<section class="section-alt section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <img src="/assets/images/handshake.webp" alt="Care provider and marketing partner agreeing on an advertising strategy" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="801" loading="lazy" decoding="async">
    <div>
      <span class="eyebrow">05</span>
      <h2>Paid Advertising</h2>
      <p>Targeted Google and Meta campaigns built around your actual goals, whether that's filling beds, growing a home care patch, or recruiting carers. Every pound is tied back to a measurable outcome.</p>
      <ul class="price-features">
        <li>Google Search and Local Services Ads</li>
        <li>Meta campaigns for family and recruitment audiences</li>
        <li>Transparent monthly spend reporting</li>
        <li>Ongoing optimisation, not "set and forget"</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="container cta-band">
    <h2>Not sure which services you need?</h2>
    <p class="lede center" style="color:rgba(255,255,255,0.85);">Book a free audit and we'll tell you honestly where the quickest wins are.</p>
    <div class="hero-actions" style="justify-content:center;">
      <a href="/contact" class="btn btn-primary">Book a Free Audit</a>
      <a href="/pricing" class="btn btn-outline">See Pricing</a>
    </div>
  </div>
</section>
"""

CASE_STUDIES = """
<section class="page-hero container">
  <span class="eyebrow">Example Engagements</span>
  <h1>What a Care Reach Marketing engagement looks like</h1>
  <p class="lede center">As a newly launched agency, we're building our public case study library from live client work. The scenarios below are illustrative examples of how we approach common challenges in the care sector, based on our experience in digital marketing. Ask us for current client references directly.</p>
</section>

<section class="section-alt">
  <div class="container grid grid-3">
    <div class="card media-card">
      <img src="/assets/images/nurses-smiling.webp" alt="Staff at a residential care home" width="1200" height="800" loading="lazy" decoding="async">
      <div class="card-body">
        <h3>Residential care home, North West England</h3>
        <p><strong>Challenge:</strong> An incomplete Google Business Profile and a website that took over 8 seconds to load on mobile, resulting in enquiries going to better-ranked competitors.</p>
        <p><strong>Approach:</strong> Full profile rebuild, review generation system, and a new mobile-first website with a simple enquiry form above the fold.</p>
        <p><strong>What good looks like:</strong> Stronger local map-pack visibility and a shorter path from search to enquiry.</p>
      </div>
    </div>
    <div class="card media-card">
      <img src="/assets/images/wheelchair-companion.webp" alt="A home care worker supporting a client" width="1200" height="1800" loading="lazy" decoding="async">
      <div class="card-body">
        <h3>Home care agency, multi-borough coverage</h3>
        <p><strong>Challenge:</strong> Enquiries coming through several channels (phone, web form, Facebook) with no consistent follow-up, leading to leads going cold.</p>
        <p><strong>Approach:</strong> Centralised CRM with automated follow-up sequences and a single enquiry dashboard for the office manager.</p>
        <p><strong>What good looks like:</strong> Fewer missed follow-ups and a clear, auditable enquiry trail for CQC purposes.</p>
      </div>
    </div>
    <div class="card media-card">
      <img src="/assets/images/medical-reception.webp" alt="Reception area of a private clinic" width="1200" height="1800" loading="lazy" decoding="async">
      <div class="card-body">
        <h3>Private clinic, single site</h3>
        <p><strong>Challenge:</strong> Strong local reputation but almost no online visibility beyond word of mouth, limiting growth.</p>
        <p><strong>Approach:</strong> Local SEO foundation, content calendar built around common patient questions, and a modest paid search campaign.</p>
        <p><strong>What good looks like:</strong> A second, digital channel of enquiries alongside existing referrals.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container cta-band">
    <h2>Want to see what this could look like for your business?</h2>
    <p class="lede center" style="color:rgba(255,255,255,0.85);">Book a free audit and we'll show you the specific gaps in your current setup.</p>
    <div class="hero-actions" style="justify-content:center;">
      <a href="/contact" class="btn btn-primary">Book a Free Audit</a>
    </div>
  </div>
</section>
"""

PRICING = """
<section class="page-hero container">
  <span class="eyebrow">Pricing</span>
  <h1>Straightforward pricing, built for care budgets</h1>
  <p class="lede center">Three tiers, no hidden setup fees, and a shorter minimum term than most agencies offer. All prices are guide prices for a single site; multi-site groups get a custom quote.</p>
</section>

<section class="section-alt">
  <div class="container">
    <div class="pricing-grid">
      <div class="pricing-card">
        <h3>Visibility</h3>
        <p>For care providers who need the fundamentals fixed first.</p>
        <div class="price">&pound;449<span>/month</span></div>
        <ul class="price-features">
          <li>Google Business Profile optimisation</li>
          <li>Review generation system</li>
          <li>Local SEO health check &amp; fixes</li>
          <li>Monthly reporting call</li>
          <li>1-month minimum term</li>
        </ul>
        <a href="/contact" class="btn btn-dark btn-block">Get Started</a>
      </div>
      <div class="pricing-card featured">
        <span class="pricing-badge">Most Popular</span>
        <h3>Growth</h3>
        <p>Full-service marketing for care providers ready to scale enquiries.</p>
        <div class="price">&pound;895<span>/month</span></div>
        <ul class="price-features">
          <li>Everything in Visibility</li>
          <li>Website build or ongoing optimisation</li>
          <li>Monthly content &amp; social calendar</li>
          <li>CRM &amp; automated enquiry follow-up</li>
          <li>3-month minimum term</li>
        </ul>
        <a href="/contact" class="btn btn-primary btn-block">Get Started</a>
      </div>
      <div class="pricing-card">
        <h3>Partner</h3>
        <p>For multi-site groups or providers ready to invest in paid growth.</p>
        <div class="price">&pound;1,495<span>/month</span></div>
        <ul class="price-features">
          <li>Everything in Growth</li>
          <li>Paid Google &amp; Meta campaign management</li>
          <li>Dedicated account manager</li>
          <li>Quarterly strategy review</li>
          <li>3-month minimum term</li>
        </ul>
        <a href="/contact" class="btn btn-dark btn-block">Get Started</a>
      </div>
    </div>
    <p class="text-center" style="margin-top:2rem;color:var(--color-text-muted);font-size:0.9rem;">Media spend for paid advertising campaigns is separate from the monthly fee. All plans begin with a short onboarding period so we can agree goals and baseline metrics together.</p>
  </div>
</section>

<section class="section">
  <div class="container cta-band">
    <h2>Not sure which tier fits your business?</h2>
    <p class="lede center" style="color:rgba(255,255,255,0.85);">Tell us about your care business and we'll recommend a starting point, no pressure.</p>
    <div class="hero-actions" style="justify-content:center;">
      <a href="/contact" class="btn btn-primary">Talk To Us</a>
    </div>
  </div>
</section>
"""

INDUSTRIES = """
<section class="page-hero container">
  <span class="eyebrow">Industries We Serve</span>
  <h1>Built for the way UK care businesses actually operate</h1>
  <p class="lede center">Every corner of the care sector has different pressures. Here's how we adapt our approach to each.</p>
</section>

<section class="section-alt section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <img src="/assets/images/healthcare-professionals.webp" alt="Staff team at a residential care home" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="800" loading="lazy" decoding="async">
    <div>
      <h2>Residential &amp; Nursing Care Homes</h2>
      <p>Occupancy is everything. We focus on local search visibility, a website that reassures anxious families quickly, and a review pipeline that reflects the quality of care you already provide.</p>
      <ul class="price-features">
        <li>Local map-pack and "near me" visibility</li>
        <li>Family-facing content and virtual tours</li>
        <li>Fast-response enquiry handling</li>
      </ul>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <div>
      <h2>Home Care &amp; Domiciliary Agencies</h2>
      <p>Coverage area and trust are the deciding factors for home care. We build service-area pages, manage reviews across your patch, and set up CRM systems that keep referrals and enquiries organised as you grow.</p>
      <ul class="price-features">
        <li>Service-area and postcode-level SEO</li>
        <li>Referral and enquiry tracking</li>
        <li>Staff recruitment content and campaigns</li>
      </ul>
    </div>
    <img src="/assets/images/wheelchair-woman.webp" alt="A home care client receiving support" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="1800" loading="lazy" decoding="async">
  </div>
</section>

<section class="section-alt section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <img src="/assets/images/reception-interior.webp" alt="Modern private clinic reception area" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="1600" loading="lazy" decoding="async">
    <div>
      <h2>Private Clinics &amp; Practices</h2>
      <p>Referrals and reputation carry private clinics a long way, but digital visibility fills the gaps word of mouth can't reach. We build a steady, low-maintenance digital presence that complements your existing referral network.</p>
      <ul class="price-features">
        <li>Local SEO and Google Business Profile</li>
        <li>Patient-focused content and FAQs</li>
        <li>Light-touch paid search campaigns</li>
      </ul>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="container grid grid-2" style="align-items:center;">
    <div>
      <h2>Multi-Site Care Groups</h2>
      <p>Consistency across sites matters as much as performance at any single one. We build a central brand and reporting structure while still optimising each location's local presence individually.</p>
      <ul class="price-features">
        <li>Per-site Google Business Profile management</li>
        <li>Group-wide reporting dashboard</li>
        <li>Dedicated account manager</li>
      </ul>
    </div>
    <img src="/assets/images/handshake-partnership.webp" alt="Care group leadership agreeing on a marketing partnership" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="800" loading="lazy" decoding="async">
  </div>
</section>

<section class="section section-alt">
  <div class="container cta-band">
    <h2>Don't see your exact setup?</h2>
    <p class="lede center" style="color:rgba(255,255,255,0.85);">If you provide care in the UK, we've almost certainly got a relevant approach. Get in touch and tell us about your business.</p>
    <div class="hero-actions" style="justify-content:center;">
      <a href="/contact" class="btn btn-primary">Get in Touch</a>
    </div>
  </div>
</section>
"""

RESOURCES = """
<section class="page-hero container">
  <span class="eyebrow">Resources</span>
  <h1>Practical marketing guidance for UK care providers</h1>
  <p class="lede center">Straightforward, no-nonsense articles on getting found, getting trusted, and getting more of the right enquiries. New articles publishing soon.</p>
</section>

<section class="section-alt">
  <div class="container grid grid-2">
    <div class="card">
      <span class="tag">Coming soon</span>
      <div class="blog-meta">Local SEO</div>
      <h3>How to improve your care home's Google Business Profile</h3>
      <p>The specific fields, photos and review habits that make the biggest difference to local search visibility for care homes.</p>
    </div>
    <div class="card">
      <span class="tag">Coming soon</span>
      <div class="blog-meta">Enquiry Management</div>
      <h3>Five ways to turn more care enquiries into move-ins</h3>
      <p>Where most care providers lose enquiries between first contact and admission, and simple fixes for each stage.</p>
    </div>
    <div class="card">
      <span class="tag">Coming soon</span>
      <div class="blog-meta">CQC &amp; Marketing</div>
      <h3>CQC ratings and your marketing: what families actually search for</h3>
      <p>How to present your CQC rating honestly and effectively, whatever it currently says.</p>
    </div>
    <div class="card">
      <span class="tag">Coming soon</span>
      <div class="blog-meta">Recruitment</div>
      <h3>A quick-start guide to staff recruitment marketing for care providers</h3>
      <p>Using the same digital channels you use for families to reach the carers you're struggling to hire.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container cta-band">
    <h2>Want these delivered straight to your inbox?</h2>
    <p class="lede center" style="color:rgba(255,255,255,0.85);">Get in touch and we'll let you know as soon as new articles go live.</p>
    <div class="hero-actions" style="justify-content:center;">
      <a href="/contact" class="btn btn-primary">Get in Touch</a>
    </div>
  </div>
</section>
"""

FAQ = """
<section class="page-hero container">
  <span class="eyebrow">Frequently Asked Questions</span>
  <h1>Straight answers to the questions we get most</h1>
</section>

<section class="section-alt">
  <div class="container" style="max-width:800px;">
    <div class="faq-item open">
      <button class="faq-question" type="button" id="faq-q1" aria-expanded="true" aria-controls="faq-a1">Do you actually understand the care sector, or is this just a rebrand?</button>
      <div class="faq-answer" id="faq-a1" role="region" aria-labelledby="faq-q1"><p>We work exclusively with care homes, home care agencies and clinics. That means our team spends its time understanding occupancy pressure, safeguarding-aware content and CQC context, rather than splitting attention across unrelated industries.</p></div>
    </div>
    <div class="faq-item">
      <button class="faq-question" type="button" id="faq-q2" aria-expanded="false" aria-controls="faq-a2">What's the minimum contract length?</button>
      <div class="faq-answer" id="faq-a2" role="region" aria-labelledby="faq-q2"><p>Our Visibility tier has a 1-month minimum term. Growth and Partner tiers have a 3-month minimum, mainly because meaningful SEO and content results need a little runway. There's no lengthy annual lock-in by default.</p></div>
    </div>
    <div class="faq-item">
      <button class="faq-question" type="button" id="faq-q3" aria-expanded="false" aria-controls="faq-a3">How quickly will we see results?</button>
      <div class="faq-answer" id="faq-a3" role="region" aria-labelledby="faq-q3"><p>Google Business Profile improvements can show impact within a few weeks. Website and SEO work typically takes 2 to 3 months to build meaningful momentum. We'll give you honest, sector-specific timelines during your free audit rather than generic promises.</p></div>
    </div>
    <div class="faq-item">
      <button class="faq-question" type="button" id="faq-q4" aria-expanded="false" aria-controls="faq-a4">Do you work with multi-site care groups?</button>
      <div class="faq-answer" id="faq-a4" role="region" aria-labelledby="faq-q4"><p>Yes. We build a consistent group-wide structure while still optimising each individual location's local visibility. Multi-site engagements get a custom quote and a dedicated account manager.</p></div>
    </div>
    <div class="faq-item">
      <button class="faq-question" type="button" id="faq-q5" aria-expanded="false" aria-controls="faq-a5">Will you write content that's safeguarding and dignity aware?</button>
      <div class="faq-answer" id="faq-a5" role="region" aria-labelledby="faq-q5"><p>Yes, this is core to how we work. All family-facing and resident-facing content is written with dignity, consent and safeguarding front of mind, not just conversion rate.</p></div>
    </div>
    <div class="faq-item">
      <button class="faq-question" type="button" id="faq-q6" aria-expanded="false" aria-controls="faq-a6">What happens if we want to leave?</button>
      <div class="faq-answer" id="faq-a6" role="region" aria-labelledby="faq-q6"><p>Once your minimum term is up, you can cancel with 30 days' notice. We'll hand over any assets we've built, such as your website files and content calendar, in a usable format.</p></div>
    </div>
    <div class="faq-item">
      <button class="faq-question" type="button" id="faq-q7" aria-expanded="false" aria-controls="faq-a7">Do you handle staff recruitment marketing as well as family-facing marketing?</button>
      <div class="faq-answer" id="faq-a7" role="region" aria-labelledby="faq-q7"><p>Yes. Many of our clients use the same channels and content systems to support carer recruitment alongside family enquiries. We can scope this in as part of your plan.</p></div>
    </div>
    <div class="faq-item">
      <button class="faq-question" type="button" id="faq-q8" aria-expanded="false" aria-controls="faq-a8">How is reporting handled?</button>
      <div class="faq-answer" id="faq-a8" role="region" aria-labelledby="faq-q8"><p>You'll get a plain-English monthly report covering enquiries, visibility and campaign performance, plus a call with your named account contact to talk through what it means.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container cta-band">
    <h2>Still have a question?</h2>
    <div class="hero-actions" style="justify-content:center;">
      <a href="/contact" class="btn btn-primary">Ask Us Directly</a>
    </div>
  </div>
</section>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do you actually understand the care sector, or is this just a rebrand?",
      "acceptedAnswer": { "@type": "Answer", "text": "We work exclusively with care homes, home care agencies and clinics. That means our team spends its time understanding occupancy pressure, safeguarding-aware content and CQC context, rather than splitting attention across unrelated industries." }
    },
    {
      "@type": "Question",
      "name": "What's the minimum contract length?",
      "acceptedAnswer": { "@type": "Answer", "text": "Our Visibility tier has a 1-month minimum term. Growth and Partner tiers have a 3-month minimum, mainly because meaningful SEO and content results need a little runway. There's no lengthy annual lock-in by default." }
    },
    {
      "@type": "Question",
      "name": "How quickly will we see results?",
      "acceptedAnswer": { "@type": "Answer", "text": "Google Business Profile improvements can show impact within a few weeks. Website and SEO work typically takes 2 to 3 months to build meaningful momentum. We'll give you honest, sector-specific timelines during your free audit rather than generic promises." }
    },
    {
      "@type": "Question",
      "name": "Do you work with multi-site care groups?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. We build a consistent group-wide structure while still optimising each individual location's local visibility. Multi-site engagements get a custom quote and a dedicated account manager." }
    },
    {
      "@type": "Question",
      "name": "Will you write content that's safeguarding and dignity aware?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, this is core to how we work. All family-facing and resident-facing content is written with dignity, consent and safeguarding front of mind, not just conversion rate." }
    },
    {
      "@type": "Question",
      "name": "What happens if we want to leave?",
      "acceptedAnswer": { "@type": "Answer", "text": "Once your minimum term is up, you can cancel with 30 days' notice. We'll hand over any assets we've built, such as your website files and content calendar, in a usable format." }
    },
    {
      "@type": "Question",
      "name": "Do you handle staff recruitment marketing as well as family-facing marketing?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Many of our clients use the same channels and content systems to support carer recruitment alongside family enquiries. We can scope this in as part of your plan." }
    },
    {
      "@type": "Question",
      "name": "How is reporting handled?",
      "acceptedAnswer": { "@type": "Answer", "text": "You'll get a plain-English monthly report covering enquiries, visibility and campaign performance, plus a call with your named account contact to talk through what it means." }
    }
  ]
}
</script>
"""

CONTACT = """
<section class="page-hero container">
  <span class="eyebrow">Get in Touch</span>
  <h1>Let's talk about your care business</h1>
  <p class="lede center">Book a free audit or just ask a question. We reply to every enquiry personally, usually within one working day.</p>
</section>

<section class="section-alt">
  <div class="container grid grid-2" style="align-items:flex-start;">
    <div class="card">
      <form class="contact-form" method="post" novalidate>
        <div class="form-grid">
          <div class="form-field">
            <label for="name">Full name</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div class="form-field">
            <label for="email">Email address</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div class="form-field">
            <label for="phone">Phone number</label>
            <input type="tel" id="phone" name="phone">
          </div>
          <div class="form-field">
            <label for="type">Type of care business</label>
            <select id="type" name="type">
              <option>Residential / Nursing Care Home</option>
              <option>Home Care / Domiciliary Agency</option>
              <option>Private Clinic or Practice</option>
              <option>Multi-Site Care Group</option>
              <option>Other</option>
            </select>
          </div>
          <div class="form-field full">
            <label for="message">Tell us about your goals</label>
            <textarea id="message" name="message" placeholder="E.g. we're struggling to fill beds, our website is outdated, we're losing enquiries..."></textarea>
          </div>
        </div>
        <p class="form-hp" aria-hidden="true">
          <label for="company-website">Leave this field empty</label>
          <input type="text" id="company-website" name="company-website" tabindex="-1" autocomplete="off">
        </p>
        <p class="form-consent">
          By sending this form you agree to us storing these details so we can reply
          to your enquiry. We never sell your data or add you to a mailing list without
          asking. See our <a href="/privacy">Privacy Policy</a>.
        </p>
        <button type="submit" class="btn btn-primary btn-block">Book My Free Audit</button>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
      <div class="form-confirmation" tabindex="-1" style="display:none;text-align:center;padding:2rem 0;">
        <h3>Thanks, that's on its way to us.</h3>
        <p>We'll be in touch within one working day to arrange your free audit.</p>
      </div>
    </div>
    <div>
      <div class="card" style="margin-bottom:1.5rem;">
        <h4>Direct Contact</h4>
        <p>Email: <a href="mailto:hello@carerm.co.uk">hello@carerm.co.uk</a><br>Based in Manchester, serving care providers UK-wide.</p>
      </div>
      <div class="card" style="margin-bottom:1.5rem;">
        <h4>What happens next?</h4>
        <ul class="price-features">
          <li>We review your current Google presence and website</li>
          <li>We send over a short, honest audit with quick wins</li>
          <li>We recommend a plan, with no pressure to commit</li>
        </ul>
      </div>
      <img src="/assets/images/person-laptop.webp" alt="Care Reach Marketing team member reviewing a client enquiry" style="border-radius:12px;box-shadow:var(--shadow-md);" width="1200" height="1800" loading="lazy" decoding="async">
    </div>
  </div>
</section>
"""

PRIVACY = """
<section class="page-hero container">
  <span class="eyebrow">Legal</span>
  <h1>Privacy Policy</h1>
  <p class="lede center">How Care Reach Marketing collects, uses and protects your personal data.</p>
</section>

<section class="section-alt">
  <div class="container prose" style="max-width:800px;">
    <p><strong>Last updated:</strong> 18 August 2026</p>

    <div class="notice">
      <strong>Before publishing:</strong> the bracketed details below still need
      completing — your registered address, ICO registration number (if you are
      required to register) and your data retention period. Have a solicitor or
      your ICO-registered data protection contact review this before launch. It
      is a sound starting template, not legal advice.
    </div>

    <h2>Who we are</h2>
    <p>Care Reach Marketing ("we", "us") is a digital marketing agency serving UK care providers, based in Manchester, United Kingdom. For the purposes of UK GDPR and the Data Protection Act 2018, we are the data controller for the personal data described in this policy.</p>
    <p>If you have any questions about this policy or about how we handle your data, contact us at <a href="mailto:hello@carerm.co.uk">hello@carerm.co.uk</a>.</p>
    <p><strong>Registered address:</strong> [ADD YOUR REGISTERED OR TRADING ADDRESS]<br>
    <strong>ICO registration number:</strong> [ADD IF REGISTERED WITH THE ICO]</p>

    <h2>What personal data we collect</h2>
    <p>We only collect data you choose to give us. When you complete the enquiry form on our contact page, we collect:</p>
    <ul class="price-features">
      <li>Your full name</li>
      <li>Your email address</li>
      <li>Your phone number, if you provide one (optional)</li>
      <li>The type of care business you run</li>
      <li>Anything you write in the message field</li>
    </ul>
    <p>If you email us directly, we hold whatever you include in that email.</p>

    <h2>Why we use it, and our lawful basis</h2>
    <p>We use the details above solely to respond to your enquiry, to prepare and send the free audit you asked for, and to discuss whether our services suit your business.</p>
    <p>Our lawful basis is <strong>legitimate interests</strong> (responding to a business enquiry you initiated) and, where you go on to become a client, <strong>performance of a contract</strong>. We do not add enquiry contacts to a marketing mailing list unless you separately and explicitly ask us to.</p>

    <h2>How long we keep it</h2>
    <p>We keep enquiry data for [ADD RETENTION PERIOD, E.G. 24 MONTHS] from your last contact with us, after which it is deleted. Client records are kept for as long as we work together, and then for six years after the end of the engagement to meet UK accounting and tax requirements.</p>

    <h2>Who we share it with</h2>
    <p>We do not sell your personal data, and we never share it with third parties for their own marketing. We share it only with service providers who help us operate, and only as far as they need it:</p>
    <ul class="price-features">
      <li><strong>Our website host (Vercel Inc.)</strong> — serves this website and keeps standard server logs, which include IP addresses.</li>
      <li><strong>Our form and email providers</strong> — receive and store enquiry messages so we can read and reply to them.</li>
      <li><strong>Google Fonts</strong> — this site loads fonts from Google's servers, so your browser sends Google your IP address when a page loads.</li>
    </ul>
    <p>Some of these providers process data outside the UK. Where that happens, the transfer is covered by the UK's International Data Transfer Agreement or equivalent safeguards.</p>

    <h2>Cookies</h2>
    <p>This website does not set any cookies of its own, and we do not run analytics or advertising trackers on it. If that changes we will update this policy and add a cookie banner before doing so.</p>

    <h2>Your rights</h2>
    <p>Under UK data protection law you have the right to:</p>
    <ul class="price-features">
      <li>Ask for a copy of the personal data we hold about you</li>
      <li>Ask us to correct anything inaccurate</li>
      <li>Ask us to delete your data</li>
      <li>Object to, or ask us to restrict, how we use it</li>
      <li>Ask us to transfer it to another provider</li>
    </ul>
    <p>Email <a href="mailto:hello@carerm.co.uk">hello@carerm.co.uk</a> to exercise any of these. We will respond within one month.</p>
    <p>If you are unhappy with how we have handled your data, you can complain to the Information Commissioner's Office at <a href="https://ico.org.uk" rel="noopener">ico.org.uk</a> or on 0303 123 1113. We would appreciate the chance to put things right first.</p>

    <h2>Changes to this policy</h2>
    <p>If we change how we handle personal data, we will update this page and change the "last updated" date above.</p>
  </div>
</section>
"""

NOT_FOUND = """
<section class="page-hero container">
  <span class="eyebrow">Error 404</span>
  <h1>We couldn't find that page.</h1>
  <p class="lede center">The link may be out of date, or the page may have moved. Here's where most people are heading.</p>
  <div class="hero-actions" style="justify-content:center;">
    <a href="/" class="btn btn-primary">Back to Home</a>
    <a href="/contact" class="btn btn-outline" style="color:#1F2421;">Book a Free Audit</a>
  </div>
</section>

<section class="section-alt">
  <div class="container grid grid-3">
    <div class="card">
      <h3>Our Services</h3>
      <p>Google Business Profile, websites and SEO, content, CRM automation and paid advertising.</p>
      <a href="/services">See services &rarr;</a>
    </div>
    <div class="card">
      <h3>Pricing</h3>
      <p>Three transparent tiers with no hidden setup fees and short minimum terms.</p>
      <a href="/pricing">See pricing &rarr;</a>
    </div>
    <div class="card">
      <h3>Questions</h3>
      <p>Contract length, timelines, compliance and reporting, answered plainly.</p>
      <a href="/faq">Read the FAQ &rarr;</a>
    </div>
  </div>
</section>
"""

PAGES = [
    ("index.html", "Care Home Marketing Agency UK", "UK digital marketing agency for care homes, home care agencies and clinics. Get more enquiries with Google, website, content and CRM support. Book a free audit.", "index.html", HOME),
    ("about.html", "About Our Care Marketing Team", "Care Reach Marketing is a UK digital marketing agency built exclusively for the care sector. Learn about our approach, values and how we work.", "about.html", ABOUT),
    ("services.html", "Marketing Services for Care Providers", "Google Business Profile, websites, SEO, content, CRM automation and paid advertising — five services built for UK care homes and clinics.", "services.html", SERVICES),
    ("case-studies.html", "Care Marketing Case Studies", "See how Care Reach Marketing tackles common marketing challenges for UK care homes, home care agencies and clinics. Explore example engagements.", "case-studies.html", CASE_STUDIES),
    ("pricing.html", "Care Marketing Pricing & Packages", "Three transparent pricing tiers for UK care providers, from £449/month. No hidden setup fees, short minimum terms. Compare plans and get started.", "pricing.html", PRICING),
    ("industries.html", "Care Marketing by Sector", "Tailored digital marketing for residential care homes, home care agencies, private clinics and multi-site care groups across the UK.", "industries.html", INDUSTRIES),
    ("resources.html", "Care Marketing Resources & Guides", "Practical, no-nonsense digital marketing guidance for UK care providers: local SEO, enquiry management, CQC marketing and recruitment content.", "resources.html", RESOURCES),
    ("faq.html", "Care Marketing FAQs", "Answers to common questions about working with Care Reach Marketing, including contract terms, timelines, compliance and reporting.", "faq.html", FAQ),
    ("privacy.html", "Privacy Policy", "How Care Reach Marketing collects, uses, stores and protects your personal data, and how to exercise your data protection rights.", "privacy.html", PRIVACY),
    ("contact.html", "Book a Free Care Marketing Audit", "Get in touch with Care Reach Marketing to book a free audit for your UK care business. We reply to every enquiry personally within one working day.", "contact.html", CONTACT),
]
