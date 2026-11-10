#!/usr/bin/env python3
"""Generates the static Prestia site from the data in this file.

The generated HTML is committed, so GitHub Pages serves the repository root as it is and there is
no build step on the server. To change copy, edit the data below and run:

    python3 -I tools/build.py

All links are relative, so the same files work under https://ankit2305.github.io/Prestia/ (the
preview) and at the root of a custom domain. The one exception is 404.html, which GitHub Pages
serves at any depth: it sets a <base> from its own path before anything else loads.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BRAND = "Prestia"
YEAR = "2026"
UPDATED = "10 November 2026"
EMAIL = "support@prestia.in"
PLAY = "https://play.google.com/store/apps/details?id="
BHAKTI_SITE = "https://bhakti.prestia.in"
SIP_WEB = "https://sip.prestia.in"
FONTS = ("https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600"
         "&family=Geist+Mono:wght@400;500&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap")

# --------------------------------------------------------------------------------------------
# Apps. Every fact here comes from the app's own repository or its live Play listing.
# `live` is True only when the Play listing returns the app (checked 10 November 2026).
# --------------------------------------------------------------------------------------------
APPS = [
    dict(
        slug="bhakti", key="bhakti", name="Bhakti", category="Faith & devotion",
        package="org.ankitkumar.bhajan", live=False, min_android="Android 7.0 and later",
        value="Aartis, bhajans and kathas with Devanagari, transliteration and meaning.",
        long=("Read and listen along in Devanagari, with transliteration and plain-language meaning. "
              "A playlist for each day’s deity, gentle reminders and a simple daily routine help "
              "you keep a calm practice."),
        # (file stem, caption). Real screenshots, light and dark.
        shots=[("home", "Today’s playlist and your daily routine"),
               ("reader", "Devanagari, transliteration and meaning"),
               ("library", "Aartis, bhajans and kathas"),
               ("playlists", "Likes, bookmarks and playlists")],
        card_shot="reader", hero_shots=("home", "reader"),
        features=[
            ("Devanagari text", "Every line in clear Devanagari script, with a text size you can adjust."),
            ("Transliteration and meaning", "Read along in English letters, with a plain-language meaning for each verse."),
            ("Listen or read", "Play a recording, or simply read. Aartis, bhajans and kathas are all in one place."),
            ("Today’s playlist", "A playlist for each day’s deity, like Shiva on Monday, ready when you open the app."),
            ("Gentle reminders", "A quiet call before sunrise or at the evening aarti, only if you turn them on."),
            ("Sunrise and sunset", "Today’s times for the city you choose, to plan your morning and evening puja."),
            ("Niyama, your daily routine", "Tick off morning aarti, japa and sandhya deepam, and keep your streak going."),
            ("Playlists and sharing", "Like what moves you, build your own playlists and share a reading with family."),
        ],
        faqs=[
            ("Which languages does Bhakti support?",
             "The app’s menus are in English. Each text is in Devanagari, with English transliteration and meaning."),
            ("Can I choose which reminders I get?",
             "Yes. The sunrise and evening aarti reminders arrive only if you turn them on. A single evening "
             "nudge, sent only on days you have not practised yet, can be switched off in Settings."),
            ("Do I need an account?", "No. Bhakti works without signing in, and what you save stays on your phone."),
            ("Is Bhakti on Google Play?", "Not yet. It is coming soon to Google Play for Android."),
            ("Does Bhakti have its own website?",
             'Yes. Visit <a href="https://bhakti.prestia.in">bhakti.prestia.in</a> for more about the app.'),
        ],
        privacy=[("Account required", "No"), ("Ads", "None"), ("Analytics", "None"),
                 ("Likes, playlists and routine", "Stored only on your phone"),
                 ("Internet", "To load audio and artwork"),
                 ("Notifications", "Reminders and playback controls")],
        policy=BHAKTI_SITE + "/privacy", policy_label="Read Bhakti’s full privacy policy",
        site=BHAKTI_SITE,
    ),
    dict(
        slug="sip-calculator", key="sip", name="SIP Calculator", category="Money",
        package="org.ankitkumar.sipcalculatorapp", live=True, min_android="Android 7.0 and later",
        value="Plan SIPs, loans and savings goals, with clear numbers and a simple chart.",
        long=("Enter a monthly amount, an expected return and a time period. See what you invest, what "
              "you could gain and the final value. Set savings goals and track what you put towards them. "
              "No sign-up needed."),
        shots=[], card_shot=None, hero_shots=(),
        features=[
            ("SIP calculator", "Set a monthly amount, return rate and period. See total investment, estimated gains and future value."),
            ("Inflation-adjusted SIP", "Add an inflation rate to see what your returns could be worth in today’s money."),
            ("Lump sum", "See how a one-time investment could grow over the same period."),
            ("Goal calculator", "Start from a target amount and find the monthly SIP you would need."),
            ("Goal tracker", "Set a goal with an optional deadline, add what you save and watch your progress."),
            ("SWP calculator", "Plan regular withdrawals from an invested amount."),
            ("Loan and EMI", "Work out the monthly instalment for a loan amount, rate and tenure."),
            ("FD, RD and PPF", "Quick estimates for fixed deposits, recurring deposits and PPF."),
        ],
        faqs=[
            ("Are the results guaranteed?",
             "No. The app shows estimates based on the return rate you enter. Real returns change with the market."),
            ("Is this financial advice?",
             "No. SIP Calculator is a planning tool. For advice, speak to a SEBI-registered investment adviser."),
            ("Do I need to create an account?", "No. Every calculator works without signing in."),
            ("Where are my numbers stored?",
             "Calculations run on your phone, and the goals and contributions you save are stored only on your "
             "phone. The app does use Google services for usage analytics, crash reports and ads; the "
             '<a href="#privacy-summary">privacy summary</a> below lists exactly what they receive.'),
            ("Can I use it on the web?",
             'Yes. A web version is at <a href="https://sip.prestia.in">sip.prestia.in</a>.'),
        ],
        privacy=[("Account required", "No"),
                 ("Amounts, goals and contributions", "Stored only on your phone"),
                 ("Usage analytics", "Yes, Google Firebase Analytics"),
                 ("Crash reports", "Yes, Firebase Crashlytics"),
                 ("Ads", "Banner ads from Google AdMob"),
                 ("Sold to anyone", "Never")],
        policy=None, policy_label="Read the full privacy policy",
        web=SIP_WEB,
    ),
    dict(
        slug="deeplink-tester", key="deeplink", name="Deeplink Tester", category="For Android developers",
        package="org.ankitkumar.deeplinktester", live=True, min_android="Android 7.0 and later",
        value="Test deep links on a real Android device, in seconds.",
        long=("Paste a link, open it and see what happens on your phone. Every link you try is kept in a "
              "history, so you can run it again with one tap. Made for Android developers and testers."),
        shots=[], card_shot=None, hero_shots=(),
        features=[
            ("Open any link", "Paste a custom-scheme or https link and open it with one tap."),
            ("History", "Every link you open is saved with the time it was last triggered, newest first."),
            ("Run it again", "Open any link from your history again with a single tap."),
            ("Copy", "Copy a saved link to the clipboard to share it or use it elsewhere."),
            ("Tidy up", "Delete links you no longer need."),
            ("Clear errors", "If no app on the phone can handle a link, the app tells you so."),
        ],
        faqs=[
            ("Does it need root?", "No. It uses a standard Android intent to open each link."),
            ("Which Android versions are supported?", "Android 7.0 and later."),
            ("Are my links sent anywhere?",
             "No. The app does not request internet access. Your links and their history stay on your device."),
            ("Can I test links for apps I didn’t build?", "Yes. It opens a link the same way a tap would."),
        ],
        privacy=[("Account required", "No"), ("Internet access", "Not requested"),
                 ("Link history", "Stored only on your phone"),
                 ("Ads or analytics", "None in the app"), ("Data collected", "None")],
        policy=None, policy_label="Read the full privacy policy",
    ),
]
BY_SLUG = {a["slug"]: a for a in APPS}

# --------------------------------------------------------------------------------------------
# Legal copy. Plain-language drafts, written from what each app's code does. Not legal advice.
# --------------------------------------------------------------------------------------------
LEGAL = {
    "privacy": dict(
        title="Privacy Policy",
        description="How the Prestia website and its apps, Bhakti, SIP Calculator and Deeplink Tester, handle your data.",
        summary=[
            "This website uses no cookies, analytics or advertising.",
            "None of the apps needs an account.",
            "Bhakti and Deeplink Tester collect no personal data.",
            "SIP Calculator uses Google services for usage analytics, crash reports and ads. The details are below.",
            "Your data is never sold.",
        ],
        sections=[
            ("scope", "What this covers", [
                f"This policy covers the {BRAND} website and three Android apps: Bhakti, SIP Calculator and "
                f"Deeplink Tester. {BRAND} is the name under which Ankit Kumar, an independent developer in "
                "India, publishes apps. “We” and “us” below mean him.",
                'Bhakti also has its own, more detailed policy at '
                '<a href="https://bhakti.prestia.in/privacy">bhakti.prestia.in/privacy</a>. For Bhakti, that '
                "policy is the one that applies.",
            ]),
            ("website", "This website", [
                "This website is hosted on GitHub Pages, a service of GitHub. To deliver each page, GitHub "
                "receives your IP address and basic details of the request, such as your browser, and may keep "
                "them in its logs.",
                "Fonts are loaded from Google Fonts, so Google also receives your IP address when a page loads.",
                "The site sets no cookies and runs no analytics or advertising. If you switch between light and "
                "dark mode, that choice is saved in your own browser only.",
            ]),
            ("bhakti", "Bhakti", [
                "Bhakti has no account, no ads and no analytics. What you save, such as liked tracks, "
                "bookmarks, playlists, your daily routine and streak, reminder settings, your chosen city and "
                "text size, is stored only on your phone.",
                "The app loads prayer audio and artwork from the servers that host them. Those servers see your "
                "IP address and basic device details, as any website would.",
                "It asks for notifications (for reminders and playback controls), optional exact alarms, "
                "permission to restore reminders after a restart, background playback and internet access. It "
                "does not ask for your location, contacts, microphone, camera or files.",
            ]),
            ("sip-calculator", "SIP Calculator", [
                "SIP Calculator has no account. The amounts, rates and periods you enter are calculated on your "
                "phone, and the goals and contributions you save are stored only on your phone. We do not "
                "receive them.",
                "The app uses these Google services, which receive information under Google’s own privacy "
                'policy (<a href="https://policies.google.com/privacy">policies.google.com/privacy</a>):',
                "<strong>Firebase Analytics</strong> records how the app is used: for example when it opens, "
                "which screens and calculators you visit, the return rate and number of years in a calculation, "
                "a goal’s category, and a rough size band (low, mid or high) when you add a contribution. "
                "It does not record your exact amounts or goal names. Google links these events to an app "
                "instance ID and basic device details.",
                "<strong>Firebase Crashlytics</strong> sends a report with device and app details when the app "
                "crashes, so problems can be fixed. <strong>Firebase Remote Config</strong> fetches settings, "
                "such as whether ads are shown.",
                "<strong>Google AdMob</strong> shows banner ads when they are switched on. AdMob may use your "
                "device’s advertising ID and usage details to choose and measure ads. You can reset or "
                "delete your advertising ID in Android settings.",
                "The “Suggest a feature” option opens a Google Form in your browser. Anything you type "
                "there is sent to us through Google Forms.",
            ]),
            ("deeplink-tester", "Deeplink Tester", [
                "Deeplink Tester does not request internet access. The links you open, and the time each was "
                "last opened, are stored only on your phone. There is no account, no ads and no analytics.",
                "When you open a link, Android passes it to whichever app handles it. What that app does with "
                "the link is up to that app.",
            ]),
            ("google-play", "Google Play and Android", [
                "The apps are distributed through Google Play. Google may collect information when you download "
                "or update them, as described in its own privacy policy.",
                "If Android’s backup is turned on for your phone, Android may include the apps’ data "
                "in your device backup with Google.",
            ]),
            ("email", "If you email us", [
                f'If you write to <a href="mailto:{EMAIL}">{EMAIL}</a>, your email address and message are used '
                "only to reply to you.",
            ]),
            ("choices", "Your choices", [
                "You can uninstall an app at any time. Data stored only on your phone is removed with it, or "
                "when you clear the app’s storage in Android settings.",
                f'To ask about or delete any data, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.',
            ]),
            ("children", "Children", [
                "We do not knowingly collect personal data from children under 13. Bhakti is made for the whole "
                "family and collects no personal data from anyone. If you believe a child has sent us personal "
                f'data, write to <a href="mailto:{EMAIL}">{EMAIL}</a> and it will be deleted.',
            ]),
            ("changes", "Changes", ["If this policy changes, the date at the top will change too."]),
            ("contact", "Contact", [
                f'Questions about privacy? Write to <a href="mailto:{EMAIL}">{EMAIL}</a>.']),
        ],
    ),
    "terms": dict(
        title="Terms of Use",
        description="The terms for using the Prestia website and its apps.",
        summary=[
            "Use the apps for personal, lawful purposes.",
            "The apps are provided as they are.",
            "Calculators show estimates, not financial advice.",
            "These terms follow the laws of India.",
        ],
        sections=[
            ("accept", "Using these apps", [
                f"These terms cover the {BRAND} website and its apps: Bhakti, SIP Calculator and Deeplink Tester. "
                "By using the website or an app, you agree to them. If you do not agree, please do not use them.",
                'Bhakti also has its own terms at <a href="https://bhakti.prestia.in/terms">bhakti.prestia.in/terms</a>.',
            ]),
            ("use", "Fair use", [
                "Use the apps for personal, lawful purposes. Do not try to break, copy or resell them."]),
            ("content", "Content", [
                "The devotional texts in Bhakti are traditional. Some recordings and artwork are by other "
                "creators and remain theirs. If you believe something is used without the right to do so, "
                f'write to <a href="mailto:{EMAIL}">{EMAIL}</a>.',
            ]),
            ("advice", "No financial advice", [
                "SIP Calculator shows estimates based on the numbers you enter. It is not investment advice, and "
                "real returns change with the market."]),
            ("links", "Links you test", [
                "Deeplink Tester opens the links you enter. You are responsible for the links you open and for "
                "what the receiving app does with them."]),
            ("warranty", "No guarantees", [
                "The apps are provided as they are. Every effort is made to keep them working, but they may "
                "sometimes have errors, and features may change or stop."]),
            ("law", "Governing law", ["These terms are governed by the laws of India."]),
            ("contact", "Contact", [
                f'Questions about these terms? Write to <a href="mailto:{EMAIL}">{EMAIL}</a>.']),
        ],
    ),
}

# --------------------------------------------------------------------------------------------
# Shared pieces
# --------------------------------------------------------------------------------------------
THEME_BOOT = ("<script>(function(){var d=document.documentElement;d.className+=' js';"
              "try{var t=localStorage.getItem('prestia-theme');if(t==='light'||t==='dark')d.setAttribute('data-theme',t)}"
              "catch(e){}})();</script>")


def head(r, title, description, base_script=""):
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{base_script}<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#F7F5F0" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#161513" media="(prefers-color-scheme: dark)">
{THEME_BOOT}
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS.replace('&', '&amp;')}">
<link rel="stylesheet" href="{r}assets/site.css">
<script src="{r}assets/site.js" defer></script>
</head>
"""


