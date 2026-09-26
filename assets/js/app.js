/* SHOW.MEDIA — site runtime (no build step, no backend) */
(function () {
  const C = window.SM_CONFIG;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  /* ---------- contact address: never in the DOM as text ---------- */
  const rot13 = s => s.replace(/[a-zA-Z]/g, c => String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26));
  const contact = () => rot13(C.contactKey);
  // Any element with data-contact becomes a click-to-mail link, address resolved only on click.
  $$("[data-contact]").forEach(el => {
    el.setAttribute("href", "#contact");
    el.addEventListener("click", e => { e.preventDefault(); location.href = "mailto:" + contact() + "?subject=" + encodeURIComponent(el.dataset.subject || "Inquiry via SHOW.MEDIA"); });
  });

  /* ---------- theme ---------- */
  const root = document.documentElement;
  try { const t = localStorage.getItem("sm-theme"); if (t) root.setAttribute("data-theme", t); } catch (e) {}
  $$("[data-theme-toggle]").forEach(b => b.addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("sm-theme", next); } catch (e) {}
  }));

  /* ---------- mobile drawer ---------- */
  const drawer = $("#drawer");
  $$("[data-drawer]").forEach(b => b.addEventListener("click", () => drawer.classList.toggle("open")));

  /* ---------- active nav ---------- */
  const here = location.pathname.split("/").pop() || "index.html";
  $$(".menu a, #drawer a").forEach(a => { if (a.getAttribute("href") === here) a.classList.add("active"); });

  /* ---------- external links in config ---------- */
  $$("[data-link]").forEach(a => {
    const [grp, key] = a.dataset.link.split(".");
    const url = key ? (C[grp] || {})[key] : C[grp];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener sponsored"; }
  });
  $$("[data-owner-contact]").forEach(a => { a.href = C.ownerContactUrl; a.target = "_blank"; a.rel = "noopener"; });

  /* ---------- ads ---------- */
  const ads = C.adsense;
  $$(".ad").forEach(el => {
    if (ads.enabled) {
      const ins = document.createElement("ins");
      ins.className = "adsbygoogle"; ins.style.display = "block";
      ins.dataset.adClient = ads.client; ins.dataset.adSlot = ads.slots[el.dataset.slot] || ads.slots.infeed;
      ins.dataset.adFormat = "auto"; ins.dataset.fullWidthResponsive = "true";
      el.textContent = ""; el.appendChild(ins);
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    } else { el.textContent = "Advertisement"; }
  });
  if (ads.enabled) {
    const s = document.createElement("script"); s.async = true; s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + ads.client; document.head.appendChild(s);
  }
  const anchor = $(".ad-anchor"); if (anchor) anchor.classList.add("on");

  /* ---------- cookie notice ---------- */
  const ck = $("#cookie");
  try { if (ck && !localStorage.getItem("sm-cookie")) ck.classList.add("on"); } catch (e) { if (ck) ck.classList.add("on"); }
  $("#cookie-ok") && $("#cookie-ok").addEventListener("click", () => { ck.classList.remove("on"); try { localStorage.setItem("sm-cookie", "1"); } catch (e) {} });

  /* ---------- toast ---------- */
  const toast = msg => { const t = $("#toast"); if (!t) return; t.textContent = msg; t.classList.add("on"); setTimeout(() => t.classList.remove("on"), 2600); };

  /* ---------- forms (FormSubmit AJAX, honeypot, multi-step) ---------- */
  $$("form.sm").forEach(f => {
    const steps = $$(".step", f), bars = $$(".steps span", f);
    let i = 0;
    const show = n => { steps.forEach((s, k) => s.classList.toggle("on", k === n)); bars.forEach((b, k) => b.classList.toggle("on", k <= n)); };
    if (steps.length) show(0);
    $$("[data-next]", f).forEach(b => b.addEventListener("click", () => {
      const req = $$("[required]", steps[i]); if (!req.every(x => x.reportValidity())) return; i = Math.min(i + 1, steps.length - 1); show(i);
    }));
    $$("[data-prev]", f).forEach(b => b.addEventListener("click", () => { i = Math.max(i - 1, 0); show(i); }));
    f.addEventListener("submit", async e => {
      e.preventDefault();
      if ($(".hp input", f) && $(".hp input", f).value) return;
      const st = $(".form-status", f), btn = $("[type=submit]", f);
      btn.disabled = true; btn.textContent = "Sending…";
      const data = Object.fromEntries(new FormData(f).entries());
      data._subject = "[SHOW.MEDIA] " + (f.dataset.subject || "Form submission");
      data._template = "table"; data._captcha = "false"; data.page = location.href;
      try {
        const r = await fetch(C.formEndpoint + contact(), { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) });
        if (!r.ok) throw new Error(r.status);
        st.className = "form-status ok"; st.textContent = f.dataset.thanks || "Thanks — we received it and will reply within 2 business days.";
        f.reset(); if (steps.length) { i = 0; show(0); }
        try { localStorage.setItem("sm-lead", "1"); } catch (x) {}
      } catch (err) {
        st.className = "form-status err"; st.textContent = "Could not send right now. Please try again or use the contact link at the top of the page.";
      }
      btn.disabled = false; btn.textContent = btn.dataset.label || "Send";
    });
  });

  /* ---------- support goal ---------- */
  const goal = $("#goal-bar");
  if (goal) { const pct = Math.min(100, Math.round(100 * C.support.goalRaised / C.support.goalAmount)); setTimeout(() => goal.style.width = pct + "%", 200); $("#goal-text").textContent = "$" + C.support.goalRaised.toLocaleString() + " of $" + C.support.goalAmount.toLocaleString() + " · " + C.support.goalLabel; }

  /* ---------- YouTube playlists ---------- */
  $$("[data-yt-playlists]").forEach(host => {
    C.youtube.playlists.forEach(p => {
      const d = document.createElement("div"); d.className = "card";
      d.innerHTML = `<div class="video"><iframe loading="lazy" src="https://www.youtube-nocookie.com/embed/videoseries?list=${p.id}" title="${p.title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div><h3 style="margin-top:14px">${p.title}</h3>`;
      host.appendChild(d);
    });
  });

  /* ---------- shows catalogue ---------- */
  const PLAT = { netflix: ["Netflix", "#e50914"], prime: ["Prime Video", "#00a8e1"], disney: ["Disney+", "#1f80e0"], max: ["HBO Max", "#8a2be2"], apple: ["Apple TV+", "#a5a5a5"], hulu: ["Hulu", "#1ce783"], peacock: ["Peacock", "#ffcc4d"], paramount: ["Paramount+", "#0064ff"] };
  window.SM_PLAT = PLAT;
  const posterArt = s => `linear-gradient(160deg,hsl(${s.hue} 80% 55%),hsl(${(s.hue + 40) % 360} 70% 25%) 70%,#0b0d12)`;
  const posterCard = (s, rank) => `<a class="poster" href="show.html?id=${s.id}">
      <div class="art" style="background:${posterArt(s)}">${s.title}</div>
      ${rank ? `<span class="rank">#${rank}</span>` : ""}
      ${s.trend > 2 ? `<span class="tag badge badge-hot">Rising</span>` : ""}
      <div class="meta"><span>${PLAT[s.platform][0]} · ${s.year}</span><span class="score">${s.score}</span></div></a>`;
  window.SM_posterCard = posterCard; window.SM_posterArt = posterArt;

  const needShows = $("[data-rail]") || $("[data-catalogue]") || $("[data-show-page]") || $("#site-search");
  if (needShows) {
    fetch("assets/data/shows.json").then(r => r.json()).then(shows => {
      window.SM_SHOWS = shows;
      $$("[data-rail]").forEach(el => {
        const kind = el.dataset.rail; let list = shows.slice();
        if (kind === "trending") list.sort((a, b) => (b.score + b.trend * 2) - (a.score + a.trend * 2));
        if (kind === "new") list = list.filter(s => s.year >= 2024).sort((a, b) => b.year - a.year);
        if (kind === "movies") list = list.filter(s => s.type === "Movie").sort((a, b) => b.score - a.score);
        if (kind === "top") list.sort((a, b) => b.score - a.score);
        if (PLAT[kind]) list = list.filter(s => s.platform === kind).sort((a, b) => b.score - a.score);
        el.innerHTML = list.slice(0, +el.dataset.limit || 10).map((s, i) => posterCard(s, kind === "trending" || kind === "top" ? i + 1 : 0)).join("");
      });
      const cat = $("[data-catalogue]");
      if (cat) {
        const state = { platform: "all", type: "all", genre: "all", q: "" };
        const render = () => {
          const out = shows.filter(s => (state.platform === "all" || s.platform === state.platform) && (state.type === "all" || s.type === state.type) && (state.genre === "all" || s.genre.includes(state.genre)) && (!state.q || s.title.toLowerCase().includes(state.q))).sort((a, b) => b.score - a.score);
          cat.innerHTML = out.length ? out.map(s => posterCard(s)).join("") : `<p class="muted">Nothing matches — try another filter.</p>`;
          $("#cat-count") && ($("#cat-count").textContent = out.length + " titles");
        };
        const params = new URLSearchParams(location.search); if (params.get("platform")) state.platform = params.get("platform");
        $$("[data-filter]").forEach(ch => {
          const [k, v] = ch.dataset.filter.split(":");
          if (state[k] === v) ch.classList.add("on");
          ch.addEventListener("click", () => { state[k] = v; $$(`[data-filter^="${k}:"]`).forEach(x => x.classList.remove("on")); ch.classList.add("on"); render(); });
        });
        $("#cat-q") && $("#cat-q").addEventListener("input", e => { state.q = e.target.value.toLowerCase(); render(); });
        render();
      }
      const sp = $("[data-show-page]");
      if (sp) {
        const id = new URLSearchParams(location.search).get("id"); const s = shows.find(x => x.id === id) || shows[0];
        document.title = `${s.title} (${s.year}) — Where to watch, review & score | SHOW.MEDIA`;
        const p = PLAT[s.platform];
        sp.innerHTML = `
          <div class="breadcrumb"><a href="index.html">Home</a> › <a href="watch.html">What to Watch</a> › ${s.title}</div>
          <div class="show-head">
            <div class="poster"><div class="art" style="background:${posterArt(s)}">${s.title}</div></div>
            <div>
              <span class="eyebrow">${s.type} · ${s.year} · ${s.rating}${s.seasons ? " · " + s.seasons + " season" + (s.seasons > 1 ? "s" : "") : ""}</span>
              <h1>${s.title}</h1>
              <div style="margin:8px 0 16px">${s.genre.map(g => `<span class="chip">${g}</span>`).join(" ")}</div>
              <div style="margin-bottom:18px"><div class="scorebox"><b>${s.score}</b><span>Show Score</span></div><div class="scorebox"><b style="color:var(--accent)">${s.trend >= 0 ? "▲" : "▼"} ${Math.abs(s.trend)}</b><span>7-day trend</span></div></div>
              <p class="lead">${s.synopsis}</p>
              <div class="jump"><a class="chip" href="#where">Where to watch</a><a class="chip" href="#verdict">Verdict</a><a class="chip" href="#trailer">Trailer</a><a class="chip" href="#similar">More like this</a></div>
            </div>
          </div>
          <div class="ad ad-leader" data-slot="leaderboard"></div>
          <div class="with-side">
            <div>
              <h2 id="where">Where to watch ${s.title}</h2>
              <div class="wtw">
                <a data-link="affiliate.${s.platform}" href="#"><span><i style="display:inline-block;width:10px;height:10px;border-radius:3px;background:${p[1]};margin-right:8px"></i>${p[0]}</span><span class="badge badge-new">Stream</span></a>
                <a data-link="affiliate.prime" href="#"><span>Rent or buy (HD / 4K)</span><span class="muted small">from $3.99</span></a>
              </div>
              <p class="form-note">Availability changes by region. Links may be affiliate links — we may earn a commission at no cost to you.</p>
              <h2 id="verdict">Stream it or skip it?</h2>
              <p><strong>${s.score >= 90 ? "Stream it — tonight." : s.score >= 85 ? "Stream it." : "Stream it if the genre is your thing."}</strong> ${s.title} sits at ${s.score} on the Show Score, which blends critic consensus, audience sentiment and current momentum. ${s.trend > 0 ? "It is climbing this week — a good sign that word of mouth is still building." : "Momentum has cooled, but the catalogue rating holds."}</p>
              <h2 id="trailer">Trailer</h2>
              <div class="card" style="display:flex;gap:16px;align-items:center;flex-wrap:wrap"><div><b>Official trailer for ${s.title}</b><br><span class="muted small">Opens the official trailer search on YouTube (add a video ID in the data file to embed it inline).</span></div><a class="btn btn-primary btn-sm" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=${encodeURIComponent(s.title + " official trailer")}">▶ Watch trailer</a></div>
              <div class="ad ad-infeed" data-slot="infeed" style="margin:24px 0"></div>
              <h2 id="similar">More like this</h2>
              <div class="grid-posters">${shows.filter(x => x.id !== s.id && x.genre.some(g => s.genre.includes(g))).slice(0, 6).map(x => posterCard(x)).join("")}</div>
            </div>
            <aside><div class="ad ad-side" data-slot="sidebar"></div></aside>
          </div>`;
        // re-run hooks for injected content
        $$("[data-link]", sp).forEach(a => { const [g, k] = a.dataset.link.split("."); const u = (C[g] || {})[k]; if (u) { a.href = u; a.target = "_blank"; a.rel = "noopener sponsored"; } });
        $$(".ad", sp).forEach(el => { if (!ads.enabled) el.textContent = "Advertisement"; });
      }
      /* search */
      const si = $("#site-search"), sr = $("#search-results");
      if (si && sr) {
        si.addEventListener("input", () => {
          const q = si.value.trim().toLowerCase();
          if (!q) { sr.classList.remove("open"); return; }
          const hits = shows.filter(s => s.title.toLowerCase().includes(q) || s.genre.join(" ").toLowerCase().includes(q)).slice(0, 6);
          sr.innerHTML = hits.length ? hits.map(s => `<a href="show.html?id=${s.id}"><span style="width:34px;height:50px;border-radius:6px;background:${posterArt(s)}"></span><span><b>${s.title}</b><br><span class="small muted">${s.type} · ${PLAT[s.platform][0]} · ${s.year}</span></span></a>`).join("") : `<div class="muted" style="padding:10px">No titles found for “${q}”. Try <a href="watch.html">browsing the guide</a>.</div>`;
          sr.classList.add("open");
        });
        document.addEventListener("click", e => { if (!sr.contains(e.target) && e.target !== si) sr.classList.remove("open"); });
      }
    });
  }

  /* ---------- countdowns ---------- */
  $$("[data-deadline]").forEach(el => {
    const d = new Date(el.dataset.deadline); const tick = () => { const ms = d - Date.now(); if (ms < 0) { el.textContent = "Closed"; return; } const days = Math.floor(ms / 864e5), h = Math.floor(ms % 864e5 / 36e5); el.textContent = `${days}d ${h}h left`; }; tick(); setInterval(tick, 6e4);
  });

  /* ---------- share ---------- */
  $$("[data-share]").forEach(b => b.addEventListener("click", async () => { try { if (navigator.share) await navigator.share({ title: document.title, url: location.href }); else { await navigator.clipboard.writeText(location.href); toast("Link copied"); } } catch (e) {} }));

  /* ---------- exit-intent newsletter (desktop, once) ---------- */
  let shown = false; try { shown = !!localStorage.getItem("sm-nl"); } catch (e) {}
  const nl = $("#nl-modal");
  if (nl && !shown) document.addEventListener("mouseleave", e => { if (e.clientY < 10 && !shown) { shown = true; nl.classList.add("on"); try { localStorage.setItem("sm-nl", "1"); } catch (x) {} } });
  $("#nl-close") && $("#nl-close").addEventListener("click", () => nl.classList.remove("on"));

  /* ---------- year ---------- */
  $$("[data-year]").forEach(e => e.textContent = new Date().getFullYear());
})();
