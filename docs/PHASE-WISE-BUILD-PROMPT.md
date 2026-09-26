# SHOW.MEDIA — Phase-wise Build Prompt

Domain: **show.media** · Brand: **SHOW.MEDIA** (always stylised with the dot — see trademark note at the end)
Concept: **"What to watch" streaming & show discovery hub** + entertainment video + Creator Spotlight + contests + live events, fully monetisable on a free static host (GitHub Pages).

Each phase below is a self-contained prompt you can hand to an AI coding agent (or a developer). Phases are cumulative; run them in order.

---

## Phase 0 — Positioning & revenue model (decision prompt)

> Act as a media-business strategist. Using the domain show.media, define an independent entertainment hub whose primary search intent is "what to watch on [service]" and "is [title] worth watching". Produce: (1) a one-line positioning, (2) the 7 revenue streams ranked by expected yield in year one for a static site (AdSense display; streaming/ticket affiliate; sponsored "Presented by" verdicts; branded contests with e-mail opt-ins; creator collaboration packages; reader support/memberships; domain/website partnership inquiries), (3) target RPM assumptions (entertainment display $5–15 Tier-1; assume $8 blended), (4) a 12-month traffic plan built on long-tail service+genre pages and a weekly newsletter, (5) a trademark-safe brand rule: never use the two-word wordmark "Show Media"; always "SHOW.MEDIA"; publish a non-affiliation disclosure covering Show Media LLC (Las Vegas OOH advertising) and Show Media Limited (UK).

Numbers to design around: 100k pageviews/month × $8 RPM ≈ $800 display; affiliate at 1% click-to-signup on 3% CTR ≈ $300–600; one sponsored feature/month at $750; one branded contest/quarter at $1,500 + prize → ~$2.5–3k/month at 100k views, scaling linearly.

## Phase 1 — Information architecture & design system

> Build a static, no-backend, GitHub-Pages-compatible site skeleton for SHOW.MEDIA. Flat HTML files at repo root (index.html, watch.html, show.html, news.html, videos.html, creators.html, contests.html, events.html, support.html, advertise.html, careers.html, newsletter.html, contact.html, about.html, plus privacy, terms, cookies, dmca, editorial-policy, disclaimer, sitemap.html, 404.html). Relative asset paths only (must work at username.github.io/repo/ and at show.media). Design system: CSS custom properties, dark default + light toggle persisted in localStorage, Inter from Google Fonts, 1240px container, 16px mobile gutter, poster cards (2:3), horizontal scroll-snap rails, article cards, sticky glass header with search + Subscribe CTA + burger drawer, cookie notice, toast. Every page: top banner "Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership" linking to https://web.works/contact; footer with Discover / Community / Business / Company columns, non-affiliation + trademark line, affiliate/AdSense disclosure. No horizontal scroll at 390px.

## Phase 2 — Content engine (shows, articles, video)

> Implement a JSON-driven catalogue (assets/data/shows.json: id, title, year, type, genre[], platform, score, trend, synopsis, seasons, rating, hue). Render: Top-10 trending rail (score + 2×trend), New-this-season rail, per-platform rails, top-rated chart; watch.html with chips for service/type/genre + title filter + ?platform= deep links; show.html?id= detail page with anchor jump-nav (Where to watch → Verdict → Trailer → More like this), "Show Score" badge, affiliate where-to-watch buttons resolved from config, Stream-It-or-Skip-It verdict logic (≥90 tonight, ≥85 stream it), related titles by shared genre. Header search with live results across the catalogue. Six evergreen articles with Article JSON-LD, share button, related cards. Video hub embedding YouTube uploads playlists via youtube-nocookie with a config array of playlist IDs; channel subscribe CTA.

## Phase 3 — Monetisation layer

> Add a single config object (assets/js/config.js) holding: AdSense client + slot IDs with an enabled flag; affiliate URLs per platform + ticketing; YouTube channel and playlists; support links (Ko-fi, Buy Me a Coffee, PayPal, GitHub Sponsors) and a monthly goal; socials. Reserve fixed-height ad slots (leaderboard 970×90 under hero/page-head, sticky 300×600 sidebar, 300×250 in-feed after 2nd content block, mobile anchor) that render a labelled placeholder until AdSense is enabled, then inject <ins class="adsbygoogle"> with zero CLS. Mark affiliate links rel="noopener sponsored". Add ads.txt placeholder. Add sitemap.xml, robots.txt, canonical/OG/Twitter meta, WebSite + SearchAction JSON-LD, manifest.

