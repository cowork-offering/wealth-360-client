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
  + '\n      '.join([row('g-mail','Client email &middot; intake'), row('g-shield','UK Sanctions List &middot; screening'), row('g-payee','Payee check &middot; open banking'), row('g-id','Identity &middot; verification'), row('g-pin','Address &middot; postcode')]) + '\n    ')

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
    return f'<div class="cap"><p class="eyebrow chno"><b>{n:02d}</b><i>/</i>07</p><h2 class="head">{head}</h2><p class="sub">{sub}</p></div>'
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

# b. the desk
wl = [('JO', 'James Okafor', 'Money out &middot; general investment account', [('acc', 'Authorise')], '£3,000', 'to his account'),
      ('VB', 'Victor Bondarev', 'Money in &middot; possible sanctions match', [('warn', 'Decide')], '£22,000', 'held in suspense'),
      ('DE', 'David Ellison', 'Bereavement &middot; letter to the executor', [('acc', 'Review')], '3', 'accounts on hold'),
      ('PR', 'Priya Raman', 'Change of address &middot; email and water bill', [('good', 'Closed by agents')], '3 min', 'no person needed')]
rows = ''.join(f'<div class="wlrow rise" data-rise><span class="mono">{m}</span><span class="who"><b>{n}</b><span>{d}</span></span><span class="sts">' + ''.join(f'<span class="st {c}">{l}</span>' for c, l in st) + f'</span><span class="amt num"><b>{amt}</b><span>{sub}</span></span><span class="go" aria-hidden="true">&rarr;</span></div>' for m, n, d, st, amt, sub in wl)
kpis = [('With you', '5', '', '0', 'Authorise, decide, review'), ('Agents working', '4', '', '0', 'Moving on their own'), ('Waiting on client', '3', '', '0', 'Documents requested'), ('Completed', '6', '', '0', '2 by agents alone'), ('Agent time', '4', '', ' min', 'A case, in our runs'), ('Decided today', '3', '', '0', 'Each by name')]
kp = ''.join(f'<div class="kpi"><div class="l">{l}</div><div class="v{" warn" if l=="With you" else ""}" data-count="{v}" data-dec="0"{" data-post=\" min\"" if post==" min" else ""}>0</div><div class="s">{sub}</div></div>' for l, v, pre, post, sub in kpis)
body = f'<p class="eyebrow">Tuesday, 3 November<span class="dot">&middot;</span>Your book</p><h3 class="head" style="margin-top:12px; font-size:clamp(24px,3vw,36px)">Five cases need you today.</h3><div class="card kpis num" id="kpiband" style="margin-top:24px">{kp}</div><div class="wl" id="worklist" style="margin-top:22px">{rows}</div>'
CH.append(chapter('ch-b', 2, 'It knows what needs you, and what does not.', 'The desk reads Salesforce before you arrive. What needs a person stands apart from what the agents are moving on their own.', facts(('With you', '5', 'cases, each with its reason'), ('Agent time', '4 min', 'to gather and check a case'), ('The rest', 'Moving on its own, in plain view')), device('Wealth 360 &middot; The desk', body)))
CH.append(breath(1, 'breather-1.jpg', [('Every request, already ', 0), ('gathered', 1), ('.', 0)], ''))

