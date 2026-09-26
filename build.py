#!/usr/bin/env python3
"""SHOW.MEDIA static site generator. Run: python3 build.py  (outputs *.html at repo root)"""
import os, json, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://show.media/"
TODAY = datetime.date.today().isoformat()

NAV = [("index.html","Home"),("watch.html","What to Watch"),("news.html","News"),("videos.html","Videos"),
       ("creators.html","Creators"),("contests.html","Contests"),("events.html","Events"),("support.html","Support")]

def shell(title, desc, body, canonical, extra_head="", schema=None):
    menu = "".join(f'<a href="{h}">{t}</a>' for h,t in NAV)
    drawer = "".join(f'<a href="{h}">{t}</a>' for h,t in NAV) + '<a href="advertise.html">Advertise & Sponsor</a><a href="careers.html">Careers</a><a href="newsletter.html">Newsletter</a><a href="contact.html">Contact</a>'
    sch = f'<script type="application/ld+json">{json.dumps(schema)}</script>' if schema else ""
    return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{canonical}">
<meta property="og:type" content="website"><meta property="og:site_name" content="SHOW.MEDIA"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{DOMAIN}{canonical}"><meta property="og:image" content="{DOMAIN}assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0d12">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{sch}{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="top-banner">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership — <a data-owner-contact href="https://web.works/contact">web.works/contact</a></div>
<header class="header"><div class="wrap nav">
  <a class="logo" href="index.html" aria-label="SHOW.MEDIA home"><span class="dot"></span>SHOW<span class="tld">.MEDIA</span></a>
  <nav class="menu" aria-label="Primary">{menu}</nav>
  <div class="nav-right">
    <div class="search" role="search"><span aria-hidden="true">⌕</span><input id="site-search" type="search" placeholder="Search shows, movies…" aria-label="Search" autocomplete="off"></div>
    <button class="icon-btn" data-theme-toggle aria-label="Toggle theme">◐</button>
    <a class="btn btn-primary btn-sm" href="newsletter.html">Subscribe</a>
    <button class="icon-btn burger" data-drawer aria-label="Menu">☰</button>
  </div>
  <div class="search-results" id="search-results"></div>
</div></header>
<div class="drawer" id="drawer"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px"><b>Menu</b><button class="icon-btn" data-drawer aria-label="Close">✕</button></div>{drawer}</div>
<main id="main">
{body}
</main>
<footer class="footer"><div class="wrap">
  <div class="footer-grid">
    <div><a class="logo" href="index.html"><span class="dot"></span>SHOW<span class="tld">.MEDIA</span></a>
      <p class="muted small" style="margin-top:10px;max-width:320px">Independent guide to what's worth watching, the people making it, and where to find it. Built for fans, creators and the brands that want to reach them.</p>
      <div class="socials"><a data-link="social.youtube" href="#" aria-label="YouTube">▶</a><a data-link="social.x" href="#" aria-label="X">𝕏</a><a data-link="social.instagram" href="#" aria-label="Instagram">◎</a><a data-link="social.tiktok" href="#" aria-label="TikTok">♪</a><a data-link="social.facebook" href="#" aria-label="Facebook">f</a></div></div>
    <div><h4>Discover</h4><a href="watch.html">What to Watch</a><a href="watch.html?platform=netflix">New on Netflix</a><a href="watch.html?platform=prime">Best on Prime Video</a><a href="watch.html?platform=max">Best on HBO Max</a><a href="news.html">News & Reviews</a><a href="videos.html">Trailers & Video</a><a href="events.html">Live Events</a></div>
    <div><h4>Community</h4><a href="creators.html">Creator Spotlight</a><a href="creators.html#submit">Submit your work</a><a href="contests.html">Contests & Prizes</a><a href="support.html">Support the site</a><a href="newsletter.html">Newsletter</a></div>
    <div><h4>Business</h4><a href="advertise.html">Advertise & Sponsor</a><a href="advertise.html#partner">Partnerships</a><a href="advertise.html#media-kit">Media kit</a><a href="careers.html">Careers & Talent</a><a href="contact.html">Contact</a></div>
    <div><h4>Company</h4><a href="about.html">About</a><a href="editorial-policy.html">Editorial policy</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="cookies.html">Cookies</a><a href="dmca.html">DMCA</a><a href="disclaimer.html">Disclaimer & trademarks</a><a href="sitemap.html">Sitemap</a></div>
  </div>
  <div class="legal">
    <p>© <span data-year>2026</span> SHOW.MEDIA. All rights reserved. SHOW.MEDIA is an independent publication operated under the domain name show.media. It is not affiliated with, endorsed by, or connected to any company trading as “Show Media”, including Show Media LLC (Las Vegas, NV) or Show Media Limited (UK), nor with Netflix, Amazon, Disney, Warner Bros. Discovery, Apple, Paramount, NBCUniversal or any streaming service, studio or network mentioned. All titles, logos and trademarks belong to their respective owners and are used for identification and commentary only. <a href="disclaimer.html" style="display:inline">Full disclosure →</a></p>
    <p>Some links are affiliate links; we may earn a commission at no extra cost to you. This site shows advertising, including Google AdSense. See our <a href="privacy.html" style="display:inline">privacy policy</a> and <a href="cookies.html" style="display:inline">cookie policy</a>.</p>
  </div>
</div></footer>
<div class="ad ad-anchor" data-slot="anchor"></div>
<div class="cookie" id="cookie"><span>We use cookies for analytics and personalised ads. <a href="cookies.html" style="text-decoration:underline">Learn more</a></span><button class="btn btn-primary btn-sm" id="cookie-ok">OK</button></div>
<div class="toast" id="toast"></div>
<script src="assets/js/config.js"></script>
<script src="assets/js/app.js"></script>
</body>
</html>"""

def field(name, label, type="text", req=True, ph="", opts=None, rows=None):
    r = " required" if req else ""
    if opts:
        o = "".join(f'<option value="{x}">{x}</option>' for x in opts)
        inp = f'<select name="{name}"{r}><option value="" disabled selected>Select…</option>{o}</select>'
    elif rows:
        inp = f'<textarea name="{name}" rows="{rows}" placeholder="{ph}"{r}></textarea>'
    else:
        inp = f'<input name="{name}" type="{type}" placeholder="{ph}"{r}>'
    return f'<div class="field"><label>{label}{"" if req else " <span class=faint>(optional)</span>"}</label>{inp}</div>'

HP = '<div class="hp" aria-hidden="true"><input type="text" name="_honey" tabindex="-1" autocomplete="off"></div>'
CONSENT = '<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="privacy.html" style="text-decoration:underline">privacy policy</a> and to be contacted about this inquiry.</label>'

def leadgen(compact=False):
    """Dedicated, high-conversion lead-generation section (used on every commercial page)."""
    return f"""
<section class="section" id="work-with-us"><div class="wrap">
 <div class="leadgen">
  <div>
   <span class="eyebrow">Work with SHOW.MEDIA</span>
   <h2>Reach an audience that decides what to watch tonight</h2>
   <p class="muted">Sponsor a spotlight, run a branded contest, place your title in our weekly guide or license our audience for your launch. Tell us the goal — we reply with a proposal and pricing within 2 business days.</p>
   <ul><li>Sponsored “Stream It” reviews, newsletter takeovers and homepage rails</li><li>Contest & giveaway packages with guaranteed entries and email opt-ins</li><li>Creator collaborations, premieres and event coverage</li><li>Domain, website and equity partnership inquiries welcome</li></ul>
   <div class="trust"><span>✓ No agency mark-up</span><span>✓ Transparent reporting</span><span>✓ Replies in 48h</span></div>
  </div>
  <form class="sm card" data-subject="Lead: Work with us" data-thanks="Got it — expect a proposal within 2 business days.">
   <div class="steps"><span></span><span></span><span></span></div>
   <div class="step">
     <h3>1 · What do you need?</h3>
     {field("interest","I'm interested in",opts=["Sponsorship / advertising","Branded contest or giveaway","Partnership / collaboration","Buying or leasing this domain / website","Creator or talent placement","Something else"])}
     {field("budget","Monthly budget",opts=["Under $500","$500 – $2,000","$2,000 – $10,000","$10,000+","Not sure yet"])}
     <button type="button" class="btn btn-primary btn-block" data-next>Continue →</button>
   </div>
   <div class="step">
     <h3>2 · Tell us about the project</h3>
     {field("company","Company / brand",ph="Acme Studios")}
     {field("website","Website",type="url",req=False,ph="https://")}
     {field("goal","What does success look like?",rows=3,ph="e.g. 5,000 trailer views and 800 newsletter opt-ins during launch week")}
     <div class="row"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div>
   </div>
   <div class="step">
     <h3>3 · Where should we send the proposal?</h3>
     <div class="row">{field("name","Your name",ph="Jane Doe")}{field("email","Work e-mail",type="email",ph="you@company.com")}</div>
     {field("timeline","Timeline",opts=["This month","Next 1–3 months","Later this year","Just exploring"])}
     {CONSENT}{HP}
     <div class="row"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="submit" class="btn btn-primary" data-label="Request proposal">Request proposal</button></div>
     <div class="form-status" role="status"></div>
   </div>
  </form>
 </div>
