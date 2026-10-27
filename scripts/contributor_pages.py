from html import escape
from html.parser import HTMLParser
from pathlib import Path
import posixpath

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
SUPPORT_PAGES = {"about.html", "contributors/riley-hart.html"}
EXCLUDED_PAGES = {"googled495b3fc6f0765f8.html", "collections/rainy-day-activities-for-preschoolers.html"}


class PagePositions(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.line_starts = [0] + [i + 1 for i, char in enumerate(source) if char == "\n"]
        self.h1_end = None
        self.head_end = None

    def absolute_position(self):
        line, column = self.getpos()
        return self.line_starts[line - 1] + column

    def handle_endtag(self, tag):
        if tag == "h1" and self.h1_end is None:
            self.h1_end = self.source.index(">", self.absolute_position()) + 1
        if tag == "head":
            self.head_end = self.absolute_position()


def with_contributor_credit(source, relative_path):
    markers = (source.count('data-kal-contributor="credit"'), source.count('data-kal-contributor="style"'))
    if markers == (1, 1):
        return source
    if markers != (0, 0):
        raise ValueError(f"Partial or duplicate contributor markup: {relative_path}")
    positions = PagePositions(source)
    positions.feed(source)
    if positions.h1_end is None or positions.head_end is None:
        raise ValueError(f"Contributor page needs a head and H1: {relative_path}")
    parent = Path(relative_path).parent.as_posix()
    profile = posixpath.relpath("contributors/riley-hart.html", parent)
    stylesheet = posixpath.relpath("assets/contributors.css", parent)
    credit = f'\n        <p class="contributor-credit" data-kal-contributor="credit">Research by <a href="{escape(profile)}">Riley Hart</a> <span>&middot; AI research contributor</span></p>'
    style = f'<link data-kal-contributor="style" rel="stylesheet" href="{escape(stylesheet)}?v=1">\n'
    # Insert from the end so parser offsets still refer to the original bytes.
    for position, value in sorted([(positions.h1_end, credit), (positions.head_end, style)], reverse=True):
        source = source[:position] + value + source[position:]
    return source


def support_page(path, title, description, kicker, heading, body):
    parent = Path(path).parent.as_posix()
    rel = lambda target: posixpath.relpath(target, parent)
    canonical = f"https://kidactivitylab.com/{path}"
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{escape(title)} | Kid Activity Lab</title>
    <meta name="description" content="{escape(description)}">
    <link rel="canonical" href="{canonical}">
    <link rel="stylesheet" href="{rel("styles.css")}">
    <link rel="stylesheet" href="{rel("assets/contributors.css")}?v=1">
  </head>
  <body>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/">Kid Activity Lab</a>
        <div class="nav-links"><a href="/">Home</a><a href="{rel("cards.html")}">Cards</a><a href="{rel("about.html")}">About</a></div>
      </nav>
    </header>
    <main class="contributor-profile">
      <p class="kicker">{escape(kicker)}</p>
      <h1>{escape(heading)}</h1>
{body}
    </main>
    <footer class="site-footer"><p><a href="{rel("about.html")}">About Kid Activity Lab</a> &middot; <a href="{rel("contributors/riley-hart.html")}">Riley Hart, AI research contributor</a> &middot; <a href="{rel("cards.html")}">Activity cards</a></p></footer>
  </body>
</html>
'''


def contributor_pages():
    profile = support_page(
        "contributors/riley-hart.html", "Riley Hart | AI Research Contributor",
        "Meet Kid Activity Lab's AI research contributor, learn how the work is checked, and identify the responsible publisher.",
        "AI research contributor", "Riley Hart",
        '''      <p class="profile-intro">Riley Hart is the name used for Kid Activity Lab's AI research contributor.</p>
      <section aria-labelledby="contribution">
        <h2 id="contribution">What Riley contributes</h2>
        <p>The role helps research public sources, compare activity instructions, draft parent setup notes, and maintain guides and cards. A credit describes this ongoing contribution, rather than sole original authorship of every earlier sentence.</p>
        <ul><li>Keep source links, check dates and conflicting details visible.</li><li>Turn research into materials, adult setup, a kid mission and a rescue route.</li><li>Identify estimates, editorial choices and questions the evidence cannot settle.</li></ul>
      </section>
      <section aria-labelledby="review">
        <h2 id="review">How the work is checked</h2>
        <p>Material changes receive a separate read-only AI review and technical checks before release. That review checks the research and implementation; it is not family testing or a substitute for firsthand evidence.</p>
        <p>Riley is an AI role with no human biography, professional qualification or personal experience to claim. A contributor credit does not mean an activity was tried with a child. Individual pages must identify any actual firsthand observations and retain their own source-check dates.</p>
      </section>
      <section aria-labelledby="publisher">
        <h2 id="publisher">Who publishes the site</h2>
        <p><a href="../about.html#apoorva-garg">Apoorva Garg, founder and publisher</a>, is responsible for Kid Activity Lab. The credit does not mean Apoorva personally reviews every page. Read <a href="../about.html#research-process">how our research works</a>.</p>
      </section>
      <section aria-labelledby="return">
        <h2 id="return">Back to an activity</h2>
        <ul><li><a href="../articles/paper-bridge-challenge-kids.html">Paper Bridge Challenge</a></li><li><a href="../collections/card-games-for-kids.html">Card games with one deck</a></li><li><a href="../cards.html">Browse activity cards</a></li></ul>
      </section>'''
    )
    about = support_page(
        "about.html", "About Kid Activity Lab",
        "Who publishes Kid Activity Lab, how AI contributes, and what research-backed activity guidance can and cannot tell you.",
        "Our research", "About Kid Activity Lab",
        '''      <p class="profile-intro">We help a caregiver choose something that fits the child and the moment, then make it easy to start.</p>
      <section aria-labelledby="apoorva-garg">
        <h2 id="apoorva-garg">Apoorva Garg</h2>
        <p>Founder and publisher of Kid Activity Lab. Apoorva sets the direction and is responsible for publication. This does not imply personal review or firsthand use of every activity.</p>
        <p><a href="https://www.linkedin.com/in/apoorvag20/">Apoorva Garg on LinkedIn</a></p>
      </section>
      <section aria-labelledby="research-process">
        <h2 id="research-process">How our research works</h2>
        <p><a href="contributors/riley-hart.html">Riley Hart, AI research contributor</a>, supports source research, drafting and maintenance. A separate read-only AI reviewer checks material changes, alongside technical and page checks.</p>
        <p>Our contribution is the synthesis: a useful default, materials and substitutions, adult setup, kid-facing steps, and honest stop or rescue choices. Sources, editorial estimates and uncertainty should remain distinguishable.</p>
      </section>
      <section aria-labelledby="evidence-limits">
        <h2 id="evidence-limits">What the credit means</h2>
        <p>A contributor name is not a claim of family testing, professional expertise or guaranteed suitability. Research-backed guidance has not been tried by Kid Activity Lab unless a page supplies specific valid firsthand evidence.</p>
        <p>Timing, mess, engagement, enjoyment, learning, repeat play and safety outcomes remain unknown without valid observations. Check the individual activity's materials, adult role and stop conditions for your household; source-check dates belong to the facts checked, not to the contributor credit.</p>
      </section>
      <p><a href="cards.html">Choose an activity card</a></p>'''
    )
    return {"contributors/riley-hart.html": profile, "about.html": about}


def sync_contributor_pages(site=SITE):
    for relative, content in contributor_pages().items():
        path = site / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text() != content:
            path.write_text(content)
    count = 0
    for path in sorted(site.rglob("*.html")):
        relative = path.relative_to(site).as_posix()
        if relative in SUPPORT_PAGES or relative in EXCLUDED_PAGES:
            continue
        original = path.read_text()
        updated = with_contributor_credit(original, relative)
        if updated != original:
            path.write_text(updated)
        count += 1
    return count
