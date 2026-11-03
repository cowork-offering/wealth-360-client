"""Builds the Wealth 360 client screening page from the Credit 360 screening page's system.
Every chapter is rewritten around the real Wealth 360 desk; the gate, hero player, breathers,
motion engine and close are the reference's own. Run: python3 build.py"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
s = open('/tmp/c360ref/index.html').read()

def rep(a, b, count=1):
    global s
    n = s.count(a)
    if n < 1:
        sys.exit('MISSING: ' + a[:90])
    s = s.replace(a, b) if count == 0 else s.replace(a, b, count)

def between(start, end, new, incl_end=False):
    global s
    i = s.find(start); j = s.find(end, i)
    if i < 0 or j < 0: sys.exit('MISSING block ' + start[:60])
    if incl_end: j += len(end)
    s = s[:i] + new + s[j:]

CHEV = '<svg viewBox="0 0 19.792 20.93" aria-hidden="true"><use href="#g-chev"/></svg>'
SPIN = '<svg class="spin" viewBox="0 0 19 19"><circle cx="9.5" cy="9.5" r="7.4"/></svg>'
def row(g, lbl): return f'<div class="runrow"><span class="thread"></span><span class="slot">{SPIN}<svg class="gl"><use href="#{g}"/></svg></span><span class="lbl">{lbl}</span></div>'
TICK = '<svg viewBox="0 0 16 16" aria-hidden="true"><use href="#g-tick"/></svg>'

# ---------- head ----------
s = re.sub(r'<title>.*?</title>', '<title>Wealth 360 · A private screening</title>', s, flags=re.S)
s = re.sub(r'<meta name="description"[^>]*>', '<meta name="description" content="Wealth 360. Agents do the routine work of client servicing, Salesforce keeps the rules and the record, and a named person makes every decision that matters." />', s)

# ---------- sprite: the connectors' own marks ----------
NEW_SYM = '''<symbol id="g-shield" viewBox="0 0 19 19"><path d="M9.5 1.9 3.4 4.3v4.5c0 3.9 2.6 6.9 6.1 8.3 3.5-1.4 6.1-4.4 6.1-8.3V4.3Z" fill="none" stroke="#1F2A44" stroke-width="1.5" stroke-linejoin="round"/><path d="M6.6 9.4 8.7 11.4 12.5 7.4" fill="none" stroke="#1F2A44" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="g-payee" viewBox="0 0 19 19"><rect x="1.5" y="1.5" width="16" height="16" rx="4" fill="#111"/><path d="M5.2 13.2V8.4M9.5 13.2V8.4M13.8 13.2V8.4M4.2 7.2 9.5 4.3l5.3 2.9M4.2 14.4h10.6" fill="none" stroke="#fff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="g-id" viewBox="0 0 19 19"><rect x="1.6" y="3.8" width="15.8" height="11.4" rx="2.4" fill="none" stroke="#0F766E" stroke-width="1.5"/><circle cx="6.4" cy="8.6" r="1.7" fill="none" stroke="#0F766E" stroke-width="1.4"/><path d="M3.9 12.6c.4-1.3 1.3-1.9 2.5-1.9s2.1.6 2.5 1.9M11 8h4M11 10.8h3" fill="none" stroke="#0F766E" stroke-width="1.4" stroke-linecap="round"/></symbol>
<symbol id="g-pin" viewBox="0 0 19 19"><path d="M9.5 17.2s5.4-5 5.4-9a5.4 5.4 0 0 0-10.8 0c0 4 5.4 9 5.4 9Z" fill="none" stroke="#B4532A" stroke-width="1.5" stroke-linejoin="round"/><circle cx="9.5" cy="8.2" r="1.9" fill="none" stroke="#B4532A" stroke-width="1.5"/></symbol>
<symbol id="g-mail" viewBox="0 0 19 19"><rect x="1.8" y="3.9" width="15.4" height="11.2" rx="2.2" fill="none" stroke="#3E63B8" stroke-width="1.5"/><path d="m2.6 5.1 6.9 5 6.9-5" fill="none" stroke="#3E63B8" stroke-width="1.5" stroke-linejoin="round"/></symbol>
'''
rep('<symbol id="g-tick"', NEW_SYM + '<symbol id="g-tick"')

# ---------- gate ----------
rep('<p class="eyebrow gp-eyebrow">Dreamforce 2026<span class="dot">&middot;</span>A private screening</p>',
    '<p class="eyebrow gp-eyebrow">London<span class="dot">&middot;</span>A private screening</p>')
rep('Morning, San&nbsp;Francisco.', 'Your clients are in good hands.')
rep('<div class="modelmeta" aria-hidden="true">Fable 5.1<em>Medium</em></div>', '<div class="modelmeta" aria-hidden="true">Opus 5.5<em>Medium</em></div>', 0)
rep('assets/film/sf-gate-plate.mp4', 'assets/film/gate-plate.mp4'); rep('assets/film/sf-gate-plate.jpg', 'assets/film/gate-plate.jpg')
between('<div class="runrows" id="g-rows" aria-hidden="true">', '</div>\n  </div>\n  </div>\n</div>',
  '<div class="runrows" id="g-rows" aria-hidden="true">\n      <div class="runrow" data-g="g-sf"><span class="thread"></span><span class="slot">' + SPIN + '<svg class="gl"><use href="#g-sf"/></svg></span><span class="lbl">Salesforce &middot; your cases</span></div>\n      '
  + '\n      '.join([row('g-ms','Microsoft 365 &middot; mail and calendar'), row('g-mail','Client email &middot; intake'), row('g-shield','UK Sanctions List &middot; screening'), row('g-payee','Payee check &middot; open banking'), row('g-id','Identity &middot; verification'), row('g-pin','Address &middot; postcode')]) + '\n    ')

# ---------- hero ----------
rep('<p class="eyebrow">Dreamforce 2026<span class="dot">&middot;</span>A private screening</p>', '<p class="eyebrow">London<span class="dot">&middot;</span>A private screening</p>')
rep('<span>Credit 360</span></h1>', '<span>Wealth 360</span></h1>')
rep('<p class="hero-line">Your whole book.<br /><span class="dim">Already awake.</span></p>',
    '<p class="hero-line">Every client, given time.<br /><span class="dim">Every request, already prepared.</span></p>')
rep('assets/film/hero-plate.mp4', 'assets/film/hero-plate.mp4')

# ---------- chapters ----------
def facts(*fs):
    out = []
    for f in fs:
        if len(f) == 3: out.append(f'<div class="fact rise"><span class="fl">{f[0]}</span><span class="fv num">{f[1]}</span><span class="fs">{f[2]}</span></div>')
        else: out.append(f'<div class="fact rise"><span class="fl">{f[0]}</span><span class="fp">{f[1]}</span></div>')
    return '<div class="facts">' + ''.join(out) + '</div>'
def cap(n, head, sub):
    return f'<div class="cap"><p class="eyebrow chno"><b>{n:02d}</b><i>/</i>08</p><h2 class="head">{head}</h2><p class="sub">{sub}</p></div>'
def chapter(cid, n, head, sub, fx, stage, flip=False):
    return f'''<section class="chapter{' flip' if flip else ''}" id="{cid}">
  <div class="wrap">
    {cap(n, head, sub)}
    {fx}
    <div class="stage"><div class="fit">{stage}</div></div>
  </div>
</section>
'''
def device(title, body, fav=None):
    ic = fav or '<svg class="ic" width="17" height="17" viewBox="0 0 17 17" aria-hidden="true"><rect x="3.2" y="3.4" width="10.6" height="7.6" rx="1.4"/><path d="M1.6 14.2h13.8"/></svg>'
    return f'<div class="device rise" data-rise><div class="dev-top">{ic}<span class="dev-title">{title}</span></div><div class="dev-body">{body}</div></div>'
def breath(n, img, line_parts, alt):
    seg = ','.join('{"t":"%s"%s}' % (t, ',"k":1' if k else '') for t, k in line_parts)
    plain = ''.join(t for t, k in line_parts)
    rest = ''.join(f'<span class="key">{t}</span>' if k else t for t, k in line_parts)
    return f'''<section class="breath" id="breath-{n}">
  <img src="assets/stills/{img}" alt="{alt}" width="1760" height="990" loading="lazy" decoding="async" />
  <h2 class="sr">{plain}</h2>
  <p class="breath-type" aria-hidden="true" data-seg='[{seg}]'><span class="t"></span><i class="caret"></i><span class="rest">{rest}</span></p>
</section>
'''

# a. the tabs: the original browser window, retitled
a0 = s.find('<section class="chapter" id="ch-a"'); a1 = s.find('<section class="chapter" id="ch-b"')
cha = s[a0:a1]
TABS = ['Salesforce', 'Outlook', 'KYC portal', 'Sanctions search', 'Payee check', 'Address finder', 'SharePoint', 'Teams', 'Documents', 'Cases.xlsx', 'Core platform']
titles = re.findall(r'<span class="tt a">([^<]*)</span>', cha)
for old, new in zip(titles, TABS):
    cha = cha.replace(f'<span class="tt a">{old}</span>', f'<span class="tt a">{new}</span>', 1)
cha = cha.replace('<span class="tt b">Credit 360 for my book</span>', '<span class="tt b">Wealth 360 desk</span>')
cha = re.sub(r'<span class="u1">[^<]*</span>', '<span class="u1">wealth.lightning.force.com/lightning/r/Case/500Hn00002Fm8xQIAR/view?ws=%2Flightning%2Fr%2FAccount%2F001Hn00002Lm4Q2%2Fview</span>', cha)
cha = re.sub(r'<div class="cap">.*?</div>\s*<div class="facts">.*?</div>\s*</div>', cap(1, 'A client writes in. Someone opens eleven tabs.', 'One request, eleven systems, and a morning spent checking each one against the others.') + facts(('Systems', '11', 'open for one request'), ('The request', '1', "a client's email"), ('The screen', 'The Wealth 360 desk')), cha, count=1, flags=re.S)
CH = [cha]

# the lifts: the live desk itself, captured from the running product into static HTML
# (assets/desk/*.html, scripts stripped, the desk's own stylesheet) and shown at its own
# geometry. crop = the window of the 1440-wide page that is shown, in its own pixels.
def lift(src, crop, vh=900, extra='', cls=''):
    x, y, w, h = crop
    return (f'<div class="lift rise {cls}" data-rise style="--cw:{w};--ch:{h}"{extra}>'
            f'<iframe src="assets/desk/{src}.html" title="" aria-hidden="true" tabindex="-1" loading="lazy" '
            f'style="--x:{x};--y:{y};--vh:{vh}"></iframe></div>')
DRAWER = (808, 12, 620)

# b. the desk
CH.append(chapter('ch-b', 2, 'It knows what needs you, and what does not.',
  'The desk reads Salesforce before you arrive. What needs a person stands apart from what the agents are moving on their own.',
  facts(('With you', '13', 'cases, each with its reason'), ('Completed', '5', 'one by the agents alone'), ('Where to start', 'The desk says: the sanctions match')),
  lift('board', (110, 66, 1220, 540), cls='fade')))
CH.append(breath(1, 'breather-1.jpg', [('Every request, already ', 0), ('gathered', 1), ('.', 0)], ''))

# c0. the layer: every system behind one desk, joined by the Experience server
def src(g, name, what, cls=''):
    mark = f'<svg class="ly-g" aria-hidden="true"><use href="#{g}"/></svg>' if g else '<span class="ly-plus" aria-hidden="true"></span>'
    return f'<div class="ly-src {cls}">{mark}<b>{name}</b><span>{what}</span></div>'
srcs = ''.join([src('g-sf', 'Salesforce', 'Clients, accounts, KYC, cases'), src('g-ms', 'Microsoft 365', 'Mail, calendar, Teams'),
    src('g-mail', 'Client email', 'Requests and documents'), src('g-shield', 'UK Sanctions List', 'Screening'),
    src('g-payee', 'Open banking', 'Who owns an account'), src('g-id', 'Identity', 'Document and liveness'),
    src('g-pin', 'Postcode', 'Address lookup'), src(None, 'Any source', 'Added as the firm needs it', 'add')])
def node(cls, k, b, sub):
    return f'<div class="ly-node {cls}"><small>{k}</small><b>{b}</b><span>{sub}</span></div>'
layer_html = ('<div class="layer rise" data-rise id="layer">'
  '<div class="ly-tier"><p class="ly-k">The sources</p><div class="ly-srcs">' + srcs + '</div></div>'
  '<div class="ly-wire"><i></i></div>'
  '<div class="ly-tier"><p class="ly-k">The layer</p><div class="ly-xp">'
    + node('xp', 'Wealth 360 Experience server', 'Every source, joined in code', 'Provider-agnostic: a source is added or swapped behind the same tools, and the agents never change. Every check and decision goes on a ledger.')
    + node('', 'Wealth 360 connector', 'Salesforce, as the person', 'The record, the rules and the fences') + '</div></div>'
  '<div class="ly-wire"><i></i></div>'
  '<div class="ly-tier"><p class="ly-k">The agents</p><div class="ly-row2">'
    + node('', 'Their own identity', 'Case agent', 'Works each step and cites its evidence')
    + node('', 'A fresh context', 'Review agent', 'Checks the work, blind to the first') + '</div></div>'
  '<div class="ly-wire"><i></i></div>'
  '<div class="ly-tier"><div class="ly-row1">' + node('desk', 'One page', 'The desk', 'For the person who decides') + '</div></div>'
  '</div>')
CH.append(chapter('ch-l', 3, 'Every system, one layer.',
  'The firm&rsquo;s systems stay where they are. The Experience server reads and joins them, Salesforce keeps the record, the agents work on top, and one desk shows the result.',
  facts(('Sources', '7+', 'added or swapped as the firm needs'), ('The join', 'In code, never by the model'), ('The record', 'Salesforce, with a decision ledger')),
  layer_html))

# c. the checks
CH.append(chapter('ch-c', 4, 'Every check, already run.',
  'Sanctions, candidate accounts and an independent review, each with its source, before the case reaches you.',
  facts(('Checks', '3', 'each with its source'), ('The match', '93% against a 90% threshold'), ('The review', 'A second agent, in a fresh context')),
  lift('bondarev-checks', DRAWER + (548,), cls='fade')))

# d. the activity: a bereavement, step by step
CH.append(chapter('ch-d', 5, 'Every step, on the record.',
  'A daughter writes to say her father has died. The Case agent works the case one step at a time, and every step lands on the record.',
  facts(('Done', '8 of 13', 'steps before a person is needed'), ('The tone', 'Bereavement, by design'), ('Next', 'An independent check by the Review agent')),
  lift('hale-activity', DRAWER + (560,), cls='fade')))

# e. one sentence
CH.append(chapter('ch-e', 6, 'Say it in one sentence.',
  'A call, a letter, a visit to the office. Write it down in plain words; the case is in Salesforce and the agents start at once.',
  facts(('The form', '1', 'request, in your own words'), ('Picked up', 'Within seconds, by the Case agent'), ('The record', 'A standard case in Salesforce')),
  lift('newcase', (450, 116, 540, 669), cls='modal')))
CH.append(breath(2, 'breather-2.jpg', [('Every family, given ', 0), ('time', 1), ('.', 0)], ''))

# f. the letter waits for you
CH.append(chapter('ch-f', 7, 'The letter writes itself, and waits for you.',
  'Drafted for a family, in the firm&rsquo;s voice, with the facts from the record. Nothing reaches a client until a person approves it.',
  facts(('Drafted', '1', 'letter, in the bereavement tone'), ('The meeting', 'Four times proposed, one chosen by you'), ('Sent', 'Only when you approve it')),
  lift('hale-overview', DRAWER + (560,), cls='fade')))
CH.append(breath(3, 'breather-3.jpg', [('Agents prepare. People ', 0), ('decide', 1), ('.', 0)], ''))

# g. the decision: the plan read back, then saved
CH.append(chapter('ch-g', 8, 'You decide. Salesforce does the rest.',
  'The plan is read back before anything moves. One confirmation, recorded against your name, and the record closes behind it.',
  facts(('On the record', '4', 'steps, from one confirmation'), ('Confirmed by', 'A named person, never an agent'), ('The control', 'Staged, read back, then confirmed')),
  '<div class="decide" id="decide">' + lift('hale-plan', DRAWER + (616,), vh=640) + lift('hale-saved', DRAWER + (616,), vh=640, cls='after') + '</div>'))

# the walkthrough: a second film, six minutes
CH.append('''<section class="walk" id="walk">
  <div class="wrap">
    <p class="eyebrow chno">The walkthrough<span class="dot">&middot;</span>6 minutes</p>
    <h2 class="head">One case, end to end.</h2>
    <p class="sub">What it is, what it is worth, one bereavement worked live in the sandbox, and the layer that joins every system.</p>
    <button class="wt rise" data-rise type="button" id="wtOpen" aria-label="Play the six minute walkthrough">
      <img src="assets/film/walk-poster.jpg" alt="" loading="lazy" decoding="async" />
      <span class="wt-play" aria-hidden="true"><svg viewBox="0 0 13 14"><path d="M1 1.2 12 7 1 12.8Z" fill="currentColor"/></svg><span>Watch the walkthrough</span></span>
    </button>
  </div>
  <div class="wm" id="wm" role="dialog" aria-modal="true" aria-label="Wealth 360 walkthrough" hidden>
    <div class="wm-bar"><span>Wealth 360 &middot; The walkthrough</span><button type="button" class="wm-x" id="wmClose" aria-label="Close"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
    <video id="wmv" controls playsinline preload="none" poster="assets/film/walk-poster.jpg"></video>
  </div>
</section>
''')
g1 = s.find('</main>')
s = s[:a0] + '\n'.join(CH) + s[g1:]

# ---------- the end ----------
rep('assets/film/sf-plate.mp4', 'assets/film/end-plate.mp4'); rep('assets/film/sf-plate-poster.jpg', 'assets/film/end-plate.jpg')
rep('<p class="eyebrow endbrow">Dreamforce 2026</p>', '<p class="eyebrow endbrow">A private screening</p>')
s = re.sub(r'(<p class="endlock">.*?)<span>Credit 360</span>', r'\1<span>Wealth 360</span>', s, count=1, flags=re.S)
rep('<p class="endhead">Meet us at the booth.</p>', '<p class="endhead">Care, with time to give it.</p>')
s = re.sub(r'\s*<!-- the place, drawn.*?</aside>', '', s, count=1, flags=re.S)

# ---------- motion strings ----------
_i = s.find("/* g. approve: the dim, the halo, the executed lines */")
_j = s.find("/* the breathers: the still holds", _i)
s = s[:_i] + '''/* g. the decision: the plan is read back, the person confirms, the drawer says Saved */
    once($('#decide'), function () {
      setTimeout(function () { $('#decide').classList.add('saved'); }, RM ? 0 : 2400);
    });

    ''' + s[_j:]
rep("      once(g, function () {\n        kids.forEach", "      once(g.closest('.chapter') || g, function () {\n        kids.forEach")
rep("NOT = 'Not this one.'", "NOT = 'One desk.'")
rep("var ASK = 'increase to 20';", "var ASK = 'James Okafor called. £3,000 out of his GIA for a new boiler.';")
rep("if (i > 6) { if (i === 7) { setTimeout(function () { r.classList.add('writing'); }, RM ? 0 : 120 + 7 * 90); } return; }",
    "if (i > 7) { if (i === 8) { setTimeout(function () { r.classList.add('writing'); }, RM ? 0 : 120 + 8 * 90); } return; }")
s = s.replace("__c360", "__w360")
s = s.replace('Credit 360', 'Wealth 360')
s = re.sub(r'(?m)^  CREDIT 360 .*$', '  WEALTH 360 · A PRIVATE SCREENING · London', s).replace('THE PLATE IS SAN FRANCISCO','THE PLATE IS LONDON').replace('<!-- San Francisco from altitude','<!-- London from altitude')

open(ROOT / 'index.html', 'w').write(s)
print('ok', len(s), 'credit mentions:', s.lower().count('credit'), 'bank:', len(re.findall(r'\bbank\b', s, re.I)))

# ---------- the Wealth 360 layer: a centred room, and the new components ----------
CSS = r'''<style id="w360">
/* THE ROOM IS CENTRED. Credit 360 reads in a column beside its component and swaps
   sides chapter by chapter. Wealth 360 stands still and symmetrical, the way a
   private office does: the caption centred over the product's own surface, and the
   three facts in one hairline row under it, on the same axis. */
@media (min-width:1080px){
  .chapter > .wrap,.chapter.flip > .wrap{
    grid-template-columns:minmax(0,1fr);
    grid-template-rows:auto minmax(0,1fr) auto;
    grid-template-areas:"cap" "stage" "facts";
    row-gap:clamp(14px,2.6vh,30px);
  }
  .cap{align-self:end; justify-self:center; text-align:center; max-width:980px}
  .cap .sub{max-width:72ch; margin-top:8px}
  .chno{margin-bottom:9px}
  .cap .sub{margin-left:auto; margin-right:auto}
  .stage{padding-inline:clamp(24px,4vw,72px)}
  .facts{align-self:start; justify-self:center; margin-top:0; display:flex; gap:0;
    width:min(980px,100%); border-top:1px solid var(--hair); padding-top:clamp(14px,2.2vh,22px)}
  .fact{flex:1 1 0; min-width:0; text-align:center; padding:0 18px; border-top:0; border-left:1px solid var(--hair)}
  .fact:first-child{border-left:0; padding-left:0}
  .fact:last-child{padding-right:0}
  .fact .fv{font-size:30px; margin-top:6px}
  .fact .fs{font-size:13.5px; margin-top:6px}
  .fact .fp{font-size:16px; margin-top:9px; line-height:1.34}
}
@media (max-width:1079.98px){ .cap{text-align:center} .cap .sub{margin-left:auto;margin-right:auto} .fact{text-align:center} }


@font-face{font-family:"Fraunces";font-style:normal;font-weight:300 400;font-display:swap;src:url("assets/fonts/Fraunces-latin.woff2") format("woff2")}
/* THE TWIST. Same family as Credit 360, its own voice: a private office speaks in a serif.
   The chapter headlines, the hero line, the typed breathers and the close are set in Fraunces, light, at a large optical size (the film's face);
   the product's own surfaces stay in Inter, exactly as the desk draws them. */
.cap .head,.walk .head{font-family:"Fraunces",Georgia,serif; font-weight:360; font-optical-sizing:auto; letter-spacing:-.012em; line-height:1.08;
  font-size:clamp(28px,2.9vw,42px)}
.hero-line{font-family:"Fraunces",Georgia,serif; font-weight:360; font-optical-sizing:auto; letter-spacing:-.01em}
@media (min-width:1080px){.hero-line{white-space:nowrap; font-size:clamp(22px,2.1vw,32px); text-align:right}}
.breath-type{font-family:"Fraunces",Georgia,serif; font-weight:360; font-optical-sizing:auto; letter-spacing:-.012em}
.endhead{font-family:"Fraunces",Georgia,serif; font-weight:360; font-optical-sizing:auto; letter-spacing:-.01em}
#notthis{font-family:"Fraunces",Georgia,serif; font-weight:360; font-optical-sizing:auto; font-size:clamp(22px,2vw,30px)}
.greet{letter-spacing:-.01em}

/* THE JOURNEY RAIL. A case moves through steps; so does the page. One hairline down the left
   edge, seven marks, the one you are in set in ink. Desktop only, never over the films. */
.jrail{position:fixed; left:clamp(16px,2vw,30px); top:50%; transform:translateY(-50%); z-index:60; display:none;
  flex-direction:column; align-items:flex-start; gap:18px; opacity:0; transition:opacity .5s ease; pointer-events:none}
.jrail.on{opacity:1}
.jrail::before{content:""; position:absolute; left:3px; top:4px; bottom:4px; width:1px; background:var(--hair)}
.jrail i{position:relative; display:flex; align-items:center; gap:10px; font-style:normal; font-size:10.5px; font-weight:600;
  letter-spacing:.09em; color:var(--faint); text-transform:uppercase}
.jrail i::before{content:""; width:7px; height:7px; border-radius:50%; background:var(--paper,#F6F3EE); border:1px solid var(--faint); box-sizing:border-box}
.jrail i span{opacity:0; transform:translateX(-4px); transition:opacity .35s ease, transform .35s ease}
.jrail i.done::before{background:var(--faint); border-color:var(--faint)}
.jrail i.now{color:var(--ink-max)}
.jrail i.now::before{background:var(--brand); border-color:var(--brand)}
.jrail i.now span{opacity:1; transform:none}
@media (min-width:1180px){ .jrail{display:flex} }


/* THE LIFT. The desk itself, not a picture of it: a capture of the running product, scripts
   stripped, drawn by its own stylesheet at its own size, through a window onto the part that
   matters. The fit rule scales the window down to the room; nothing is ever scaled up. */
.lift{position:relative; width:calc(var(--cw) * 1px); height:calc(var(--ch) * 1px); max-width:none; margin:0 auto;
  overflow:hidden; border-radius:16px; background:#fff;
  box-shadow:0 0 0 1px rgba(20,20,30,.07), 0 18px 48px -28px rgba(20,20,40,.28)}
.lift iframe{position:absolute; left:0; top:0; border:0; width:1440px; height:calc(var(--vh) * 1px);
  transform:translate(calc(var(--x) * -1px), calc(var(--y) * -1px)); pointer-events:none; background:#fff}
.lift.fade::after{content:""; position:absolute; left:0; right:0; bottom:0; height:56px; pointer-events:none;
  background:linear-gradient(to bottom, rgba(255,255,255,0), #fff)}
.lift.modal{border-radius:18px}
.decide{position:relative; width:620px; height:616px; margin:0 auto}
.decide .lift{position:absolute; inset:0}
.liftbox{margin:0 auto; overflow:hidden}
.liftbox > .lift,.liftbox > .decide{margin:0}
.decide .lift.after{opacity:0; transition:opacity .45s ease}
.decide.saved .lift.after{opacity:1}


/* 03: THE LAYER. Four tiers on one axis: the sources, the connectors, the agents, the desk.
   Hairlines only; the one moving thing is a violet pulse that rises through the wires once. */
.layer{width:min(1040px,100%); margin:0 auto; display:flex; flex-direction:column; align-items:stretch}
.ly-tier{display:flex; flex-direction:column; align-items:center}
.ly-k{font-size:10.5px; font-weight:600; letter-spacing:.09em; text-transform:uppercase; color:var(--faint); margin:0 0 10px}
.ly-srcs{display:grid; grid-template-columns:repeat(8,minmax(0,1fr)); gap:8px; width:100%}
.ly-src.add{background:transparent; border-style:dashed}
.ly-plus{position:relative; width:20px; height:20px; margin-bottom:3px}
.ly-plus::before,.ly-plus::after{content:""; position:absolute; left:50%; top:50%; background:var(--faint); transform:translate(-50%,-50%)}
.ly-plus::before{width:12px; height:1.5px}.ly-plus::after{width:1.5px; height:12px}
.ly-xp{display:grid; grid-template-columns:minmax(0,1.7fr) minmax(0,1fr); gap:10px; width:100%}
.ly-node.xp{border-color:var(--ink-max)}
.ly-node.xp span{max-width:52ch}
.ly-src{display:flex; flex-direction:column; align-items:center; text-align:center; gap:4px; padding:12px 8px 11px;
  background:var(--raised,#fff); border:1px solid var(--hair); border-radius:12px}
.ly-src .ly-g{width:20px; height:20px; margin-bottom:3px}
.ly-src b{font-size:12.5px; font-weight:600; color:var(--ink-max); letter-spacing:-.005em}
.ly-src span{font-size:11px; line-height:1.3; color:var(--muted)}
.ly-row3,.ly-row2,.ly-row1{display:grid; gap:10px; width:100%}
.ly-row3{grid-template-columns:repeat(3,minmax(0,1fr))}
.ly-row2{grid-template-columns:repeat(2,minmax(0,1fr)); width:min(700px,100%)}
.ly-row1{grid-template-columns:minmax(0,1fr); width:min(340px,100%)}
.ly-node{display:flex; flex-direction:column; align-items:center; text-align:center; gap:3px; padding:13px 14px 12px;
  background:var(--raised,#fff); border:1px solid var(--hair); border-radius:12px}
.ly-node small{font-size:10px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--faint)}
.ly-node b{font-size:15px; font-weight:600; color:var(--ink-max); letter-spacing:-.01em}
.ly-node span{font-size:12px; color:var(--muted)}
.ly-node.desk{border-color:var(--brand)}
.ly-node.desk small{color:var(--brand)}
.ly-wire{position:relative; height:28px; width:1px; margin:6px auto; background:var(--hair); overflow:hidden}
.ly-wire i{position:absolute; left:-1px; width:3px; height:12px; border-radius:2px; background:var(--brand); top:100%; opacity:0}
.layer.in .ly-wire i{animation:lyPulse 1.1s var(--ease-out) both}
.layer.in .ly-wire:nth-of-type(2) i{animation-delay:.25s}
.layer.in .ly-wire:nth-of-type(4) i{animation-delay:.75s}
.layer.in .ly-wire:nth-of-type(6) i{animation-delay:1.25s}
@keyframes lyPulse{0%{top:100%; opacity:0}20%{opacity:1}100%{top:-14px; opacity:0}}
@media (max-width:760px){ .ly-srcs{grid-template-columns:repeat(2,minmax(0,1fr))} .ly-xp{grid-template-columns:1fr} .ly-row3{grid-template-columns:1fr} .ly-row2{grid-template-columns:1fr} }
@media (prefers-reduced-motion:reduce){ .layer.in .ly-wire i{animation:none} }

/* 04: the activity, every step with its quote and its source */
.ctl{display:grid; gap:0; min-width:560px}
.cstep{display:grid; grid-template-columns:52px 104px minmax(0,1fr) auto; column-gap:14px; align-items:baseline;
  padding:13px 0; border-top:1px solid var(--hair-warm); opacity:0; transform:translateY(6px)}
.cstep:first-child{border-top:0; padding-top:2px}
.ctl.in .cstep{opacity:1; transform:none; transition:opacity var(--enter) var(--ease-out), transform var(--enter) var(--ease-out)}
.ctl.in .cstep:nth-child(2){transition-delay:.09s}.ctl.in .cstep:nth-child(3){transition-delay:.18s}.ctl.in .cstep:nth-child(4){transition-delay:.27s}.ctl.in .cstep:nth-child(5){transition-delay:.36s}.ctl.in .cstep:nth-child(6){transition-delay:.45s}
.cstep .ct{font-size:12.5px; color:var(--faint)}
.cstep .cw{font-size:11px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--muted)}
.cstep .ch{display:flex; flex-direction:column; gap:3px; font-size:14.5px; color:var(--ink-max); min-width:0}
.cstep .ch b{font-weight:600}
.cstep .cq{font-size:13.5px; color:var(--sub)}
.cstep .cs{font-size:12px; color:var(--faint); white-space:nowrap}
#ch-d .ctl-sum{margin-top:16px; padding-top:14px; border-top:1px solid var(--hair-warm); font-size:13.5px; color:var(--muted)}

/* 06: the first lines of the letter, as the agent drafted them */
.letter{margin-top:16px; padding:14px 16px; border:1px solid var(--hair); border-radius:10px; background:var(--surface);
  font-family:"Fraunces",Georgia,serif; font-size:15.5px; line-height:1.5; color:var(--sub)}
.letter p + p{margin-top:6px}
.letter .lt-to{color:var(--ink-max)}

#notthis{text-align:center}
@media (max-width:760px){
  .ctl{min-width:0}
  .cstep{grid-template-columns:44px minmax(0,1fr); row-gap:3px}
  .cstep .cw,.cstep .ch,.cstep .cs{grid-column:2}
  .cstep .cs{white-space:normal}
}
/* the lifted components keep their product width; the fit rule scales them down, never up */
.chapter .stage .device{width:min(900px,100%); margin:0 auto}
#ch-e .stage .device{width:min(760px,100%)}
#ch-c .stage .device{width:min(760px,100%)}
/* 05: the logged case shows its amount, not a delta */
#modcard .delta .to{font-size:22px}

/* THE WALKTHROUGH. The second film: a quiet room of its own after the decision */
.walk{min-height:var(--vph,100svh); display:flex; align-items:center; padding:clamp(40px,8vh,96px) 0; border-top:1px solid var(--hair); scroll-snap-align:start}
.walk .wrap{display:flex; flex-direction:column; align-items:center; text-align:center}
.walk .sub{margin-left:auto; margin-right:auto}
.wt{all:unset; box-sizing:border-box; cursor:pointer; position:relative; display:block; margin-top:clamp(22px,4vh,40px);
  width:min(1040px,100%); aspect-ratio:16/9; max-height:62vh; border-radius:14px; overflow:hidden; border:1px solid var(--hair); background:#0B0B0A}
.wt img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition:transform 1.2s var(--ease-out)}
.wt:hover img,.wt:focus-visible img{transform:scale(1.025)}
.wt:focus-visible{outline:2px solid var(--brand); outline-offset:4px}
.wt-play{position:absolute; left:50%; bottom:clamp(18px,4%,32px); transform:translateX(-50%); display:inline-flex; align-items:center; gap:10px;
  padding:11px 18px 11px 15px; border-radius:999px; background:rgba(250,248,244,.94); color:var(--ink-max); font-size:14px; font-weight:500}
.wt-play svg{width:12px; height:12px; color:var(--brand)}
.wm{position:fixed; inset:0; z-index:9000; background:rgba(11,11,10,.94); display:flex; flex-direction:column; align-items:center; justify-content:center;
  padding:max(16px,env(safe-area-inset-top)) max(16px,env(safe-area-inset-right)) max(16px,env(safe-area-inset-bottom)) max(16px,env(safe-area-inset-left));
  opacity:0; transition:opacity .45s ease}
.wm[hidden]{display:none}
.wm.on{opacity:1}
.wm-bar{width:min(1280px,100%); display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; color:rgba(255,255,255,.72); font-size:13px}
.wm-x{appearance:none; width:40px; height:40px; border-radius:50%; border:1px solid rgba(255,255,255,.22); background:transparent; color:#fff; cursor:pointer; display:flex; align-items:center; justify-content:center}
.wm-x svg{width:15px; height:15px; fill:none; stroke:currentColor; stroke-width:1.8; stroke-linecap:round}
.wm video{width:min(1280px,100%); max-height:calc(100svh - 110px); aspect-ratio:16/9; background:#000; border-radius:10px}
</style>
</head>'''
s = open(ROOT / 'index.html').read()
s = s.replace('</head>', CSS, 1)

WALK_JS = r'''<script>
/* on a phone the fit rule lets components flow at their own size; a lift is wider than the
   phone, so it is scaled to the column. transform, not zoom: WebKit applies zoom to the
   iframe's own viewport, and the desk inside would re-lay itself out at phone width. The
   holder takes the scaled size so the section's height follows. */
(function () {
  function size() {
    document.querySelectorAll('.stage').forEach(function (st) {
      var el = st.querySelector('.decide') || st.querySelector('.lift'); if (!el) { return; }
      var box = el.parentNode.classList.contains('liftbox') ? el.parentNode : null;
      if (innerWidth >= 761) { el.style.transform = ''; if (box) { box.style.width = box.style.height = ''; } return; }
      if (!box) { box = document.createElement('div'); box.className = 'liftbox'; el.parentNode.insertBefore(box, el); box.appendChild(el); }
      var w = el.offsetWidth, h = el.offsetHeight, k = Math.min(1, (st.clientWidth - 2) / w);
      el.style.transformOrigin = '0 0'; el.style.transform = 'scale(' + k.toFixed(4) + ')';
      box.style.width = Math.round(w * k) + 'px'; box.style.height = Math.round(h * k) + 'px';
    });
  }
  addEventListener('resize', size); document.addEventListener('DOMContentLoaded', size); size();
})();
</script>
<div class="jrail" id="jrail" aria-hidden="true"><i data-for="ch-a"><span>The request</span></i><i data-for="ch-b"><span>The desk</span></i><i data-for="ch-l"><span>The layer</span></i><i data-for="ch-c"><span>The checks</span></i><i data-for="ch-d"><span>The evidence</span></i><i data-for="ch-e"><span>One sentence</span></i><i data-for="ch-f"><span>The letter</span></i><i data-for="ch-g"><span>The decision</span></i></div>
<script>
/* the rail follows the chapter in the middle of the screen; it stands only between the hero and the walkthrough */
(function () {
  var rail = document.getElementById('jrail'); if (!rail) { return; }
  var marks = [].slice.call(rail.querySelectorAll('i')), ids = marks.map(function (m) { return m.dataset.for; });
  function tick() {
    var mid = innerHeight / 2, cur = -1, inBand = false;
    var a = document.getElementById('ch-a'), w = document.getElementById('walk');
    if (a && w) { inBand = a.getBoundingClientRect().top < mid && w.getBoundingClientRect().top > mid; }
    ids.forEach(function (id, i) { var e = document.getElementById(id); if (e && e.getBoundingClientRect().top <= mid) { cur = i; } });
    rail.classList.toggle('on', inBand && !document.documentElement.classList.contains('locked'));
    marks.forEach(function (m, i) { m.classList.toggle('done', i < cur); m.classList.toggle('now', i === cur); });
  }
  addEventListener('scroll', tick, { passive: true }); addEventListener('resize', tick); tick();
})();
</script>
<script>
/* the walkthrough: HLS, native in Safari, hls.js elsewhere, loaded only on open */
(function () {
  var open = document.getElementById('wtOpen'), wm = document.getElementById('wm'), v = document.getElementById('wmv'),
      x = document.getElementById('wmClose'), SRC = 'assets/walk/walkthrough.m3u8', ready = false;
  if (!open) { return; }
  function attach() {
    if (ready) { return Promise.resolve(); } ready = true;
    if (v.canPlayType('application/vnd.apple.mpegurl')) { v.src = SRC; return Promise.resolve(); }
    return new Promise(function (res) {
      var sc = document.createElement('script');
      sc.src = 'https://cdnjs.cloudflare.com/ajax/libs/hls.js/1.5.13/hls.min.js';
      sc.onload = function () { if (window.Hls && Hls.isSupported()) { var h = new Hls(); h.loadSource(SRC); h.attachMedia(v); } else { v.src = SRC; } res(); };
      sc.onerror = function () { v.src = SRC; res(); };
      document.head.appendChild(sc);
    });
  }
  function show() {
    var hv = document.getElementById('film-video'); if (hv && !hv.paused) { hv.pause(); }
    wm.hidden = false; document.documentElement.style.overflow = 'hidden';
    requestAnimationFrame(function () { wm.classList.add('on'); });
    attach().then(function () { var p = v.play(); if (p && p.catch) { p.catch(function () {}); } });
    x.focus();
  }
  function hide() { v.pause(); wm.classList.remove('on'); document.documentElement.style.overflow = ''; setTimeout(function () { wm.hidden = true; open.focus(); }, 450); }
  open.addEventListener('click', show); x.addEventListener('click', hide);
  wm.addEventListener('click', function (e) { if (e.target === wm) { hide(); } });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !wm.hidden) { hide(); } });
})();
</script>
</body>'''
s = s.replace('</body>', WALK_JS, 1)
open(ROOT / 'index.html', 'w').write(s)
print('layer ok')