</div></section>"""

def newsletter():
    return f"""
<section class="section"><div class="wrap">
 <div class="newsletter">
  <div><span class="eyebrow">Free newsletter</span><h2>Three picks. Every Friday. Zero filler.</h2><p class="muted">Join fans who let us do the scrolling. Pick the lists you want:</p>
   <div class="nl-lists" id="nl-lists"></div></div>
  <form class="sm" data-subject="Newsletter signup" data-thanks="You're on the list. Check your inbox to confirm.">
   <div class="nl-lists">
    <label class="check"><input type="checkbox" name="list_weekly" value="yes" checked> <b>Watch This Weekend</b> — 3 picks every Friday</label>
    <label class="check"><input type="checkbox" name="list_new" value="yes" checked> <b>New This Week</b> — everything landing on every service</label>
    <label class="check"><input type="checkbox" name="list_contests" value="yes"> <b>Contests & Prizes</b> — early access to giveaways</label>
    <label class="check"><input type="checkbox" name="list_creators" value="yes"> <b>Creator Spotlight</b> — new talent, casting and collaboration calls</label>
   </div>
   <div class="inline-form"><input type="email" name="email" placeholder="your@email.com" required aria-label="E-mail"><button class="btn btn-primary" type="submit" data-label="Subscribe free">Subscribe free</button></div>
   {HP}<p class="form-note">No spam. Unsubscribe in one click. See <a href="privacy.html" style="text-decoration:underline">privacy</a>.</p>
   <div class="form-status" role="status"></div>
  </form>
 </div>
</div></section>"""

def support_strip():
    return """
<section class="section" style="padding-top:0"><div class="wrap">
 <div class="card" style="display:grid;grid-template-columns:1fr auto;gap:20px;align-items:center">
  <div><b>Independent, reader-supported.</b> <span class="muted">No paywall. If SHOW.MEDIA saved you from a bad night on the couch, chip in for the next one.</span></div>
  <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-accent btn-sm" data-link="support.kofi" href="#">☕ Tip on Ko-fi</a><a class="btn btn-ghost btn-sm" href="support.html">All ways to support</a></div>
 </div>
</div></section>"""

def page_head(eyebrow, h1, lead, crumb=""):
    return f"""<section class="page-head"><div class="wrap">{('<div class="breadcrumb"><a href="index.html">Home</a> › '+crumb+'</div>') if crumb else ''}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead muted" style="max-width:720px;font-size:1.1rem">{lead}</p></div></section>"""

PAGES = {}

# ---------------------------------------------------------------- HOME
PAGES["index.html"] = dict(title="SHOW.MEDIA — What to Watch Tonight: Streaming Guide, Trailers, Creators & Contests",
 desc="Find what to watch on Netflix, Prime Video, Disney+, HBO Max, Apple TV+ and more. Daily trending charts, Stream-It-or-Skip-It verdicts, trailers, creator spotlights and contests.",
 schema={"@context":"https://schema.org","@type":"WebSite","name":"SHOW.MEDIA","url":DOMAIN,"potentialAction":{"@type":"SearchAction","target":DOMAIN+"watch.html?q={search_term_string}","query-input":"required name=search_term_string"}},
 body=f"""
<section class="hero"><div class="wrap">
 <span class="eyebrow">Updated daily · Independent · Free</span>
 <h1>Never waste a night <span>deciding what to watch</span></h1>
 <p class="lead">One place for every streaming service: today's trending shows, honest Stream-It-or-Skip-It verdicts, official trailers, live events near you — plus the creators and contests shaping what's next.</p>
 <div class="hero-actions"><a class="btn btn-primary" href="watch.html">Find something to watch</a><a class="btn btn-ghost" href="videos.html">▶ Watch trailers</a><a class="btn btn-ghost" href="contests.html">Enter a contest</a></div>
 <div class="platform-strip">
  <a href="watch.html?platform=netflix"><i style="background:#e50914"></i>Netflix</a><a href="watch.html?platform=prime"><i style="background:#00a8e1"></i>Prime Video</a><a href="watch.html?platform=disney"><i style="background:#1f80e0"></i>Disney+</a><a href="watch.html?platform=max"><i style="background:#8a2be2"></i>HBO Max</a><a href="watch.html?platform=apple"><i style="background:#a5a5a5"></i>Apple TV+</a><a href="watch.html?platform=hulu"><i style="background:#1ce783"></i>Hulu</a><a href="watch.html?platform=peacock"><i style="background:#ffcc4d"></i>Peacock</a>
 </div>
 <div class="hero-stats"><div><b>8</b><span>services tracked</span></div><div><b>Daily</b><span>trending refresh</span></div><div><b>100%</b><span>free, no paywall</span></div><div><b>1 e-mail</b><span>a week, that's it</span></div></div>
</div></section>
<div class="wrap"><div class="ad ad-leader" data-slot="leaderboard"></div></div>
<section class="section"><div class="wrap">
 <div class="section-head"><div><span class="eyebrow">Trending now</span><h2>Top 10 this week</h2></div><a class="btn btn-ghost btn-sm" href="watch.html">See full chart →</a></div>
 <div class="rail" data-rail="trending" data-limit="10"></div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
 <div class="section-head"><div><span class="eyebrow">Just landed</span><h2>New this season</h2></div><a class="btn btn-ghost btn-sm" href="watch.html">Everything new →</a></div>
 <div class="rail" data-rail="new" data-limit="10"></div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
 <div class="with-side">
  <div>
   <div class="section-head"><div><span class="eyebrow">Stream it or skip it</span><h2>Latest verdicts & news</h2></div><a class="btn btn-ghost btn-sm" href="news.html">All stories →</a></div>
   <div class="grid g2">
    <a class="article" href="article-streaming-price-hikes.html"><div class="thumb" style="background:linear-gradient(160deg,#ff3d71,#3d1a2b)">Every streaming price hike, ranked</div><div class="body"><span class="kicker">Money</span><h3>Every streaming price hike of the year — and which services are still worth it</h3><p class="muted small">We rank all eight services by cost-per-hour of must-watch TV.</p><span class="by">SHOW.MEDIA Staff · 6 min read</span></div></a>
    <a class="article" href="article-binge-or-weekly.html"><div class="thumb" style="background:linear-gradient(160deg,#3dd6ff,#0f2a3a)">Binge drop vs weekly episodes</div><div class="body"><span class="kicker">Analysis</span><h3>Binge drops vs. weekly episodes: the data on which one keeps shows alive</h3><p class="muted small">Weekly releases now dominate the top 10 — here's why.</p><span class="by">SHOW.MEDIA Staff · 5 min read</span></div></a>
    <a class="article" href="article-how-we-score.html"><div class="thumb" style="background:linear-gradient(160deg,#38d39f,#0f3a2a)">How the Show Score works</div><div class="body"><span class="kicker">Inside SHOW.MEDIA</span><h3>How the Show Score works (and why it's not just another aggregate)</h3><p class="muted small">Critic consensus, audience sentiment and momentum — weighted.</p><span class="by">Editors · 4 min read</span></div></a>
    <a class="article" href="article-free-streaming-guide.html"><div class="thumb" style="background:linear-gradient(160deg,#ffcc4d,#3a2f0f)">Best free streaming services</div><div class="body"><span class="kicker">Guide</span><h3>The best free, legal streaming services — and what's actually good on them</h3><p class="muted small">Tubi, Pluto, Plex, The Roku Channel, Freevee and more compared.</p><span class="by">SHOW.MEDIA Staff · 7 min read</span></div></a>
   </div>
  </div>
  <aside><div class="ad ad-side" data-slot="sidebar"></div></aside>
 </div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
 <div class="section-head"><div><span class="eyebrow">Watch</span><h2>Trailers & first looks</h2></div><a class="btn btn-ghost btn-sm" href="videos.html">Video hub →</a></div>
 <div class="video-grid" data-yt-playlists></div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
 <div class="grid g3">
  <div class="card"><span class="eyebrow">Creators</span><h3>Get your show in front of fans</h3><p class="muted">Short films, series pilots, podcasts, channels — submit for a free Creator Spotlight review.</p><a class="btn btn-ghost btn-sm" href="creators.html">Creator Spotlight →</a></div>
  <div class="card"><span class="eyebrow">Contests</span><h3>Win prizes for watching, writing & making</h3><p class="muted">Monthly contests with cash, gear and streaming subscriptions. Free to enter.</p><a class="btn btn-ghost btn-sm" href="contests.html">Open contests →</a></div>
  <div class="card"><span class="eyebrow">Events</span><h3>Premieres, screenings & tours near you</h3><p class="muted">Live events with tickets, fan meetups and festival dates.</p><a class="btn btn-ghost btn-sm" href="events.html">Browse events →</a></div>
 </div>
</div></section>
{leadgen()}
{newsletter()}
{support_strip()}
""")