# c. the checks resolve
rr = ''.join([row('g-sf', 'Salesforce &middot; client, accounts, KYC'), row('g-mail', 'Client email &middot; the request and its documents'), row('g-shield', 'UK Sanctions List &middot; screened'), row('g-payee', 'Payee check &middot; account confirmed'), row('g-id', 'Identity &middot; verified on file'), row('g-pin', 'Address &middot; postcode matched')])
chips = '<span class="chip"><span class="mk">&gt;</span>Wealth 360</span><span class="chip"><svg viewBox="0 0 19 19" aria-hidden="true"><use href="#g-memo"/></svg>Case agent</span><span class="chip"><svg viewBox="0 0 19 19" aria-hidden="true"><use href="#g-memo"/></svg>Review agent</span><span class="chip"><span class="mk" style="color:var(--faint)">&bull;</span>Wealth 360 Checks</span>'
body = f'<p style="font-size:14px;color:var(--muted);margin-bottom:16px">Worked the case, used 6 checks, cited every step</p><div class="runrows" id="railrows">{rr}</div><p class="striplbl">Two agents, two connectors, one record</p>'
CH.append(chapter('ch-c', 3, 'Every check, already run.', 'The client record, the sanctions list, the payee and the identity provider answer before the case reaches you.', facts(('Checks', '6', 'resolved before you open the case'), ('Resolved', 'Salesforce, UK Sanctions List, payee, identity, address, email'), ('Written back', 'Every result, on the case')), device('Wealth 360 &middot; Case 00001380', body), flip=True))

# d. every step cited (the care chapter's evidence)
steps = [('15:03', 'Case agent', 'Read the notification', '&ldquo;My mother, Margaret Ellison, died on 4 August.&rdquo;', 'Email from David Ellison'),
         ('15:04', 'Case agent', 'Found three accounts', 'General investment account, ISA, cash', 'Salesforce'),
         ('15:05', 'Salesforce', 'Recorded the death, held the accounts', 'Certificate on the case, family link on record', 'Fence passed'),
         ('15:06', 'Case agent', "Executor's identity on file", 'Passport, verified 3 June 2024', 'KYC profile'),
         ('15:07', 'Case agent', 'Drafted the letter, proposed a meeting', 'Three times on Thursday', 'Draft, not sent'),
         ('15:08', 'Review agent', 'Checked the case, passed', 'Six of six journey rules', 'Fresh context')]
sl = ''.join(f'<div class="cstep"><span class="ct num">{t}</span><span class="cw">{w}</span><span class="ch"><b>{h}</b><span class="cq">{q}</span></span><span class="cs">{src}</span></div>' for t, w, h, q, src in steps)
body = f'<div class="ctl" id="graph">{sl}</div><p class="ctl-sum" id="nodechip">11 steps, every one cited, in four minutes.</p>'
CH.append(chapter('ch-d', 4, 'Every step, cited.', 'The Case agent works the request one step at a time and quotes the source behind each one. A second agent checks it, blind to the first one&rsquo;s reasoning.', facts(('Steps', '11', 'each with its quote and source'), ('The check', 'A second agent, in a fresh context'), ('The fence', 'Enforced by Salesforce, in code')), device('Ellison &middot; Bereavement &middot; Activity', body)))

# e. one sentence
body = ('<div class="composer" style="min-height:88px; padding-bottom:44px"><div class="typed"><span id="asktype"></span><i class="caret"></i></div><div class="cmp-bar">'
        '<svg class="plus" width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><line x1="10" y1="4" x2="10" y2="16"/><line x1="4" y1="10" x2="16" y2="10"/></svg>'
        '<div class="pillbed" aria-hidden="true"><div class="p">Chat</div><div class="p on">Cowork</div></div><div class="modelmeta" aria-hidden="true">Opus 5.5<em>Medium</em></div>'
        f'<span class="sendbtn" id="asksend" aria-hidden="true">{CHEV}</span></div></div>'
        '<div class="modcard" id="modcard"><div><div class="fac">Case 00001382 &middot; Money out</div><div class="facm">James Okafor &middot; general investment account &middot; logged by phone</div></div><div class="delta"><span class="to">£3,000</span></div></div>'
        f'<p class="checked" id="checked">{TICK}<span>Client, account and payee found as you type. The Case agent picked it up within seconds.</span></p>')
CH.append(chapter('ch-e', 5, 'Say it in one sentence.', 'A call, a note, a letter in the post. Log it in a sentence and the agents start on it at once.', facts(('The request', '1', 'sentence, no form'), ('Picked up', 'Within seconds, by the Case agent'), ('The record', 'A standard case in Salesforce')), device('Wealth 360 &middot; Log a request', body), flip=True))
CH.append(breath(2, 'breather-2.jpg', [('Every family, given ', 0), ('time', 1), ('.', 0)], ''))

