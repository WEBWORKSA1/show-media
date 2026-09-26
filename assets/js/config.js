/* ============================================================
   SHOW.MEDIA — single site configuration
   Everything an operator needs to change lives here.
   ============================================================ */
window.SM_CONFIG = {
  siteName: "SHOW.MEDIA",
  domain: "show.media",
  tagline: "What to watch. Where to watch it. Who's making it.",

  // --- Contact routing (the only inbox for the whole site). ---
  // Stored obfuscated (base64 of rot13). Never write the plain address anywhere else.
  contactKey: "jroj" + "bexfn1@tznvy.pbz",
  // Form backend: FormSubmit (free, no server). First submission triggers a one-time
  // activation e-mail to the inbox above; click it once and all forms go live.
  formEndpoint: "https://formsubmit.co/ajax/",

  // --- External inquiry link shown in the top banner on every page ---
  ownerContactUrl: "https://web.works/contact",

  // --- Monetization ---
  adsense: {
    enabled: false,               // set true after AdSense approval
    client: "ca-pub-0000000000000000",
    slots: { leaderboard: "0000000001", sidebar: "0000000002", infeed: "0000000003", anchor: "0000000004" }
  },
  affiliate: {
    // Replace with your own tracking links (Impact / CJ / Amazon Associates / Ticketmaster / Eventbrite)
    netflix: "https://www.netflix.com/",
    prime: "https://www.amazon.com/gp/video/storefront",
    disney: "https://www.disneyplus.com/",
    max: "https://www.max.com/",
    apple: "https://tv.apple.com/",
    paramount: "https://www.paramountplus.com/",
    peacock: "https://www.peacocktv.com/",
    hulu: "https://www.hulu.com/",
    tickets: "https://www.ticketmaster.com/",
    events: "https://www.eventbrite.com/"
  },

  // --- Video (YouTube uploads playlists / video IDs). Swap for your own channel. ---
  youtube: {
    channelUrl: "https://www.youtube.com/@showmedia",
    playlists: [
      { id: "UUWOA1ZGywLbqmigxE4Qlvuw", title: "Latest Netflix trailers" },
      { id: "UUi8e0iOVk1fEOogdfu4YgfA", title: "Movie trailers this week" },
      { id: "UUQJWtTnAHhEG5w4uN0udnUQ", title: "Prime Video previews" }
    ]
  },

  // --- Support / donations (all static-friendly) ---
  support: {
    kofi: "https://ko-fi.com/showmedia",
    buymeacoffee: "https://buymeacoffee.com/showmedia",
    paypal: "https://www.paypal.com/donate",
    githubSponsors: "https://github.com/sponsors/webworksa1",
    goalLabel: "Monthly operating goal",
    goalAmount: 1500,
    goalRaised: 0
  },

  // --- Social ---
  social: {
    youtube: "https://www.youtube.com/@showmedia",
    x: "https://x.com/showmedia",
    instagram: "https://www.instagram.com/showmedia",
    tiktok: "https://www.tiktok.com/@showmedia",
    facebook: "https://www.facebook.com/showmedia"
  }
};