# ---------------------------------------------------------------- WATCH
plat_chips = "".join(f'<span class="chip" data-filter="platform:{k}">{v}</span>' for k,v in [("netflix","Netflix"),("prime","Prime Video"),("disney","Disney+"),("max","HBO Max"),("apple","Apple TV+"),("hulu","Hulu"),("peacock","Peacock")])
genre_chips = "".join(f'<span class="chip" data-filter="genre:{g}">{g}</span>' for g in ["Drama","Comedy","Thriller","Sci-Fi","Horror","Action","Animation","Mystery","Fantasy","History"])
PAGES["watch.html"] = dict(title="What to Watch Tonight — Best Shows & Movies on Every Streaming Service | SHOW.MEDIA",
 desc="Browse the best shows and movies on Netflix, Prime Video, Disney+, HBO Max, Apple TV+, Hulu and Peacock. Filter by service, genre and type. Updated daily.",
 body=f"""
{page_head("Streaming guide","What to watch tonight","Every title ranked by the Show Score — critic consensus, audience sentiment and this week's momentum. Filter by service and genre, then hit a title for where to watch.","What to Watch")}
<div class="wrap"><div class="ad ad-leader" data-slot="leaderboard"></div></div>
<section class="section" style="padding-top:10px"><div class="wrap">
 <div class="filters"><span class="chip on" data-filter="platform:all">All services</span>{plat_chips}</div>
 <div class="filters"><span class="chip on" data-filter="type:all">Shows & movies</span><span class="chip" data-filter="type:TV">TV shows</span><span class="chip" data-filter="type:Movie">Movies</span></div>
 <div class="filters"><span class="chip on" data-filter="genre:all">All genres</span>{genre_chips}</div>
 <div class="section-head"><div class="search" style="display:flex;max-width:360px"><span>⌕</span><input id="cat-q" type="search" placeholder="Filter by title" aria-label="Filter by title"></div><span class="muted small" id="cat-count"></span></div>
 <div class="grid-posters" data-catalogue></div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
 <div class="section-head"><div><span class="eyebrow">Charts</span><h2>Top-rated of all time</h2></div></div>
 <div class="rail" data-rail="top" data-limit="12"></div>
 <div class="ad ad-infeed" data-slot="infeed" style="margin-top:28px"></div>
</div></section>
{newsletter()}
""")

PAGES["show.html"] = dict(title="Show — Where to watch, verdict & score | SHOW.MEDIA", desc="Where to watch, Stream-It-or-Skip-It verdict, trailer and similar titles.",
 body="""<section class="section"><div class="wrap" data-show-page><p class="muted">Loading…</p></div></section>""")

# ---------------------------------------------------------------- NEWS + articles
ARTICLES = {
 "article-streaming-price-hikes.html": ("Money","Every streaming price hike of the year — and which services are still worth it",
   """<p>Every major service raised prices again this year. The question is not whether streaming got more expensive — it did — but which subscriptions still pay for themselves in hours of television you would actually recommend.</p>
<h2>How we measured it</h2><p>We took each service's current ad-free monthly price and divided it by the number of hours of content scoring 85+ on the Show Score that arrived in the last twelve months. That gives a cost per must-watch hour — the only number that matters when you're deciding what to cancel.</p>
<h2>The ranking</h2><table><tr><th>Service</th><th>Verdict</th><th>Why</th></tr><tr><td>Apple TV+</td><td>Keep</td><td>Smallest catalogue, highest hit rate. Slow Horses, Severance and The Studio alone justify it.</td></tr><tr><td>HBO Max</td><td>Keep</td><td>Prestige library plus Warner theatrical window. Best cost-per-hour for movie fans.</td></tr><tr><td>Netflix</td><td>Keep (ad tier)</td><td>Volume masks a mid hit rate; the ad-supported plan is where the value is.</td></tr><tr><td>Hulu</td><td>Rotate</td><td>The Bear and Shōgun are seasonal — subscribe for the run, then pause.</td></tr><tr><td>Prime Video</td><td>Bundle only</td><td>Rarely worth it standalone; excellent as a Prime add-on.</td></tr><tr><td>Disney+</td><td>Rotate</td><td>Andor is a masterpiece; the rest is family-dependent.</td></tr><tr><td>Peacock</td><td>Rotate</td><td>Great for Universal theatrical windows and live sport, thin otherwise.</td></tr><tr><td>Paramount+</td><td>Cancel</td><td>Unless you're a Taylor Sheridan or Star Trek household.</td></tr></table>
<h2>The rotation strategy</h2><p>Keep two anchors year-round (we'd pick Apple TV+ and HBO Max), then rotate one third service each month based on what's dropping. Our <a href="newsletter.html">New This Week</a> newsletter is built precisely for that decision.</p>"""),
 "article-binge-or-weekly.html": ("Analysis","Binge drops vs. weekly episodes: the data on which one keeps shows alive",
   """<p>For a decade the binge drop was the default. Then the weekly show came back — and it's now winning the conversation. Here's what the trending data on this site says about why.</p>
<h2>Weekly shows stay in the chart four times longer</h2><p>Titles released weekly hold a top-10 position for an average of five to six weeks. Full-season drops peak in week one and are usually gone by week three. For a streamer, that's the difference between one news cycle and a season-long marketing campaign that the audience runs for free.</p>
<h2>The exceptions prove the rule</h2><p>Global event drops — Squid Game, Stranger Things — still work as binges because the fandom does the pacing itself. Everything below that tier benefits from a weekly cadence.</p>
<h2>What it means for you</h2><p>If a show you love is weekly, the smart move is to start it two episodes late and never wait a week again. Our show pages flag the release cadence so you can plan around it.</p>"""),
 "article-how-we-score.html": ("Inside SHOW.MEDIA","How the Show Score works (and why it's not just another aggregate)",
   """<p>The Show Score is a single 0–100 number on every title. It exists because critic scores tell you what reviewers thought at premiere and audience scores tell you what fans thought after — neither tells you whether a show is worth your evening <em>tonight</em>.</p>
<h2>Three inputs</h2><ul><li><b>Critic consensus (45%)</b> — normalised across published review aggregates.</li><li><b>Audience sentiment (35%)</b> — verified viewer ratings, de-weighted for review-bombing patterns.</li><li><b>Momentum (20%)</b> — search interest, social mentions and streaming-chart movement over the last seven days.</li></ul>
<h2>What we don't do</h2><p>We don't accept payment to change a score. Sponsored placements are labelled, and they never touch the number. See our <a href="editorial-policy.html">editorial policy</a>.</p>
<h2>Verdicts</h2><p>90+ is “Stream it — tonight”. 85–89 is “Stream it”. Below that, we tell you which audience it's for instead of pretending it's for everyone.</p>"""),
 "article-free-streaming-guide.html": ("Guide","The best free, legal streaming services — and what's actually good on them",
   """<p>Free ad-supported streaming (FAST) is the fastest-growing corner of the industry, and the libraries are far better than their reputation. Here is what's worth your time on each.</p>
<h2>Tubi</h2><p>The largest free library in the US, with an unusually deep horror and cult-movie selection and a growing slate of originals. Best for: movie nights when nobody can agree.</p>
<h2>Pluto TV</h2><p>Channel-surfing reinvented: hundreds of always-on themed channels. Best for: background TV and classic sitcoms.</p>
<h2>The Roku Channel</h2><p>A rotating selection of studio films plus live news and sport. Best for: recent theatrical movies you missed.</p>
<h2>Plex</h2><p>Free movies and live TV alongside a universal watchlist that tracks every other service. Best for: people juggling four subscriptions.</p>
<h2>Freevee & YouTube</h2><p>Amazon's free tier carries surprising originals; YouTube's free movies section is bigger than most people realise. Best for: comedies and documentaries.</p>
<p>Every free service is tagged in our <a href="watch.html">streaming guide</a> with a green “Free” badge.</p>"""),
 "article-fall-tv-preview.html": ("Preview","Fall TV preview: the 12 returning and new shows that will own the conversation",
   """<p>The autumn slate is the most stacked in years. Here is our shortlist, ordered by how confident we are that each will dominate your group chat.</p>
<h2>Returning heavyweights</h2><p>Stranger Things bows out with its final season, Slow Horses continues its perfect run, The Boys sets up its endgame, and Only Murders in the Building somehow finds another body.</p>
<h2>New arrivals to watch</h2><p>Look for limited series from prestige filmmakers moving to television, plus at least two video-game adaptations following the Fallout and The Last of Us playbook.</p>
<h2>How to keep up</h2><p>Our <a href="watch.html">guide</a> updates daily and our Friday newsletter picks the three you actually need. Everything else can wait.</p>"""),
 "article-creator-economy-tv.html": ("Creators","How independent creators are getting shows picked up in 2026 — and how to submit yours",
   """<p>The path from a YouTube pilot or a festival short to a commissioned series has never been shorter. Streamers now scout creator platforms directly, and a spotlight in the right place can start the conversation.</p>
<h2>What buyers look for</h2><p>A clear premise in one line, a pilot or proof-of-concept under 15 minutes, evidence of an audience (even a small, engaged one) and a creator who can talk about season two.</p>
<h2>Where SHOW.MEDIA fits</h2><p>Our <a href="creators.html">Creator Spotlight</a> is free to submit, reviewed by editors within seven days, and featured spotlights are pushed to our newsletter and social channels. Our <a href="contests.html">contests</a> add prize money and jury feedback.</p>"""),
}
def article_cards():
    grads = ["#ff3d71,#3d1a2b","#3dd6ff,#0f2a3a","#38d39f,#0f3a2a","#ffcc4d,#3a2f0f","#8a2be2,#1e0f3a","#ff8a3d,#3a1f0f"]
    out=[]
    for i,(slug,(k,h,_)) in enumerate(ARTICLES.items()):
        out.append(f'<a class="article" href="{slug}"><div class="thumb" style="background:linear-gradient(160deg,{grads[i%6]})">{k}</div><div class="body"><span class="kicker">{k}</span><h3>{h}</h3><span class="by">SHOW.MEDIA Staff · {TODAY}</span></div></a>')
    return "".join(out)