## Phase 4 — Lead generation (the money section)

> Build one reusable, high-conversion "Work with SHOW.MEDIA" section and place it on the homepage, advertise.html, contact.html, creators.html and events.html. Left: benefit copy + 4 checkmarks + trust row (no agency mark-up, transparent reporting, replies in 48h). Right: 3-step form with progress bar — Step 1 intent (sponsorship / branded contest / partnership / buying-leasing domain-website / creator placement / other) + budget band; Step 2 company, website, success definition; Step 3 name, work e-mail, timeline, consent. Client-side validation per step, honeypot, AJAX submission to FormSubmit with the inbox address stored obfuscated (rot13 + assembled at runtime) and NEVER printed in the DOM or HTML. All other forms (newsletter multi-list picker, creator submission, contest entry, event listing, job application, contact) use the same handler and the same single inbox. Success and error states inline. Exit-intent newsletter hook.

## Phase 5 — Community & operations pages

> Creators: stat row (free, 7-day response, 3 channels, you keep rights), 6 spotlight cards, submission form with rights checkbox and "what we don't accept" list. Contests: 4 live contests with prize, live countdown (data-deadline), rules summary, one universal entry form with opt-in checkbox, sponsor-a-contest CTA. Events: date-block cards with affiliate ticket buttons, filter chips, free organiser listing form. Support: monthly goal progress bar from config, three tiers (one-time $5+, member $5/mo, patron $25/mo), fund allocation split, supporter wall, "other ways to help". Careers: role table + one application/talent-pool form. Newsletter: dedicated page with four lists.

## Phase 6 — Legal, trust & compliance

> Write privacy (AdSense cookie language + Google Ads Settings opt-out, GDPR/CCPA rights, form-relay retention), terms (contest rules: 18+, void where prohibited, one entry, prize payment within 30 days, licence to display; creator submission licence; donations non-refundable and buy no influence), cookie policy, DMCA, editorial policy (scores never for sale, corrections, AI-use statement), and a disclaimer page with the full trademark/copyright disclosure (nominative fair use of service and title names; artwork generated, not official key art; videos embedded from rights holders).

## Phase 7 — QA & launch

> Run: grep for the inbox address in all HTML (must be zero hits); internal link checker; Playwright at 1366×900 and 390×844 on 8 key pages — assert no page errors, scrollWidth ≤ viewport, search returns results, multi-step form advances; Lighthouse ≥ 90 performance/SEO. Push to github.com/webworksa1/showmedia-com (main). Add .github/workflows/pages.yml using actions/configure-pages (enablement: true), upload-pages-artifact and deploy-pages so Pages is enabled automatically on first push. Add CNAME "show.media" and .nojekyll. DNS: A records 185.199.108–111.153 + CNAME www → webworksa1.github.io; enable "Enforce HTTPS".

## Phase 8 — Growth backlog (post-launch)

> (a) Replace sample catalogue with a nightly GitHub Action that pulls JustWatch/TMDB-style data into shows.json; (b) per-service landing pages (new-on-netflix.html …) generated from the JSON for long-tail SEO; (c) YouTube video IDs per title for inline trailers; (d) Ko-fi/BMC webhooks → supporters.json for the live wall; (e) Buttondown/Beehiiv for newsletter automation; (f) Cloudflare in front for analytics + caching; (g) programmatic "is [title] worth watching" pages; (h) contest voting via a free Firebase/Supabase table if public voting is needed.

---

### Trademark / copyright note (apply in every phase)
"Show Media" is used by unrelated businesses (Show Media LLC, Las Vegas — out-of-home advertising; Show Media Limited, UK). This site is a consumer entertainment publication, never an advertising-services agency, and never uses the two-word mark alone. Brand as SHOW.MEDIA; keep the non-affiliation disclosure in the footer and on /disclaimer.html.