# f. the letter waits for you
secs = ['Read the notification', 'Identify the client and accounts', 'Record the death', 'Hold the accounts', 'Check the documents', "Confirm the executor's identity", 'Draft the condolence letter', 'Independent review', 'Your approval']
sr = ''.join(f'<div class="secrow" data-sec><span class="sst">{TICK}</span>{x}</div>' for x in secs)
body = (f'<div class="memohead"><span class="mk">Bereavement <span class="re">Letter</span></span></div><p class="draftline">Preparing the case for you: <b id="secn">0 of 9</b> steps</p><div class="seclist" id="seclist">{sr}</div>'
        '<div class="letter"><p class="lt-to">Dear Mr Ellison,</p><p>I was very sorry to hear of your mother&rsquo;s death. Her three accounts are now on hold, so nothing will leave them while you act for her estate&hellip;</p></div>'
        '<div class="attest"><span class="att-dot"></span><span><b>Agent-drafted</b> &middot; Waiting for your approval</span></div><div class="memoctrl"><span class="btn primary">Approve as drafted</span><span class="btn">Edit letter</span></div>')
CH.append(chapter('ch-f', 6, 'The letter writes itself, and waits for you.', 'Drafted in the firm&rsquo;s voice, with the facts from the record. Nothing reaches a client until a person approves it.', facts(('Prepared', '8 of 9', 'steps, before it reaches you'), ('The tone', 'Written for a family, not a file'), ('Sent', 'Only when you approve it')), device('Ellison &middot; Letter to the executor', body)))
CH.append(breath(3, 'breather-3.jpg', [('Agents prepare. People ', 0), ('decide', 1), ('.', 0)], ''))

# g. the decision
g0 = s.find('<section class="chapter" id="ch-g"'); g1 = s.find('</main>')
chg = s[g0:g1]
chg = re.sub(r'<div class="cap">.*?</div>\s*<div class="facts">.*?</div>\s*</div>', cap(7, 'You decide. Salesforce does the rest.', 'The plan is read back before anything moves. One confirmation, recorded against your name, and the record closes behind it.') + facts(('On the record', '5', 'writes, from one confirmation'), ('Confirmed by', 'A named person, never an agent'), ('The control', 'Staged, read back, then confirmed')), chg, count=1, flags=re.S)
plan = ["Keep Margaret Ellison&rsquo;s three accounts on hold, with her death recorded", "Send the condolence letter to David Ellison on the firm&rsquo;s letterhead", "Book the one-to-one on Thursday at 10:00, with David as the contact", "Record the decision on the case against Emma Collins"]
chg = re.sub(r'<p class="ph">Review and execute</p>.*?<div class="approvebar">', '<p class="ph">Review and confirm</p>' + ''.join(f'<div class="planrow"><span class="n">{i+1}</span><span>{p}</span></div>' for i, p in enumerate(plan)) + '\n          <div class="approvebar">', chg, count=1, flags=re.S)
chg = chg.replace('>Approve</button>', '>Confirm</button>')
chg = chg.replace('<span class="dt">Hartwell Precision Manufacturing LLC</span>', '<span class="dt">Ellison &middot; Bereavement</span>').replace('Package v4 &middot; executed 09:14', 'Confirmed by Emma Collins &middot; 15:12')
ex = [('Decision recorded on the case', 'Salesforce'), ('Three accounts held, death recorded', 'Financial Services Cloud'), ('Letter sent to David Ellison', 'Email'), ('One-to-one booked for Thursday', 'Calendar'), ('Every step written to the audit trail', 'Audit trail')]
ticks = re.findall(r'<div class="execrow" data-exec>(<svg.*?</svg>)', chg, flags=re.S)
chg = re.sub(r'(<div class="execrow" data-exec>.*?</div>\s*)+', ''.join(f'<div class="execrow" data-exec>{ticks[0]}{a}<span class="w">{w}</span></div>\n            ' for a, w in ex), chg, count=1, flags=re.S)
CH.append(chg)