def related_cards(current):
    cards = article_cards().split('</a>')
    keys = list(ARTICLES.keys())
    picks = [cards[i] + '</a>' for i,k in enumerate(keys) if k != current][:2]
    return "".join(picks)

PAGES["news.html"] = dict(title="Streaming News, Reviews & Stream-It-or-Skip-It Verdicts | SHOW.MEDIA",
 desc="Entertainment news, streaming analysis, honest reviews and guides from SHOW.MEDIA's editors.",
 body=f"""
{page_head("News & reviews","Stream it or skip it","Verdicts, guides and analysis — no recaps padded to 2,000 words, no spoilers before the fold.","News")}
<div class="wrap"><div class="ad ad-leader" data-slot="leaderboard"></div></div>
<section class="section" style="padding-top:10px"><div class="wrap"><div class="with-side"><div class="grid g2">{article_cards()}</div><aside><div class="ad ad-side" data-slot="sidebar"></div></aside></div></div></section>
{newsletter()}
""")

for slug,(kicker,head,html) in ARTICLES.items():
    PAGES[slug] = dict(title=f"{head} | SHOW.MEDIA", desc=head,
     schema={"@context":"https://schema.org","@type":"Article","headline":head,"datePublished":TODAY,"author":{"@type":"Organization","name":"SHOW.MEDIA"},"publisher":{"@type":"Organization","name":"SHOW.MEDIA"},"mainEntityOfPage":DOMAIN+slug},
     body=f"""
<section class="page-head"><div class="wrap"><div class="breadcrumb"><a href="index.html">Home</a> › <a href="news.html">News</a> › {kicker}</div><span class="eyebrow">{kicker}</span><h1 style="max-width:820px">{head}</h1><p class="muted small">By SHOW.MEDIA Staff · Published {TODAY} · <button class="btn btn-ghost btn-sm" data-share style="padding:4px 10px">Share</button></p></div></section>
<div class="wrap"><div class="ad ad-leader" data-slot="leaderboard"></div></div>
<section class="section" style="padding-top:10px"><div class="wrap"><div class="with-side"><article class="prose">{html}<div class="ad ad-infeed" data-slot="infeed" style="margin:28px 0"></div><h2>More from SHOW.MEDIA</h2><div class="grid g2">{related_cards(slug)}</div></article><aside><div class="ad ad-side" data-slot="sidebar"></div></aside></div></div></section>
{newsletter()}{support_strip()}""")

# ---------------------------------------------------------------- VIDEOS
PAGES["videos.html"] = dict(title="Trailers, First Looks & Video | SHOW.MEDIA", desc="Official trailers, teasers and first looks from every studio and streamer, updated as they drop.",
 body=f"""
{page_head("Video hub","Trailers & first looks","Official trailers and previews, embedded straight from the studios' channels — updated as they publish.","Videos")}
<div class="wrap"><div class="ad ad-leader" data-slot="leaderboard"></div></div>
<section class="section" style="padding-top:10px"><div class="wrap"><div class="video-grid" data-yt-playlists></div>
<div class="card" style="margin-top:28px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center"><div><b>Subscribe to the SHOW.MEDIA channel</b><br><span class="muted small">Weekly “what to watch” roundups, creator interviews and contest announcements.</span></div><a class="btn btn-primary" data-link="youtube.channelUrl" href="#">▶ Subscribe on YouTube</a></div>
<div class="ad ad-infeed" data-slot="infeed" style="margin-top:28px"></div></div></section>
{newsletter()}""")

