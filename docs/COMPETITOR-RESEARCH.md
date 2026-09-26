# SHOW.MEDIA — Competitor Research (36 sites, September 2026)

Method: each site's homepage plus one secondary page (advertise / newsletter / submit / show page) was fetched and torn down for value proposition, navigation, homepage modules, monetisation, lead-gen forms, donation/contest/jobs/partner pages, UX patterns and footer/legal stack. Sites that block fetching (Decider, EW, Ticketmaster, Dailymotion/Roku JS shells, Backstage) were reconstructed from search snippets, help centres and company pages.

## Sites reviewed

| Group | Sites |
|---|---|
| Streaming guides & databases (9) | JustWatch, Reelgood, TV Guide, What's on Netflix, Decider, TV Insider, Metacritic, Rotten Tomatoes, IMDb |
| Entertainment news (9) | Variety, The Hollywood Reporter, Deadline, Entertainment Weekly, Screen Rant, Collider, Den of Geek, TVLine, Playbill |
| Creator / talent / podcast / support (9) | Backstage, FilmFreeway, Short of the Week, No Film School, Podchaser, Listen Notes, Patreon, Buy Me a Coffee, Ko-fi |
| Video / FAST / events (9) | Vimeo, Dailymotion, Tubi, Plex, Roku What's On, Eventbrite, Bandsintown, Ticketmaster Discover, TheWrap |

## Feature matrix → what SHOW.MEDIA shipped

| Pattern (seen on) | Shipped on SHOW.MEDIA |
|---|---|
| Provider-logo filter strip (JustWatch, TV Guide, TVLine) | Hero platform strip + chips on watch.html + ?platform= deep links |
| Owned score badge cross-shown with others (Metacritic, RT, IMDb, JustWatch) | "Show Score" 0–100 + 7-day trend on every title |
| Top-10 with ↑↓ movement, daily refresh (JustWatch, What's on Netflix, IMDb) | Trending rail ranked by score + momentum; "Rising" badge |
| Title page with anchor jump-nav: where to watch / seasons / trailer / similar (RT, JustWatch) | show.html jump chips + affiliate where-to-watch + related |
| Verdict franchise "Stream It or Skip It" (Decider), letter grades (EW) | Verdict block on every show page + news kicker |
| Multi-list newsletter picker in 3 places (TV Guide, TV Insider, THR) | 4-list picker on home, every content page, newsletter.html; exit-intent hook |
| Video rail high on page, embedded official trailers (TV Insider, Den of Geek, IMDb) | Homepage video rail + videos.html playlists (youtube-nocookie) |
| Labelled ad architecture: leaderboard, sticky 300×600, in-feed, mobile anchor (Screen Rant, Den of Geek, TV Guide) | Fixed-height slots, config-driven AdSense injection, zero CLS |
| Affiliate where-to-watch and ticket links (TV Guide, RT, Bandsintown, Eventbrite) | Config-driven affiliate map, rel="sponsored" |
| Advertise page with packages + media kit + inquiry form (TV Insider, Variety, No Film School, Tubi) | advertise.html with 6 packages, rate-card starting prices, media-kit request, FAQ |
| Sponsored screenings / branded events as lead-gen (Collider, Deadline Contenders) | Events page + "Sponsor a contest" package |
| Free-to-submit curated showcase with published criteria (Short of the Week, FilmFreeway badges) | Creator Spotlight with criteria, do-not-accept list, 7-day promise, rights checkbox |
| Contest cards: prize, deadline, fee, rules (FilmFreeway) | Live countdowns, prize, free badge, universal entry form with opt-in |
| Tip jar + tiers + goal bar + supporter feed (Ko-fi, BMC, Patreon) | support.html: 3 tiers, goal bar from config, allocation split, wall |
| Jobs board as utility + revenue (Playbill, Backstage, No Film School) | careers.html role table + talent-pool form |
| Event cards with date block + date chips + ticket CTA (Bandsintown, Eventbrite) | events.html + free organiser listing form |
| Trust footer: editorial/corrections/AI policy, DMCA, cookie/CCPA, non-affiliation (TVLine, What's on Netflix, Plex) | Full legal set + trademark disclosure on every page |
| Search with autocomplete across titles (Eventbrite, IMDb) | Header live search over catalogue |
| Dark theme default, poster grid, freshness timestamps (JustWatch, IMDb, RT) | Dark/light toggle, poster cards, bylines/dates |
| JSON-LD on every page (Ticketmaster MusicEvent, news Article) | WebSite+SearchAction, Article schema |

## Notable gaps across the field (= SHOW.MEDIA's edge)
- None of the 18 media sites has a donation/support layer; contests exist only as event-tied giveaways. SHOW.MEDIA has both, always on.
- Only Playbill and Backstage monetise jobs; SHOW.MEDIA folds hiring into a talent pool that feeds the creator pipeline.
- Trade sites bury "advertise" behind agency contacts; SHOW.MEDIA sells direct with starting prices and a 48h proposal promise.

## AdSense benchmarks used
Entertainment display RPM $8–15 (Tier-1), movies/TV $5–12, celebrity news $3–8; geography dominates (Tier-1 $15–45 vs Tier-3 <$5). Best placements: leaderboard above fold without pushing content, in-content unit after paragraph 2–3, sticky sidebar for viewability, mobile anchor, in-feed native in card grids, ≤4 units per view, reserved heights for CLS.

## Trademark check
"Show Media LLC" (Las Vegas, NV — taxi-top / out-of-home advertising) and "Show Media Limited" (UK) exist. SHOW.MEDIA is positioned as a consumer entertainment publication (different class of services), always styled with the dot, and carries a non-affiliation disclosure in the footer and on /disclaimer.html. It offers no advertising-agency or OOH services.