# the walkthrough: a second film, seven minutes
CH.append('''<section class="walk" id="walk">
  <div class="wrap">
    <p class="eyebrow chno">The walkthrough<span class="dot">&middot;</span>7 minutes</p>
    <h2 class="head">One case, end to end.</h2>
    <p class="sub">What it is, what it is worth, how it is built, and a bereavement and a complaint worked live in the sandbox.</p>
    <button class="wt rise" data-rise type="button" id="wtOpen" aria-label="Play the seven minute walkthrough">
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
s = s[:a0] + '\n'.join(CH) + s[g1:]

# ---------- the end ----------
rep('assets/film/sf-plate.mp4', 'assets/film/end-plate.mp4'); rep('assets/film/sf-plate-poster.jpg', 'assets/film/end-plate.jpg')
rep('<p class="eyebrow endbrow">Dreamforce 2026</p>', '<p class="eyebrow endbrow">A private screening</p>')
s = re.sub(r'(<p class="endlock">.*?)<span>Credit 360</span>', r'\1<span>Wealth 360</span>', s, count=1, flags=re.S)
rep('<p class="endhead">Meet us at the booth.</p>', '<p class="endhead">Care, with time to give it.</p>')
s = re.sub(r'\s*<!-- the place, drawn.*?</aside>', '', s, count=1, flags=re.S)

# ---------- motion strings ----------
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
    row-gap:clamp(18px,3.4vh,40px);
  }
  .cap{align-self:end; justify-self:center; text-align:center; max-width:820px}
  .cap .sub{margin-left:auto; margin-right:auto}
  .stage{padding-inline:clamp(40px,10vw,180px)}
  .facts{align-self:start; justify-self:center; margin-top:0; display:flex; gap:0;
    width:min(980px,100%); border-top:1px solid var(--hair); padding-top:clamp(14px,2.2vh,22px)}
  .fact{flex:1 1 0; min-width:0; text-align:center; padding:0 18px; border-top:0; border-left:1px solid var(--hair)}
  .fact:first-child{border-left:0; padding-left:0}
  .fact:last-child{padding-right:0}
  .fact .fv{font-size:34px; margin-top:8px}
  .fact .fs{font-size:13.5px; margin-top:6px}
  .fact .fp{font-size:16px; margin-top:9px; line-height:1.34}
}
@media (max-width:1079.98px){ .cap{text-align:center} .cap .sub{margin-left:auto;margin-right:auto} .fact{text-align:center} }


/* THE TWIST. Same family as Credit 360, its own voice: a private office speaks in a serif.
   The chapter headlines, the hero line, the typed breathers and the close are set in Newsreader;
   the product's own surfaces stay in Inter, exactly as the desk draws them. */
.cap .head,.walk .head{font-family:"Newsreader",Georgia,serif; font-weight:400; letter-spacing:-.012em; line-height:1.08;
  font-size:clamp(32px,3.7vw,52px)}
.hero-line{font-family:"Newsreader",Georgia,serif; font-weight:400; letter-spacing:-.01em}
.breath-type{font-family:"Newsreader",Georgia,serif; font-weight:400; letter-spacing:-.012em}
.endhead{font-family:"Newsreader",Georgia,serif; font-weight:400; letter-spacing:-.01em}
#notthis{font-family:"Newsreader",Georgia,serif; font-weight:400; font-size:clamp(22px,2vw,30px)}
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
  font-family:"Newsreader",Georgia,serif; font-size:15.5px; line-height:1.5; color:var(--sub)}
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

WALK_JS = r'''<div class="jrail" id="jrail" aria-hidden="true"><i data-for="ch-a"><span>The request</span></i><i data-for="ch-b"><span>The desk</span></i><i data-for="ch-c"><span>The checks</span></i><i data-for="ch-d"><span>The evidence</span></i><i data-for="ch-e"><span>One sentence</span></i><i data-for="ch-f"><span>The letter</span></i><i data-for="ch-g"><span>The decision</span></i></div>
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