# ---------------------------------------------------------------- CREATORS
creators = [("Maya R.","@mayaframes","Short film · Sci-Fi","Winner, Spring Shorts Contest"),("The Late Rewind","@laterewind","Podcast · TV rewatch","Featured spotlight"),("Dev & Ana","@devanafilms","Web series · Comedy","Rising creator"),("Kofi Mensah","@kofishoots","Documentary · Music","Jury pick"),("Nightlight Studio","@nightlightanim","Animation · Fantasy","Featured spotlight"),("Sara Lin","@saralinwrites","Screenwriting · Drama","Finalist, Pilot Script Prize")]
creator_cards = "".join(f'<div class="creator"><div class="avatar">{n[0]}</div><h3 style="margin-bottom:2px">{n}</h3><div class="handle">{h}</div><p class="muted small" style="margin:8px 0">{c}</p><span class="badge badge-new">{b}</span></div>' for n,h,c,b in creators)
PAGES["creators.html"] = dict(title="Creator Spotlight — Submit Your Show, Film, Series or Podcast | SHOW.MEDIA",
 desc="Free Creator Spotlight for independent filmmakers, series creators, podcasters and channels. Submit your work for an editorial feature, newsletter push and social promotion.",
 body=f"""
{page_head("Creator Spotlight","Get your show in front of people who watch everything","Independent films, pilots, web series, podcasts, channels. Free to submit. Reviewed by editors within 7 days. Featured work goes to our newsletter and social channels.","Creators")}
<section class="section" style="padding-top:10px"><div class="wrap">
 <div class="stat-row"><div class="stat"><b>Free</b><span class="muted small">to submit, always</span></div><div class="stat"><b>7 days</b><span class="muted small">editorial response</span></div><div class="stat"><b>3 channels</b><span class="muted small">site · newsletter · social</span></div><div class="stat"><b>You keep</b><span class="muted small">100% of your rights</span></div></div>
 <div class="section-head" style="margin-top:36px"><div><span class="eyebrow">Featured this month</span><h2>Spotlight creators</h2></div></div>
 <div class="grid g3">{creator_cards}</div>
 <div class="ad ad-infeed" data-slot="infeed" style="margin-top:28px"></div>
</div></section>
<section class="section" id="submit"><div class="wrap"><div class="leadgen">
 <div><span class="eyebrow">Submit your work</span><h2>What we look for</h2><p class="muted">Head, heart and craft. A clear premise, a finished piece (or a real pilot), and a creator we can write about.</p>
 <ul><li>Any length; any genre; any language with subtitles</li><li>Link to YouTube, Vimeo, a podcast feed or a private screener</li><li>Must be your own work with clearances for music and footage</li><li>We do not feature ads, showreels, or AI-generated compilations</li></ul>
 <p class="small muted">Want guaranteed placement, a sponsored feature or a paid campaign? See <a href="advertise.html" style="text-decoration:underline">Advertise & Sponsor</a>.</p></div>
 <form class="sm card" data-subject="Creator submission" data-thanks="Submitted! Our editors review every entry within 7 days.">
  <div class="row">{field("name","Your name",ph="Full name")}{field("email","E-mail",type="email",ph="you@email.com")}</div>
  <div class="row">{field("handle","Creator name / handle",ph="@yourhandle")}{field("type","Type of work",opts=["Short film","Feature film","Series / pilot","Web series","Podcast","YouTube / channel","Screenplay","Music video","Other"])}</div>
  {field("title","Title of the work",ph="Title")}
  {field("link","Link to watch / listen",type="url",ph="https://")}
  {field("logline","One-line premise",ph="A retired stunt double takes one last job…")}
  {field("about","Tell us about it",rows=4,req=False,ph="Background, festival history, audience so far, what you're looking for")}
  <label class="check"><input type="checkbox" name="rights" value="yes" required> This is my original work and I hold the rights (or have clearances) to everything in it.</label>
  {CONSENT}{HP}
  <button class="btn btn-primary btn-block" type="submit" data-label="Submit for Spotlight">Submit for Spotlight</button>
  <div class="form-status" role="status"></div>
 </form>
</div></div></section>
{newsletter()}{support_strip()}""")

# ---------------------------------------------------------------- CONTESTS
contests = [
 ("Watch & Win: Fall TV Bingo","$500 cash + 12-month streaming subscription","2026-11-30","Complete the fall bingo card with screenshots of your watchlist and tell us your pick of the season in 100 words. Public vote + editor jury.","Free"),
 ("60-Second Pitch Prize","$1,000 + Creator Spotlight feature","2026-12-15","Pitch a series in a 60-second video. Judged on premise, clarity and the season-two answer. Top 5 get jury feedback.","Free"),
 ("Fan Trailer Remix","Editing gear bundle worth $800","2026-10-31","Re-cut any public-domain or licensed trailer into a new genre. 90 seconds max. Must credit all sources.","Free"),
 ("Best Review of the Month","$150 + byline on SHOW.MEDIA","2026-10-15","Write a 300-word Stream-It-or-Skip-It verdict on any title in our guide. The winner is published, paid, and credited.","Free"),
]
contest_cards = "".join(f'<div class="contest"><div style="display:flex;justify-content:space-between;align-items:center"><span class="badge badge-free">{fee} to enter</span><span class="deadline" data-deadline="{d}T23:59:00Z"></span></div><h3 style="margin:6px 0 0">{t}</h3><div class="prize">🏆 {p}</div><p class="muted small" style="margin:0">{desc}</p><a class="btn btn-primary btn-sm" href="#enter" style="justify-self:start">Enter now</a></div>' for t,p,d,desc,fee in contests)
PAGES["contests.html"] = dict(title="Contests & Prizes — Win Cash, Gear and Subscriptions | SHOW.MEDIA",
 desc="Free-to-enter monthly contests for fans and creators: cash prizes, streaming subscriptions, gear and published bylines.",
 body=f"""
{page_head("Contests & prizes","Win for watching, writing and making","Free to enter. Real prizes. Jury feedback on creative categories. New contests open monthly — subscribe to the Contests list to get in first.","Contests")}
<section class="section" style="padding-top:10px"><div class="wrap">
 <div class="grid g2">{contest_cards}</div>
 <div class="ad ad-infeed" data-slot="infeed" style="margin-top:28px"></div>
 <div class="card" style="margin-top:28px"><b>Brands:</b> <span class="muted">sponsor a contest and we deliver guaranteed entries, opt-in e-mail leads and content rights. </span><a href="advertise.html#contest" style="text-decoration:underline">Sponsor a contest →</a></div>
</div></section>
<section class="section" id="enter"><div class="wrap"><div class="leadgen">
 <div><span class="eyebrow">Enter</span><h2>One form for every contest</h2><p class="muted">Pick the contest, drop your link or text, done. Winners are announced on the site, in the newsletter and by e-mail.</p>
 <ul><li>18+ or with guardian consent; void where prohibited</li><li>One entry per person per contest</li><li>Prizes paid via PayPal or gift card within 30 days of announcement</li><li>Full rules on the <a href="terms.html#contests" style="text-decoration:underline">terms page</a></li></ul></div>
 <form class="sm card" data-subject="Contest entry" data-thanks="Entry received! Good luck — winners are announced by e-mail and on the site.">
  {field("contest","Contest",opts=[c[0] for c in contests])}
  <div class="row">{field("name","Your name",ph="Full name")}{field("email","E-mail",type="email",ph="you@email.com")}</div>
  {field("country","Country",ph="e.g. Canada")}
  {field("entry_link","Link to your entry",type="url",req=False,ph="https:// (video, doc, image)")}
  {field("entry_text","Or paste your text entry",rows=4,req=False,ph="Up to 300 words")}
  <label class="check"><input type="checkbox" name="rules" value="yes" required> I have read the rules and confirm the entry is my own work.</label>
  <label class="check"><input type="checkbox" name="list_contests" value="yes" checked> E-mail me when new contests open.</label>
  {CONSENT}{HP}
  <button class="btn btn-primary btn-block" type="submit" data-label="Submit entry">Submit entry</button>
  <div class="form-status" role="status"></div>
 </form>
</div></div></section>
{newsletter()}""")

# ---------------------------------------------------------------- EVENTS
events = [("OCT","03","Global premiere screening + Q&A","Los Angeles · Regal LA Live","tickets"),("OCT","10","Fan Fest: sci-fi weekend","Toronto · Metro Convention Centre","events"),("OCT","17","Live podcast taping — The Late Rewind","New York · The Bell House","events"),("OCT","24","Horror marathon: 24 hours of frights","Austin · Alamo Drafthouse","tickets"),("NOV","07","Comedy series live tour","Chicago · The Vic","tickets"),("NOV","21","Short film festival — SHOW.MEDIA jury night","Montréal · Cinéma du Parc","events")]
event_cards = "".join(f'<div class="event"><div class="date"><span class="small muted">{m}</span><b>{d}</b></div><div><b>{t}</b><br><span class="muted small">{loc}</span></div><a class="btn btn-ghost btn-sm" data-link="affiliate.{k}" href="#">Tickets →</a></div>' for m,d,t,loc,k in events)
PAGES["events.html"] = dict(title="Live Events — Premieres, Screenings, Fan Fests & Tours | SHOW.MEDIA",
 desc="Premieres, screenings, fan conventions, live podcast tapings and tours. Find events near you and get tickets.",
 body=f"""
{page_head("Live events","Premieres, screenings & tours","Because some shows are better with a crowd. Tickets via our partners; list your own event for free.","Events")}
<div class="wrap"><div class="ad ad-leader" data-slot="leaderboard"></div></div>
<section class="section" style="padding-top:10px"><div class="wrap">
 <div class="filters"><span class="chip on">All</span><span class="chip">This week</span><span class="chip">This month</span><span class="chip">Premieres</span><span class="chip">Festivals</span><span class="chip">Live podcasts</span><span class="chip">Free</span></div>
 <div class="grid" style="gap:12px">{event_cards}</div>
 <p class="form-note" style="margin-top:12px">Ticket links go to partner ticketing sites; we may earn a commission.</p>
</div></section>
<section class="section"><div class="wrap"><div class="leadgen">
 <div><span class="eyebrow">Organisers</span><h2>List your event free</h2><p class="muted">Premieres, screenings, meetups, festivals. Listings are free; featured placements and newsletter pushes are available for organisers who want reach.</p></div>
 <form class="sm card" data-subject="Event listing" data-thanks="Thanks — we'll review and publish your listing within 3 business days.">
  <div class="row">{field("name","Contact name",ph="Full name")}{field("email","E-mail",type="email",ph="you@email.com")}</div>
  {field("event","Event name",ph="Event title")}
  <div class="row">{field("date","Date",type="date")}{field("city","City & venue",ph="City · Venue")}</div>
  {field("link","Ticket / info link",type="url",ph="https://")}
  {field("details","Details",rows=3,req=False,ph="What, who, price")}
  {CONSENT}{HP}
  <button class="btn btn-primary btn-block" type="submit" data-label="Submit event">Submit event</button>
  <div class="form-status" role="status"></div>
 </form>
</div></div></section>
{newsletter()}""")