def home_href(r, anchor, on_home):
    return f"#{anchor}" if on_home else f"{r}#{anchor}"


def header(r, on_home=False):
    h = lambda a: home_href(r, a, on_home)
    home = "#top" if on_home else (r or "./")
    return f"""<body id="top">
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="wordmark" href="{home}" aria-label="{BRAND} home">{BRAND}</a>
    <nav class="main-nav" aria-label="Main">
      <a href="{h('apps')}">Apps</a>
      <a href="{h('about')}">About</a>
      <a href="{h('contact')}">Contact</a>
    </nav>
    <div class="header-actions">
      <button type="button" class="icon-btn" data-theme-toggle aria-label="Switch to dark mode" title="Switch to dark mode"><span class="theme-glyph" aria-hidden="true"></span></button>
      <a class="btn btn-m btn-primary header-cta" href="{h('apps')}">View apps</a>
      <button type="button" class="menu-btn" data-menu-toggle aria-expanded="false" aria-controls="mobile-menu">Menu</button>
    </div>
  </div>
  <nav id="mobile-menu" class="mobile-nav" aria-label="Mobile" hidden>
    <a href="{h('apps')}">Apps</a>
    <a href="{h('about')}">About</a>
    <a href="{h('contact')}">Contact</a>
    <a class="btn btn-primary mobile-cta" href="{h('apps')}">View apps</a>
  </nav>
</header>
"""