# ---------------------------------------------------------------- SUPPORT
PAGES["support.html"] = dict(title="Support SHOW.MEDIA — Keep It Independent and Free | SHOW.MEDIA",
 desc="Support an independent streaming guide: one-time tips, monthly membership, sponsorships. Funds go to hosting, contest prizes, creator payments and hiring.",
 body=f"""
{page_head("Support","Keep SHOW.MEDIA free, independent and growing","No paywall, no pay-to-play scores. Reader support funds hosting, contest prize pools, paid creator features and the writers we hire next.","Support")}
<section class="section" style="padding-top:10px"><div class="wrap">
 <div class="card" style="margin-bottom:28px"><div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px"><b id="goal-text">Monthly operating goal</b><span class="muted small">Updated monthly</span></div><div class="goal"><i id="goal-bar"></i></div><div class="muted small">Where it goes: 40% contest prizes & creator payments · 30% writers & editors · 20% hosting, tools & data · 10% promotion</div></div>
 <div class="tiers">
  <div class="tier"><span class="eyebrow">One-time</span><div class="price">$5+</div><p class="muted small">Buy the editors a coffee. Every tip is listed on our supporter wall (first name only, if you want).</p><a class="btn btn-accent btn-block" data-link="support.kofi" href="#">☕ Tip on Ko-fi</a><a class="btn btn-ghost btn-block" style="margin-top:8px" data-link="support.buymeacoffee" href="#">Buy Me a Coffee</a></div>
  <div class="tier featured"><span class="eyebrow">Monthly · most popular</span><div class="price">$5<span class="small muted">/mo</span></div><p class="muted small">Member badge, ad-light newsletter edition, vote on which contests we run next, early access to spotlights.</p><a class="btn btn-primary btn-block" data-link="support.kofi" href="#">Become a member</a></div>
  <div class="tier"><span class="eyebrow">Patron</span><div class="price">$25<span class="small muted">/mo</span></div><p class="muted small">Everything in Member, plus your name (or brand) in the monthly thank-you post and a yearly shout-out on the channel.</p><a class="btn btn-ghost btn-block" data-link="support.githubSponsors" href="#">Sponsor monthly</a><a class="btn btn-ghost btn-block" style="margin-top:8px" data-link="support.paypal" href="#">Give via PayPal</a></div>
 </div>
 <div class="grid g2" style="margin-top:32px">
  <div class="card"><h3>Other ways to help</h3><ul class="muted" style="padding-left:18px"><li>Use our <a href="watch.html" style="text-decoration:underline">streaming links</a> when you subscribe — affiliate commissions cost you nothing.</li><li>Share a verdict you agree (or disagree) with.</li><li>Submit your work to the <a href="creators.html" style="text-decoration:underline">Creator Spotlight</a>.</li><li>Brands: <a href="advertise.html" style="text-decoration:underline">sponsor a contest or a section</a>.</li></ul></div>
  <div class="card"><h3>Recent supporters</h3><ul class="support-feed"><li><span>Be the first on the wall</span><span class="muted">—</span></li></ul><p class="form-note" style="margin-top:10px">Supporters are listed with their consent. Supporting the site does not influence editorial coverage or scores.</p></div>
 </div>
</div></section>
{newsletter()}""")

# ---------------------------------------------------------------- ADVERTISE / SPONSOR / PARTNER (lead-gen page)
PAGES["advertise.html"] = dict(title="Advertise, Sponsor & Partner with SHOW.MEDIA — Media Kit & Rates",
 desc="Reach streaming-first audiences: display, sponsored verdicts, newsletter takeovers, branded contests, creator collaborations, domain and equity partnerships.",
 body=f"""
{page_head("Advertise · Sponsor · Partner","Put your title, product or brand in front of people deciding what to watch","Direct, no agency mark-up. Packages from $250. Reporting on every campaign. Reply within 2 business days.","Advertise")}
<section class="section" style="padding-top:10px"><div class="wrap">
 <div class="grid g3">
  <div class="card"><span class="eyebrow">Display</span><h3>Site & newsletter ads</h3><p class="muted small">Leaderboard, sidebar, in-feed and newsletter units. Programmatic via Google plus direct-sold takeovers.</p><b>From $250 / week</b></div>
  <div class="card"><span class="eyebrow">Sponsored content</span><h3>“Presented by” verdicts & guides</h3><p class="muted small">Your title or product inside a labelled editorial feature, homepage rail and social push.</p><b>From $750</b></div>
  <div class="card" id="contest"><span class="eyebrow">Contests</span><h3>Branded contest & giveaway</h3><p class="muted small">We build, run and promote it. You get guaranteed entries, opt-in leads and UGC rights.</p><b>From $1,500 + prize</b></div>
  <div class="card"><span class="eyebrow">Creators</span><h3>Creator collaborations</h3><p class="muted small">Match your campaign with spotlight creators for video, podcast or social activations.</p><b>Custom</b></div>
  <div class="card"><span class="eyebrow">Events</span><h3>Premiere & event coverage</h3><p class="muted small">Featured listings, live coverage, newsletter push and ticket-link placement.</p><b>From $400</b></div>
  <div class="card" id="partner"><span class="eyebrow">Partnerships</span><h3>Domain, website & equity</h3><p class="muted small">Interested in this domain, the site itself, a revenue share or a joint venture? Use the form — or the contact link at the top of every page.</p><b>Let's talk</b></div>
 </div>
 <div class="card" id="media-kit" style="margin-top:28px;display:grid;grid-template-columns:1fr auto;gap:16px;align-items:center"><div><b>Media kit</b><br><span class="muted small">Audience profile, placements, specs and rate card. Request it via the form and we send the current PDF.</span></div><a class="btn btn-ghost btn-sm" href="#work-with-us">Request media kit</a></div>
 <div class="stat-row" style="margin-top:28px"><div class="stat"><b>Streaming-first</b><span class="muted small">audience intent</span></div><div class="stat"><b>Tier-1</b><span class="muted small">US · CA · UK · AU focus</span></div><div class="stat"><b>Labelled</b><span class="muted small">every sponsored unit</span></div><div class="stat"><b>48h</b><span class="muted small">proposal turnaround</span></div></div>
</div></section>
{leadgen()}
<section class="section" style="padding-top:0"><div class="wrap"><h2>FAQ</h2>
<details><summary>Do sponsored placements affect the Show Score or verdicts?</summary><p class="muted">Never. Sponsored units are labelled and scores are computed independently. See the <a href="editorial-policy.html">editorial policy</a>.</p></details>
<details><summary>Can we buy the domain or the whole site?</summary><p class="muted">Inquiries are welcome — select “Buying or leasing this domain / website” in the form, or use the contact link in the top banner.</p></details>
<details><summary>What formats do you accept?</summary><p class="muted">Standard IAB display sizes, 16:9 video (YouTube-hosted), newsletter 600px-wide creatives, and any assets needed for a branded contest.</p></details>
<details><summary>How is reporting delivered?</summary><p class="muted">Impressions, clicks, entries and opt-ins in a shared dashboard plus a wrap-up report within 7 days of the campaign end.</p></details>
</div></section>""")

# ---------------------------------------------------------------- CAREERS
roles = [("Streaming Editor (contract)","Remote · Part-time","Own the weekly guide and Friday newsletter."),("Video Editor / Motion","Remote · Freelance","Cut weekly roundups and trailer-reaction shorts."),("Creator Relations Lead","Remote · Part-time","Run the Spotlight pipeline and contests."),("Sponsorship Sales (commission)","Remote · Flexible","Sell packages from the rate card; 20–30% commission."),("Contributing Writers","Remote · Per piece","Paid per published verdict or guide.")]
role_rows = "".join(f'<tr><td><b>{r}</b></td><td>{l}</td><td class="muted">{d}</td><td><a class="btn btn-ghost btn-sm" href="#apply">Apply</a></td></tr>' for r,l,d in roles)
PAGES["careers.html"] = dict(title="Careers & Talent — Write, Edit, Create and Sell with SHOW.MEDIA",
 desc="Open roles and a rolling talent pool for writers, video editors, creators, community managers and sponsorship sales.",
 body=f"""
{page_head("Careers & talent","Help build the guide fans actually use","Remote-first, paid work for writers, editors, video makers and sellers. Don't see your role? Join the talent pool — we hire from it first.","Careers")}
<section class="section" style="padding-top:10px"><div class="wrap"><div class="card" style="overflow:auto"><table><tr><th>Role</th><th>Type</th><th>Summary</th><th></th></tr>{role_rows}</table></div></div></section>
<section class="section" id="apply"><div class="wrap"><div class="leadgen">
 <div><span class="eyebrow">Apply / talent pool</span><h2>Tell us what you're great at</h2><p class="muted">One form for every role. Attach links, not files — a portfolio, a channel, a clip, a published piece.</p>
 <ul><li>Fully remote; async-first</li><li>Paid trials, never free “test” work</li><li>Creators and freelancers welcome</li></ul></div>
 <form class="sm card" data-subject="Job application" data-thanks="Application received. We reply to every applicant within 10 business days.">
  <div class="row">{field("name","Your name",ph="Full name")}{field("email","E-mail",type="email",ph="you@email.com")}</div>
  {field("role","Role",opts=[r[0] for r in roles]+["Talent pool — other"])}
  <div class="row">{field("location","Location / time zone",ph="City, TZ")}{field("rate","Expected rate",req=False,ph="Per hour / per piece")}</div>
  {field("portfolio","Portfolio / links",type="url",ph="https://")}
  {field("pitch","Why you? (150 words max)",rows=4,ph="What you've made, what you'd do here first")}
  {CONSENT}{HP}
  <button class="btn btn-primary btn-block" type="submit" data-label="Send application">Send application</button>
  <div class="form-status" role="status"></div>
 </form>
</div></div></section>""")

# ---------------------------------------------------------------- NEWSLETTER, CONTACT, ABOUT
PAGES["newsletter.html"] = dict(title="Newsletter — Watch This Weekend, New This Week, Contests | SHOW.MEDIA", desc="Free weekly newsletter: three picks every Friday, everything new on every service, contests and creator spotlights.",
 body=f"""{page_head("Newsletter","Let us do the scrolling","Four lists, one e-mail address, zero spam. Choose what you want below.","Newsletter")}{newsletter()}
<section class="section" style="padding-top:0"><div class="wrap"><div class="grid g4"><div class="card"><h3>Watch This Weekend</h3><p class="muted small">Every Friday. Three picks, one sentence each, where to watch.</p></div><div class="card"><h3>New This Week</h3><p class="muted small">Every Monday. Everything landing on every service, sorted by score.</p></div><div class="card"><h3>Contests & Prizes</h3><p class="muted small">When a contest opens or closes. First access to entries.</p></div><div class="card"><h3>Creator Spotlight</h3><p class="muted small">New featured creators, casting and collaboration calls.</p></div></div></div></section>""")

PAGES["contact.html"] = dict(title="Contact SHOW.MEDIA", desc="Contact SHOW.MEDIA for editorial tips, corrections, advertising, partnerships, domain inquiries and support.",
 body=f"""{page_head("Contact","Get in touch","Tips, corrections, press, advertising, partnerships or the domain itself — one form reaches the right desk.","Contact")}
<section class="section" style="padding-top:10px"><div class="wrap"><div class="leadgen">
 <div><h2>Fastest routes</h2><ul><li><b>Sponsorship, advertising, partnership, domain or website inquiries:</b> use the <a data-owner-contact href="https://web.works/contact" style="text-decoration:underline">web.works/contact</a> link at the top of every page, or the form here.</li><li><b>Creators:</b> <a href="creators.html#submit" style="text-decoration:underline">submit via Spotlight</a>.</li><li><b>Contests:</b> <a href="contests.html#enter" style="text-decoration:underline">entry form</a>.</li><li><b>Jobs:</b> <a href="careers.html#apply" style="text-decoration:underline">careers page</a>.</li><li><b>Prefer e-mail?</b> <a data-contact data-subject="Inquiry via SHOW.MEDIA contact page" href="#" style="text-decoration:underline">Click here to open your mail app</a>.</li></ul></div>
 <form class="sm card" data-subject="Contact form" data-thanks="Message sent — we reply within 2 business days.">
  <div class="row">{field("name","Your name",ph="Full name")}{field("email","E-mail",type="email",ph="you@email.com")}</div>
  {field("topic","Topic",opts=["Advertising / sponsorship","Partnership / domain / website inquiry","Editorial tip or correction","Press","Creator / contest question","Support / donation","Other"])}
  {field("message","Message",rows=5,ph="How can we help?")}
  {CONSENT}{HP}
  <button class="btn btn-primary btn-block" type="submit" data-label="Send message">Send message</button>
  <div class="form-status" role="status"></div>
 </form>
</div></div></section>""")

PAGES["about.html"] = dict(title="About SHOW.MEDIA", desc="SHOW.MEDIA is an independent streaming and entertainment guide: what to watch, where to watch it, and who's making it.",
 body=f"""{page_head("About","An independent guide to what's worth watching","SHOW.MEDIA exists because deciding what to watch shouldn't take longer than watching it.","About")}
<section class="section" style="padding-top:10px"><div class="wrap"><div class="prose">
<p>We track eight streaming services, score every title with a transparent formula, and tell you plainly whether to stream it or skip it. Alongside the guide we run a free Creator Spotlight for independent makers, monthly contests with real prizes, and a live-events calendar.</p>
<h2>How we make money</h2><p>Advertising (including Google AdSense), affiliate commissions on streaming and ticket links, sponsored placements that are always labelled, and direct reader support. None of these influence the Show Score or our verdicts — see the <a href="editorial-policy.html">editorial policy</a>.</p>
<h2>Where the money goes</h2><p>Hosting and data, contest prize pools, paid creator features, the writers and editors we hire, and promotion. Our <a href="support.html">support page</a> shows the monthly goal.</p>
<h2>Who we are</h2><p>SHOW.MEDIA is published independently under the domain name show.media by Webworks Media Network. We are not affiliated with any company trading as “Show Media” or with any streaming service, studio or network. <a href="disclaimer.html">Full disclosure</a>.</p>
<h2>Work with us</h2><p><a href="advertise.html">Advertise or sponsor</a> · <a href="careers.html">Careers</a> · <a href="contact.html">Contact</a></p>
</div></div></section>{newsletter()}""")

# ---------------------------------------------------------------- LEGAL
def legal(slug,title,desc,html):
    PAGES[slug]=dict(title=f"{title} | SHOW.MEDIA",desc=desc,body=f"""{page_head("Legal",title,desc,title)}<section class="section" style="padding-top:10px"><div class="wrap"><div class="prose">{html}<p class="faint small">Last updated {TODAY}.</p></div></div></section>""")