def footer(r, on_home=False):
    h = lambda a: home_href(r, a, on_home)
    home = "#top" if on_home else (r or "./")
    app_links = "\n".join(
        f'          <li><a href="{r}apps/{a["slug"]}/#privacy-summary">{a["name"]}</a></li>' for a in APPS)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="wordmark" href="{home}">{BRAND}</a>
        <p>Thoughtful apps for everyday life. Made in India.</p>
      </div>
      <div>
        <h2 class="label">Studio</h2>
        <ul>
          <li><a href="{h('apps')}">Apps</a></li>
          <li><a href="{h('about')}">About</a></li>
          <li><a href="{h('contact')}">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2 class="label">Legal</h2>
        <ul>
          <li><a href="{r}privacy/">Privacy</a></li>
          <li><a href="{r}terms/">Terms</a></li>
          <li><a href="{h('contact')}">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2 class="label">App privacy</h2>
        <ul>
{app_links}
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <span>© {YEAR} {BRAND}</span>
      <span>Android apps for Google Play</span>
    </div>
  </div>
</footer>
</body>
</html>
"""


def icon(r, app, size_class="app-icon", alt=""):
    return (f'<img class="{size_class}" src="{r}assets/img/icons/{app["slug"]}.webp" alt="{escape(alt)}" '
            f'width="160" height="160">')


def phone(r, app, shot=None, eager=False, cls=""):
    """A phone frame. With a real screenshot when there is one; otherwise a neutral block that shows
    only the app's icon and name, never an invented screen."""
    loading = "eager" if eager else "lazy"
    if shot:
        base = f'{r}assets/img/{app["slug"]}/{shot}'
        inner = (f'<img class="for-light" src="{base}-light.webp" alt="" width="540" height="1200" loading="{loading}" decoding="async">'
                 f'<img class="for-dark" src="{base}-dark.webp" alt="" width="540" height="1200" loading="lazy" decoding="async">')
    else:
        inner = (f'<span class="ph-block">{icon(r, app, "ph-icon")}'
                 f'<span class="ph-name">{escape(app["name"])}</span></span>')
    return (f'<div class="phone {cls}" aria-hidden="true"><div class="screen">{inner}</div>'
            f'<span class="cam"></span></div>')