legal("disclaimer.html","Disclaimer & trademark disclosure","Trademark, copyright, affiliate and advertising disclosures for SHOW.MEDIA.",f"""
<h2>Trademark disclosure</h2>
<p>“SHOW.MEDIA” is used on this site solely as the domain name <b>show.media</b> and as the stylised name of this independent online publication. The publication does not claim exclusive rights in the words “show media” and is <b>not affiliated with, endorsed by, sponsored by or connected to</b> any other business, product or service operating under a “Show Media” name, including but not limited to Show Media LLC (an out-of-home advertising company in Las Vegas, Nevada, USA), Show Media Limited (United Kingdom), or any registrant of SHOW MEDIA trademarks in any jurisdiction. This site does not offer out-of-home, taxi-top, vehicle-wrap or billboard advertising services.</p>
<p>Netflix, Prime Video, Disney+, HBO Max, Apple TV+, Hulu, Peacock, Paramount+, YouTube and all show, film, studio and network names, titles and logos referenced on this site are trademarks of their respective owners. They are used only to identify the works and services being discussed (nominative fair use) and for commentary, criticism and news reporting. No endorsement is implied.</p>
<h2>Copyright</h2>
<p>Original text, the Show Score methodology, site design and code are © SHOW.MEDIA / Webworks Media Network. Trailers and videos are embedded from the rights holders' official channels using their public embed players and are not hosted here. Poster-style artwork on this site is generated by us and does not reproduce official key art. If you believe content on this site infringes your rights, see the <a href="dmca.html">DMCA / takedown page</a>.</p>
<h2>Advertising & affiliate disclosure</h2>
<p>This site displays advertising, including through Google AdSense, and participates in affiliate programmes; links to streaming services, ticketing platforms and retailers may earn us a commission at no cost to you. Sponsored content is labelled “Sponsored” or “Presented by”. Advertising and sponsorship never influence editorial scores or verdicts.</p>
<h2>General</h2>
<p>Availability, prices and release dates change; we update daily but cannot guarantee accuracy at any moment. Contests are subject to the rules on the <a href="terms.html#contests">terms page</a>. Nothing on this site is legal or financial advice.</p>""")

legal("privacy.html","Privacy policy","How SHOW.MEDIA collects, uses and protects your data.","""
<h2>What we collect</h2><p>Information you submit through forms (name, e-mail, company, message, contest entry). Standard analytics and advertising data (IP address, device, pages viewed) collected via cookies by our analytics and advertising partners, including Google.</p>
<h2>How we use it</h2><p>To reply to inquiries, run contests, send newsletters you opted into, operate advertising and improve the site. We do not sell personal data.</p>
<h2>Advertising (Google AdSense)</h2><p>Third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You may opt out of personalised advertising at <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a> or <a href="https://www.aboutads.info" rel="noopener" target="_blank">aboutads.info</a>. Embedded YouTube players use the privacy-enhanced (youtube-nocookie) mode.</p>
<h2>Form processing</h2><p>Form submissions are transmitted via a third-party form-relay service to our inbox and are retained only as long as needed to handle the inquiry, contest or application.</p>
<h2>Your rights</h2><p>You can request access to, correction or deletion of your data, or withdraw newsletter consent at any time, via the <a href="contact.html">contact page</a>. EU/UK residents have rights under GDPR; California residents under CCPA/CPRA (we do not “sell” or “share” personal information for cross-context behavioural advertising beyond the cookie-based ad serving described above, which you can opt out of via the links above).</p>
<h2>Children</h2><p>This site is not directed at children under 13 and we do not knowingly collect their data.</p>""")

legal("terms.html","Terms of use","Terms governing use of SHOW.MEDIA, contests and submissions.","""
<h2>Use of the site</h2><p>By using SHOW.MEDIA you agree to these terms. Content is provided for information and entertainment; scores and verdicts are opinions. Do not scrape, republish or misrepresent our content.</p>
<h2 id="contests">Contest rules</h2><p>No purchase necessary. Open to entrants 18+ (or with guardian consent) where legal; void where prohibited. One entry per person per contest unless stated. Entries must be original and non-infringing. Winners are chosen by public vote and/or editorial jury as stated on each contest, notified by e-mail, and must respond within 14 days. Prizes are paid via PayPal or gift card within 30 days; cash equivalents may be substituted. By entering you grant SHOW.MEDIA a non-exclusive licence to display your entry with credit. Sponsors of a contest may receive opt-in entrant e-mails only where the entrant has ticked the relevant box.</p>
<h2>Creator submissions</h2><p>You retain all rights to submitted work and grant us a non-exclusive licence to feature, excerpt and link to it with credit. You warrant you have all necessary clearances.</p>
<h2>Support & donations</h2><p>Tips, memberships and donations are voluntary, non-refundable, and are not payments for goods or services; they do not purchase editorial influence.</p>
<h2>Liability</h2><p>The site is provided “as is”. To the fullest extent permitted by law we exclude liability for losses arising from use of the site or reliance on its content. Third-party sites linked from here have their own terms.</p>""")

legal("cookies.html","Cookie policy","Cookies used by SHOW.MEDIA and how to control them.","""
<p>We use: (1) <b>essential</b> local storage for your theme choice and to remember you dismissed notices; (2) <b>analytics</b> cookies to understand traffic; (3) <b>advertising</b> cookies set by Google and its partners to serve and measure ads. You can block cookies in your browser and opt out of personalised ads via <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a>. EU/UK visitors are shown a consent notice.</p>""")

legal("dmca.html","DMCA / copyright takedown","How to report copyright infringement on SHOW.MEDIA.","""
<p>We respect intellectual-property rights. If you believe material on this site infringes your copyright, send a notice via the <a href="contact.html">contact page</a> (topic: “Editorial tip or correction”) including: your contact details; identification of the work; the URL on our site; a statement of good-faith belief; a statement under penalty of perjury that you are authorised; and your signature. We act on valid notices promptly. Embedded videos are hosted by YouTube and should be reported to YouTube as well.</p>""")

legal("editorial-policy.html","Editorial policy","Independence, corrections, AI use and sponsorship labelling at SHOW.MEDIA.","""
<h2>Independence</h2><p>Scores and verdicts are never for sale. Advertisers and sponsors have no input into editorial decisions. Sponsored units are labelled.</p>
<h2>Corrections</h2><p>We correct errors quickly and note material corrections on the page. Report one via the <a href="contact.html">contact page</a>.</p>
<h2>AI</h2><p>We may use AI tools for research and data processing. Published verdicts are reviewed by a human editor.</p>
<h2>Affiliate links</h2><p>Where-to-watch and ticket links may be affiliate links. They do not affect what we recommend.</p>""")

PAGES["sitemap.html"] = dict(title="Sitemap | SHOW.MEDIA", desc="All pages on SHOW.MEDIA.", body="""<section class="section"><div class="wrap"><h1>Sitemap</h1><div class="grid g3" id="sitemap-list">"""+"".join(f'<a href="{p}">{p.replace(".html","").replace("-"," ").title()}</a>' for p in sorted(list(PAGES.keys())+["disclaimer.html","privacy.html","terms.html","cookies.html","dmca.html","editorial-policy.html","sitemap.html"]) if p!="show.html")+"""</div></div></section>""")

PAGES["404.html"] = dict(title="Page not found | SHOW.MEDIA", desc="That page isn't here.", body="""<section class="hero"><div class="wrap" style="text-align:center"><h1>404 — <span>that show got cancelled</span></h1><p class="lead" style="margin:0 auto">The page you're looking for isn't here. Try the guide instead.</p><div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-ghost" href="watch.html">What to Watch</a></div></div></section>""")

# ---------------------------------------------------------------- write
for slug,p in PAGES.items():
    with open(os.path.join(ROOT,slug),"w") as f:
        f.write(shell(p["title"],p["desc"],p["body"],"" if slug=="index.html" else slug,schema=p.get("schema")))
# sitemap.xml / robots / CNAME / manifest / ads.txt / .nojekyll
urls="".join(f"<url><loc>{DOMAIN}{'' if s=='index.html' else s}</loc><lastmod>{TODAY}</lastmod></url>" for s in PAGES if s not in("404.html","show.html"))
open(os.path.join(ROOT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}sitemap.xml\n")
open(os.path.join(ROOT,"CNAME"),"w").write("show.media\n")
open(os.path.join(ROOT,".nojekyll"),"w").write("")
open(os.path.join(ROOT,"ads.txt"),"w").write("# Replace with the line from your AdSense account after approval:\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
open(os.path.join(ROOT,"manifest.webmanifest"),"w").write(json.dumps({"name":"SHOW.MEDIA","short_name":"SHOW.MEDIA","start_url":"./index.html","display":"standalone","background_color":"#0b0d12","theme_color":"#0b0d12","icons":[{"src":"assets/img/favicon.svg","sizes":"any","type":"image/svg+xml"}]}))
print("built",len(PAGES),"pages")