def store_button(app, size="l"):
    url = PLAY + app["package"]
    if size == "s":
        text = "Get it" if app["live"] else "Coming soon"
        label = (f"Get {app['name']} on Google Play" if app["live"]
                 else f"{app['name']} is coming soon to Google Play")
        return f'<a class="store-s" href="{url}" aria-label="{escape(label)}">{text}</a>'
    top = "Get it on" if app["live"] else "Coming soon to"
    label = "Get it on Google Play" if app["live"] else "Coming soon to Google Play"
    return (f'<a class="store-l" href="{url}" aria-label="{label}"><span class="tri" aria-hidden="true"></span>'
            f'<span class="store-text"><span class="s1">{top}</span><span class="s2">Google Play</span></span></a>')


def label(text, tag="div", extra=""):
    return f'<{tag} class="label"{extra}>{text}</{tag}>'


# --------------------------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------------------------
def page_home():
    r = ""
    bh, sip, dl = BY_SLUG["bhakti"], BY_SLUG["sip-calculator"], BY_SLUG["deeplink-tester"]
    cards = []
    for a in APPS:
        badge = "Android · Google Play" if a["live"] else "Android · Coming soon to Google Play"
        cards.append(f"""        <article class="card app-{a['key']}">
          <div class="card-media">{phone(r, a, a['card_shot'])}</div>
          <div class="card-body">
            <div class="app-id">{icon(r, a)}
              <div class="app-id-text"><h3>{a['name']}</h3><div class="cat">{a['category']}</div></div>
            </div>
            <p class="value">{a['value']}</p>
            <div class="badge">{badge}</div>
            <div class="card-foot">
              <a class="learn" href="apps/{a['slug']}/" aria-label="Learn more about {a['name']}">Learn more <span aria-hidden="true">→</span></a>
              {store_button(a, 's')}
            </div>
          </div>
        </article>""")
    cards = "\n".join(cards)
    body = f"""<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        {label("Independent software studio · India")}
        <h1 class="display">Thoughtful apps for everyday life.</h1>
        <p class="lede">Simple, calm tools for money, faith and daily routines. Designed and built in India by one maker, with care for every detail.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="#apps">Explore our apps <span aria-hidden="true">→</span></a>
          <a class="btn btn-secondary" href="#about">Read the maker’s note</a>
        </div>
        <ul class="chips" aria-label="Principles">
          <li class="chip">No sign-up</li>
          <li class="chip">No dark patterns</li>
          <li class="chip">Made with care</li>
        </ul>
      </div>
      <div class="hero-art" role="img" aria-label="Bhakti’s home screen on a phone, between phones showing the SIP Calculator and Deeplink Tester icons">
        <div class="backdrop"></div>
        <div class="hp hp-left app-sip">{phone(r, sip, eager=True)}</div>
        <div class="hp hp-right app-deeplink">{phone(r, dl, eager=True)}</div>
        <div class="hp hp-center app-bhakti">{phone(r, bh, 'home', eager=True)}</div>
      </div>
    </div>
  </section>

  <section id="apps" class="section">
    <div class="wrap">
      <div class="section-head">
        <div>
          {label("Apps")}
          <h2 class="h2 narrow">Three small apps, each made to do one job well.</h2>
        </div>
        <p class="section-aside">SIP Calculator and Deeplink Tester are on Google Play now, and Bhakti is coming soon. Each app keeps its own colour, so you always know where you are.</p>
      </div>
      <div class="cards">
{cards}
      </div>
    </div>
  </section>

  <section id="principles" class="section alt">
    <div class="wrap">
      {label("Principles")}
      <h2 class="h2 narrow">Three promises behind every app.</h2>
      <div class="principles">
        <div class="principle">
          <div class="p-icon" aria-hidden="true"><span class="shape-circle"></span></div>
          <h3>Clear about your data</h3>
          <p>No accounts, and what you enter stays on your phone. Where an app uses an outside service, like the analytics and ads in SIP Calculator, its page says so plainly.</p>
        </div>
        <div class="principle">
          <div class="p-icon" aria-hidden="true"><span class="shape-square"></span></div>
          <h3>Simple, with no tricks</h3>
          <p>No dark patterns and no hidden settings. Each app does one job and stays out of your way.</p>
        </div>
        <div class="principle">
          <div class="p-icon" aria-hidden="true"><span class="shape-diamond"></span></div>
          <h3>Made with care</h3>
          <p>Every screen is designed and tested by hand, with clear, readable type that works for the whole family.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="about" class="section">
    <div class="wrap about-grid">
      <div class="monogram" aria-hidden="true"><span class="mono-letters">AK</span><span class="mono-caption">Ankit Kumar · India</span></div>
      <div class="about-copy">
        {label("From the maker")}
        <h2 class="h2">Small apps, looked after properly.</h2>
        <div class="about-text">
          <p>Hi, I’m Ankit. I make {BRAND} apps on my own, from India.</p>
          <p>I started because many everyday apps felt loud, and asked for permissions they didn’t need. I wanted tools my parents could use without help, and that I would trust with my own data.</p>
          <p>Each app here is small, focused and maintained. If something breaks, you can write to me and I will read it.</p>
        </div>
        <div class="signature"><span class="sig-name">Ankit Kumar</span><span class="sig-role">Founder, {BRAND}</span></div>
      </div>
    </div>
  </section>

  <section id="contact" class="section">
    <div class="wrap side-grid">
      <div>
        {label("Contact")}
        <h2 class="h2">Get in touch</h2>
        <p class="side-note">Questions, feedback, press or partnerships. Every message is read by a person.</p>
      </div>
      <div class="contact-rows">
        <div class="contact-row">
          <div class="contact-text">
            {label("Support")}
            <a class="contact-email" href="mailto:{EMAIL}">{EMAIL}</a>
            <p>Help with any app, bug reports and ideas.</p>
          </div>
          <button type="button" class="copy-btn" data-copy="{EMAIL}" aria-label="Copy support email address">Copy</button>
        </div>
        <div class="contact-row">
          <div class="contact-text">
            {label("Press &amp; partnerships")}
            <a class="contact-email" href="mailto:{EMAIL}?subject=Press">{EMAIL}</a>
            <p>Add “Press” or “Partnership” to the subject line.</p>
          </div>
          <button type="button" class="copy-btn" data-copy="{EMAIL}" aria-label="Copy press email address">Copy</button>
        </div>
        <p class="sr-only" aria-live="polite" data-copy-status></p>
      </div>
    </div>
  </section>
</main>
"""
    html = (head(r, f"{BRAND} · Thoughtful apps for everyday life",
                 f"{BRAND} is an independent, one-person software studio in India making calm Android apps: Bhakti, SIP Calculator and Deeplink Tester.")
            + header(r, on_home=True) + body + footer(r, on_home=True))
    write("index.html", html)


# --------------------------------------------------------------------------------------------
# App detail
# --------------------------------------------------------------------------------------------
def page_app(a):
    r = "../../"
    if a["hero_shots"]:
        s1, s2 = a["hero_shots"]
        art = (f'<div class="dp dp-a">{phone(r, a, s1, eager=True)}</div>'
               f'<div class="dp dp-b">{phone(r, a, s2, eager=True)}</div>')
        art_label = f"{a['name']} screens"
    else:
        art = f'<div class="dp dp-single">{phone(r, a, eager=True)}</div>'
        art_label = f"{a['name']} icon on a phone"

    extra_links = []
    if a.get("site"):
        extra_links.append(f'<a class="text-link" href="{a["site"]}">Visit bhakti.prestia.in <span aria-hidden="true">↗</span></a>')
    if a.get("web"):
        extra_links.append(f'<a class="text-link" href="{a["web"]}">Use it on the web <span aria-hidden="true">↗</span></a>')
    extra = f'<div class="hero-links">{"".join(extra_links)}</div>' if extra_links else ""

    shots_section = ""
    if a["shots"]:
        figs = "\n".join(
            f'          <figure class="shot">{phone(r, a, stem)}<figcaption>{cap}</figcaption></figure>'
            for stem, cap in a["shots"])
        shots_section = f"""
  <section class="section" aria-labelledby="shots-title">
    <div class="wrap">
      {label("Screenshots")}
      <h2 class="h2" id="shots-title">A closer look</h2>
      <div class="shots" tabindex="0" role="region" aria-label="Screenshots, scroll sideways on small screens">
{figs}
      </div>
    </div>
  </section>
"""

    features = "\n".join(
        f'        <div class="feature"><h3>{t}</h3><p>{b}</p></div>' for t, b in a["features"])
    rows = "\n".join(
        f'          <div class="prow"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in a["privacy"])
    policy_href = a["policy"] or f"{r}privacy/#{a['slug']}"
    policy_arrow = "↗" if a["policy"] else "→"
    marks = ("–", "+")
    faqs = "\n".join(f"""        <div class="faq{' open' if i == 0 else ''}">
          <h3><button type="button" class="faq-q" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="faq-{i}" id="faq-q-{i}"><span>{q}</span><span class="faq-mark" aria-hidden="true">{marks[0] if i == 0 else marks[1]}</span></button></h3>
          <div class="faq-a" id="faq-{i}" role="region" aria-labelledby="faq-q-{i}"><p>{ans}</p></div>
        </div>""" for i, (q, ans) in enumerate(a["faqs"]))
    others = "\n".join(f"""        <a class="other" href="{r}apps/{o['slug']}/">{icon(r, o)}
          <span class="other-text"><span class="other-name">{o['name']}</span><span class="other-value">{o['value']}</span></span>
          <span class="other-arrow" aria-hidden="true">→</span></a>""" for o in APPS if o is not a)
    cta_line = ("Available for Android on Google Play." if a["live"]
                else "Coming soon for Android on Google Play.")

    body = f"""<main id="main" class="app-{a['key']}">
  <section class="app-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}#apps">Apps</a><span aria-hidden="true">/</span><span aria-current="page">{a['name']}</span></nav>
      <div class="hero-grid app-hero-grid">
        <div class="hero-copy">
          {icon(r, a, "app-icon-l")}
          <div class="label cat-label">{a['category']}</div>
          <h1 class="h1">{a['name']}</h1>
          <p class="value-l">{a['value']}</p>
          <p class="long">{a['long']}</p>
          <div class="store-row">{store_button(a)}<span class="meta">Android only · {a['min_android']}</span></div>
          {extra}
        </div>
        <div class="detail-art" role="img" aria-label="{escape(art_label)}">{art}</div>
      </div>
    </div>
  </section>
{shots_section}
  <section class="section alt" aria-labelledby="features-title">
    <div class="wrap side-grid">
      <div>
        {label("Features")}
        <h2 class="h2" id="features-title">What it does</h2>
      </div>
      <div class="features">
{features}
      </div>
    </div>
  </section>

  <section id="privacy-summary" class="section" aria-labelledby="privacy-title">
    <div class="wrap side-grid">
      <div>
        {label("Privacy")}
        <h2 class="h2" id="privacy-title">Your data, in plain words</h2>
        <p class="side-note">A short summary of what {a['name']} does with your information.</p>
        <a class="text-link" href="{policy_href}">{a['policy_label']} <span aria-hidden="true">{policy_arrow}</span></a>
      </div>
      <div class="psum">
        <div class="psum-tag"><span class="tag">From the app’s code · {UPDATED}</span></div>
        <dl>
{rows}
        </dl>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="faq-title">
    <div class="wrap side-grid">
      <div>
        {label("FAQ")}
        <h2 class="h2" id="faq-title">Common questions</h2>
      </div>
      <div class="faqs" data-accordion>
{faqs}
      </div>
    </div>
  </section>

  <section class="cta-section" aria-labelledby="get-title">
    <div class="wrap">
      <div class="cta-band">
        <div class="cta-id">{icon(r, a, "app-icon-m")}
          <div><h2 class="cta-title" id="get-title">Get {a['name']}</h2><p>{cta_line}</p></div>
        </div>
        {store_button(a)}
      </div>
      <h2 class="label more-label">More from {BRAND}</h2>
      <div class="others">
{others}
      </div>
    </div>
  </section>
</main>
"""
    title = f"{a['name']} · {BRAND}"
    write(f"apps/{a['slug']}/index.html", head(r, title, a["value"]) + header(r) + body + footer(r))


# --------------------------------------------------------------------------------------------
# Privacy and Terms
# --------------------------------------------------------------------------------------------
def page_legal(kind):
    r = "../"
    L = LEGAL[kind]
    toc = "\n".join(f'            <li><a href="#{sid}">{t}</a></li>' for sid, t, _ in L["sections"])
    if kind == "privacy":
        toc += '\n            <li><a href="#app-privacy">App privacy summaries</a></li>'
    summary = "\n".join(f"              <li>{s}</li>" for s in L["summary"])
    sections = "\n".join(
        f'          <section id="{sid}" class="legal-sec"><h2>{t}</h2>'
        + "".join(f"<p>{p}</p>" for p in paras) + "</section>"
        for sid, t, paras in L["sections"])
    app_list = ""
    if kind == "privacy":
        items = "\n".join(
            f'              <a class="app-priv app-{a["key"]}" href="{r}apps/{a["slug"]}/#privacy-summary">{icon(r, a, "app-icon-s")}'
            f'<span>{a["name"]}</span><span class="other-arrow" aria-hidden="true">→</span></a>' for a in APPS)
        app_list = f"""
          <section id="app-privacy" class="legal-sec"><h2>App privacy summaries</h2>
            <div class="app-priv-list">
{items}
            </div>
          </section>"""
    p_cur = ' aria-current="page"' if kind == "privacy" else ""
    t_cur = ' aria-current="page"' if kind == "terms" else ""
    body = f"""<main id="main">
  <section class="legal">
    <div class="wrap">
      <nav class="seg" aria-label="Legal documents">
        <a href="{r}privacy/"{p_cur}>Privacy</a>
        <a href="{r}terms/"{t_cur}>Terms</a>
      </nav>
      <div class="legal-grid">
        <aside class="toc" aria-labelledby="toc-title">
          <div class="toc-inner">
            <h2 class="label" id="toc-title">On this page</h2>
            <ul>
{toc}
            </ul>
          </div>
        </aside>
        <article class="legal-article">
          <span class="tag">Draft · review before publishing</span>
          <h1 class="h1">{L['title']}</h1>
          <p class="updated">Last updated {UPDATED}</p>
          <div class="in-short">
            <h2>In short</h2>
            <ul>
{summary}
            </ul>
          </div>
{sections}{app_list}
        </article>
      </div>
    </div>
  </section>
</main>
"""
    write(f"{kind}/index.html", head(r, f"{L['title']} · {BRAND}", L["description"]) + header(r) + body + footer(r))


# --------------------------------------------------------------------------------------------
# 404 and the old addresses used in the Play listings
# --------------------------------------------------------------------------------------------
def page_404():
    # GitHub Pages serves this file for a missing path at any depth, so relative links would point
    # to the wrong place. Set a <base> to the site root first: /Prestia/ on the preview, / on a domain.
    base = ("<script>(function(){var p=location.pathname,b=/^\\/Prestia(\\/|$)/i.test(p)?'/Prestia/':'/';"
            "document.write('<base href=\"'+b+'\">')})();</script>\n<noscript><base href=\"/\"></noscript>\n")
    r = ""
    body = f"""<main id="main">
  <section class="hero notfound">
    <div class="wrap">
      {label("Error 404")}
      <h1 class="display">This page could not be found.</h1>
      <p class="lede">The link may be old, or the address may have a typo. Everything on this site is a click away from the home page.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="./">Go to the home page <span aria-hidden="true">→</span></a>
        <a class="btn btn-secondary" href="./#apps">See the apps</a>
      </div>
    </div>
  </section>
</main>
"""
    html = head(r, f"Page not found · {BRAND}", "This page could not be found.", base) + header("./") + body + footer("./")
    write("404.html", html)


def redirect_page(path, target, title):
    """A tiny page that forwards an old address to its new home, for links printed in the Play
    listings (www.prestia.in/sipcalculator/privacy-policy and the like)."""
    html = f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · {BRAND}</title>
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target}">
<style>body{{font:16px/1.6 system-ui,sans-serif;margin:40px 20px;background:#F7F5F0;color:#23211E}}a{{color:#3D4A9C}}@media (prefers-color-scheme:dark){{body{{background:#161513;color:#EFECE6}}a{{color:#A3ADEA}}}}</style>
</head>
<body>
<p>{escape(title)} has moved. <a href="{target}">Continue to the new page</a>.</p>
<script>location.replace({target!r});</script>
</body>
</html>
"""
    write(path, html)


def write(rel, text):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    print("wrote", rel)


if __name__ == "__main__":
    page_home()
    for a in APPS:
        page_app(a)
    page_legal("privacy")
    page_legal("terms")
    page_404()
    redirect_page("sipcalculator/index.html", "../apps/sip-calculator/", "SIP Calculator")
    redirect_page("sipcalculator/privacy-policy/index.html", "../../privacy/#sip-calculator", "SIP Calculator privacy policy")
    redirect_page("deeplinktester/index.html", "../apps/deeplink-tester/", "Deeplink Tester")
    redirect_page("deeplinktester/privacy-policy/index.html", "../../privacy/#deeplink-tester", "Deeplink Tester privacy policy")
