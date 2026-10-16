"""Re-lay the 8 frames of the 9:16 project for a 1080x1920 portrait canvas.
Element ids are kept so the voice-synced GSAP timelines stay valid; only the
markup between </style> and <script> and the shared CSS sizes change.
Usage: python3 -I portrait.py <project_dir>"""
import re, sys, os

FR = os.path.join(sys.argv[1], "compositions", "frames")
SG = "font-family:'Space Grotesk';"


def hdr(n, eyebrow):
    return (f'<div class="x{n}-hdr"><div class="x{n}-pill">UASZ · Scolarité</div>'
            f'<div class="x{n}-eyebrow" id="x{n}-eyebrow">{eyebrow}</div></div>'
            f'<div class="x{n}-sp" style="flex:.55;"></div>')


def tail(n, pct):
    return (f'  <div class="x{n}-sp"></div></div>\n  <div class="x{n}-counter">{n} / 08</div>\n'
            f'  <div class="x{n}-prog" style="width:{pct}"></div>\n')


BODIES = {}

# 01 — relevé full width, then « Raté ? / Faux. » under it
rows = [("UE 1", "9", "12", ""), ("UE 2", "9", "8,5", "x01-neg"), ("UE 3", "6", "11", ""), ("UE 4", "6", "9", "x01-neg")]
r = ""
for i, (ue, cr, note, neg) in enumerate(rows):
    hl = ('<div id="x01-hl" style="position:absolute;left:-22px;right:-22px;top:6px;bottom:6px;background:rgba(220,38,38,.06);'
          'border:2.5px solid #dc2626;border-radius:12px;"></div>') if i == 1 else ""
    r += (f'<div id="x01-row{i}" style="position:relative;display:flex;justify-content:space-between;align-items:center;padding:30px 0;'
          f'border-top:1.5px solid rgba(30,43,250,.12);">{hl}'
          f'<span style="position:relative;{SG}font-weight:500;font-size:46px;">{ue} <span style="color:#737373;font-size:32px;">· {cr} crédits</span></span>'
          f'<span class="x01-num {neg}" style="position:relative;font-size:72px;">{note}</span></div>')
BODIES["01"] = (hdr("01", "Résultats · Semestre 1") +
    '\n  <div class="x01-body" id="x01-who" style="font-size:44px;color:#111;">Awa · L1 · UASZ</div>'
    '\n  <div class="x01-card" id="x01-releve" style="margin-top:36px;padding:40px 50px 20px;">'
    f'<div class="x01-eyebrow" style="color:#6b6b6b;font-size:26px;margin-bottom:14px;">Relevé de notes — Awa</div>{r}</div>'
    '\n  <div style="margin-top:90px;">'
    '<div class="x01-h1" id="x01-rate" style="color:#737373;position:relative;display:inline-block;">Raté ?'
    '<div id="x01-strike" style="position:absolute;left:-10px;right:-10px;top:52%;height:11px;background:#dc2626;border-radius:6px;transform-origin:left center;"></div></div>'
    '<div class="x01-h1" style="margin-top:10px;"><span class="x01-w" id="x01-faux">Faux.</span></div></div>\n' + tail("01", "12.5%"))

# 02 — title, then 4 horizontal UE bars whose width = credit weight
bars = ""
for i, (ue, cr, w, bg) in enumerate([("UE 1", 9, "100%", ".10"), ("UE 2", 9, "100%", ".10"), ("UE 3", 6, "66.7%", ".05"), ("UE 4", 6, "66.7%", ".05")]):
    bars += (f'<div class="x02-card" id="x02-b{i}" style="width:{w};height:170px;margin-top:24px;padding:0 40px;box-sizing:border-box;display:flex;'
             f'justify-content:space-between;align-items:center;background:rgba(30,43,250,{bg});transform-origin:left center;">'
             f'<div style="{SG}font-weight:600;font-size:50px;">{ue}</div>'
             f'<div id="x02-c{i}"><span class="x02-num" style="font-size:88px;">{cr}</span> <span class="x02-body">crédits</span></div></div>')
BODIES["02"] = (hdr("02", "Les bases") +
    '\n  <div class="x02-h2" id="x02-title">Un semestre = <span class="x02-w" id="x02-n30w"><span class="x02-num x02-w" id="x02-n30">30</span> crédits</span></div>'
    '\n  <div class="x02-body" id="x02-sub" style="margin-top:22px;">UE = unité d\'enseignement</div>'
    f'\n  <div style="margin-top:70px;">{bars}</div>'
    f'\n  <div id="x02-axis" style="margin-top:34px;text-align:right;{SG}font-weight:600;font-size:36px;color:#737373;">9 + 9 + 6 + 6 = 30 crédits</div>\n' + tail("02", "25%"))

# 03 — rule, then the UE card, then the compensation note under it
BODIES["03"] = (hdr("03", "Règle 1 · Valider une UE") +
    '\n  <div class="x03-h2" id="x03-title">Une UE est validée à <span class="x03-num x03-w" id="x03-seuil">10/20</span></div>'
    '\n  <div class="x03-card" id="x03-card" style="margin-top:80px;padding:50px 54px;">'
    f'<div style="{SG}font-weight:600;font-size:48px;">UE 3 — 2 matières</div>'
    '<div id="x03-ma" style="display:flex;justify-content:space-between;align-items:baseline;margin-top:44px;font-size:42px;"><span>Matière A</span><span class="x03-num x03-neg" style="font-size:64px;">7</span></div>'
    '<div id="x03-mb" style="display:flex;justify-content:space-between;align-items:baseline;margin-top:24px;font-size:42px;"><span>Matière B</span><span class="x03-num" style="font-size:64px;">13</span></div>'
    '<div id="x03-moy" style="display:flex;justify-content:space-between;align-items:center;margin-top:40px;padding-top:34px;border-top:2px solid rgba(30,43,250,.2);">'
    f'<span style="{SG}font-weight:600;font-size:44px;">Moyenne de l\'UE</span>'
    '<span><span class="x03-num" id="x03-avg" style="font-size:88px;">10</span> <span class="x03-pill" id="x03-ok" style="background:rgba(5,150,105,.12);color:#059669;margin-left:16px;vertical-align:middle;">Validée</span></span></div></div>'
    '\n  <div id="x03-side" style="margin-top:56px;"><div class="x03-body" style="font-size:46px;color:#111;font-weight:500;">Compensation entre matières</div>'
    '<div class="x03-body" style="margin-top:14px;">7 + 13, même coefficient → 10</div></div>\n' + tail("03", "37.5%"))

# 04 — question, then the balance: 4 columns (height = weight) on a beam
cols = ""
for i, (ue, note, w, neg, h) in enumerate([("UE 1", "12", 9, "", 540), ("UE 2", "8,5", 9, "x04-neg", 540), ("UE 3", "11", 6, "", 370), ("UE 4", "9", 6, "x04-neg", 370)]):
    border = "border-color:#dc2626;" if neg else ""
    cols += (f'<div class="x04-card" id="x04-b{i}" style="flex:{w};height:{h}px;padding:24px 20px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;{border}">'
             f'<div style="{SG}font-weight:600;font-size:38px;">{ue}</div>'
             f'<div><div class="x04-num {neg}" style="font-size:68px;line-height:1;">{note}</div>'
             f'<div class="x04-body" id="x04-p{i}" style="font-size:28px;margin-top:8px;">poids {w}</div></div></div>')
q = " ".join(f'<span class="x04-w" id="x04-q{i}">{w}</span>' for i, w in enumerate("Et si une UE est sous la moyenne ?".split()))
BODIES["04"] = (hdr("04", "Règle 2 · La compensation") +
    f'\n  <div class="x04-h2">{q}</div>'
    '\n  <div class="x04-body" id="x04-sub" style="margin-top:22px;">Moyenne <b style="color:#111;">pondérée par les crédits</b></div>'
    f'\n  <div style="position:relative;margin-top:110px;"><div style="display:flex;gap:16px;align-items:flex-end;">{cols}</div>'
    '<div id="x04-beam" style="height:12px;background:#111;border-radius:6px;margin-top:16px;transform-origin:center center;"></div>'
    '<div id="x04-pivot" style="width:0;height:0;margin:0 auto;border-left:48px solid transparent;border-right:48px solid transparent;border-bottom:72px solid #1e2bfa;"></div></div>\n'
    + tail("04", "50%"))

# 05 — 2x2 notes grid, formula, big result, stamp under it
ks = ""
for i, (ue, note, k, neg) in enumerate([("UE 1", "12", 9, ""), ("UE 2", "8,5", 9, "x05-neg"), ("UE 3", "11", 6, ""), ("UE 4", "9", 6, "x05-neg")]):
    ks += (f'<div class="x05-card" id="x05-k{i}" style="padding:28px 34px;display:flex;justify-content:space-between;align-items:baseline;">'
           f'<span style="{SG}font-weight:600;font-size:40px;">{ue}</span>'
           f'<span><span class="x05-num {neg}" style="font-size:64px;">{note}</span> <span class="x05-body" style="font-size:30px;">× {k}</span></span></div>')
terms = [("t0", "(12×9"), ("t1", "+ 8,5×9"), ("t2", "+ 11×6"), ("t3", "+ 9×6)"), ("t4", "÷ 30")]
f_ = " ".join(f'<span class="x05-w" id="x05-{a}">{b}</span>' for a, b in terms)
BODIES["05"] = (hdr("05", "Le calcul d'Awa") +
    f'\n  <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;">{ks}</div>'
    f'\n  <div style="{SG}font-weight:500;font-size:50px;line-height:1.35;text-align:center;margin-top:80px;color:#6b6b6b;">{f_}</div>'
    '\n  <div style="text-align:center;margin-top:40px;"><span class="x05-num x05-w" id="x05-res" style="font-size:300px;line-height:1;transform-origin:center center;">10,15</span></div>'
    f'\n  <div style="display:flex;justify-content:center;margin-top:56px;"><div id="x05-stamp" style="border:6px solid #059669;color:#059669;border-radius:18px;padding:26px 44px;{SG}font-weight:700;font-size:56px;line-height:1.2;text-align:center;">'
    '<div>SEMESTRE VALIDÉ</div><div style="font-size:40px;">30 crédits acquis</div></div></div>\n' + tail("05", "62.5%"))

# 06 — 2x2 locked cards, example + total stacked, title revealed last
cs = ""
for i, (ue, note, cr, ok) in enumerate([("UE 1", "13", 9, True), ("UE 2", "7", 9, False), ("UE 3", "11", 6, True), ("UE 4", "6", 6, False)]):
    on = (f'<div id="x06-on{i}" style="position:absolute;inset:-1.5px;border:3px solid #1e2bfa;background:rgba(30,43,250,.06);border-radius:14px;"></div>') if ok else ""
    lock = f'<span class="x06-lock" id="x06-l{i}"></span>' if ok else ""
    neg = "" if ok else "x06-neg"
    op = "" if ok else "opacity:.45;"
    cs += (f'<div class="x06-card" id="x06-c{i}" style="position:relative;height:350px;padding:38px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;{op}">{on}'
           f'<div style="position:relative;display:flex;justify-content:space-between;align-items:center;"><span style="{SG}font-weight:600;font-size:46px;">{ue}</span>{lock}</div>'
           f'<div style="position:relative;"><span class="x06-num {neg}" style="font-size:88px;">{note}</span> <span class="x06-body" style="font-size:32px;">· {cr} crédits</span></div></div>')
BODIES["06"] = (hdr("06", "Règle 3 · Semestre non validé") +
    '\n  <div class="x06-h2" id="x06-title">La <span class="x06-num">capitalisation</span></div>'
    '\n  <div class="x06-body" id="x06-sub" style="margin-top:22px;">UE validée = acquise à vie</div>'
    f'\n  <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:70px;">{cs}</div>'
    '\n  <div class="x06-body" id="x06-note" style="font-size:34px;margin-top:36px;">Exemple : moyenne 9,4 → semestre non validé</div>'
    f'\n  <div id="x06-tot" style="{SG}font-weight:600;font-size:52px;margin-top:26px;"><span class="x06-num">15</span> crédits acquis à vie</div>\n'
    + tail("06", "75%"))

# 07 — title, gauge full width with the 70 % mark, pill under it
BODIES["07"] = (hdr("07", "Bon à savoir · Passage en L2") +
    '\n  <div class="x07-h2" id="x07-title">Au moins <span class="x07-num x07-w" id="x07-n42">42</span> crédits sur 60</div>'
    '\n  <div class="x07-body" id="x07-sub" style="margin-top:22px;">70 % des crédits de L1</div>'
    '\n  <div style="position:relative;margin-top:300px;" id="x07-gauge">'
    '<div style="position:relative;height:96px;background:rgba(30,43,250,.08);border-radius:12px;overflow:hidden;">'
    '<div id="x07-fill" style="position:absolute;left:0;top:0;bottom:0;width:70%;background:#1e2bfa;transform-origin:left center;"></div>'
    '<div style="position:absolute;left:50%;top:0;bottom:0;width:4px;background:#fdfae7;"></div></div>'
    '<div id="x07-mark" style="position:absolute;left:70%;top:-50px;height:196px;width:5px;margin-left:-2px;background:#111;transform-origin:center top;"></div>'
    f'<div id="x07-markl" data-layout-allow-overflow style="position:absolute;left:70%;top:-136px;margin-left:-200px;width:400px;text-align:center;{SG}font-weight:700;font-size:48px;white-space:nowrap;">70 % = 42 crédits</div>'
    f'<div style="position:relative;height:44px;margin-top:26px;{SG}font-size:32px;color:#6b6b6b;">'
    '<span style="position:absolute;left:0;">0</span><span style="position:absolute;left:25%;margin-left:-120px;width:240px;text-align:center;white-space:nowrap;">Semestre 1</span>'
    '<span style="position:absolute;left:81%;margin-left:-90px;width:180px;text-align:center;white-space:nowrap;">Semestre 2</span><span style="position:absolute;right:0;">60</span></div>'
    '<div style="margin-top:170px;"><span class="x07-pill" id="x07-pass" style="font-size:40px;padding:18px 34px;">Passage conditionnel en L2</span></div></div>\n'
    + tail("07", "87.5%"))

# 08 — three stacked take-aways, source under them
ts = ""
for i, (big, txt) in enumerate([("10", "de moyenne pondérée par les crédits"), ("30", "crédits par semestre"), ("À vie", "tout ce qui est validé reste acquis")]):
    ts += (f'<div class="x08-card" id="x08-t{i}" style="height:310px;margin-top:{0 if i == 0 else 30}px;padding:0 48px;box-sizing:border-box;display:flex;align-items:center;gap:40px;">'
           f'<div class="x08-num" style="font-size:132px;line-height:1;min-width:{340 if i == 2 else 180}px;">{big}</div>'
           f'<div style="{SG}font-weight:500;font-size:42px;line-height:1.25;">{txt}</div></div>')
BODIES["08"] = (hdr("08", "À retenir") + f'\n  <div>{ts}</div>'
    '\n  <div id="x08-src" style="margin-top:70px;">'
    '<div class="x08-body" style="font-size:32px;">Source : Décret n° 2012-1114 du 12 octobre 2012<br>art. 9, 27 à 29</div>'
    f'<div style="{SG}font-weight:600;font-size:36px;margin-top:20px;">UASZ · Direction de la scolarité centrale</div></div>\n'
    + tail("08", "100%"))

CSS = [  # (selector suffix, new declaration block)
    ("stage", "position:absolute;inset:0;padding:150px 72px 340px 72px;display:flex;flex-direction:column;"),
    ("hdr", "display:flex;flex-direction:column;align-items:flex-start;gap:26px;"),
    ("eyebrow", "font-family:\"Space Grotesk\";font-weight:600;font-size:30px;letter-spacing:.08em;text-transform:uppercase;color:#1e2bfa;"),
    ("pill", "font-family:\"Space Grotesk\";font-weight:500;font-size:28px;color:#1e2bfa;background:rgba(30,43,250,.08);border-radius:100px;padding:12px 26px;display:inline-block;"),
    ("h1", "font-family:\"Space Grotesk\";font-weight:700;font-size:150px;line-height:1.02;letter-spacing:-.02em;"),
    ("h2", "font-family:\"Space Grotesk\";font-weight:600;font-size:92px;line-height:1.08;letter-spacing:-.02em;margin-top:36px;"),
    ("body", "font-size:42px;line-height:1.45;color:#6b6b6b;"),
    ("counter", "position:absolute;left:72px;bottom:40px;font-family:\"Space Grotesk\";font-weight:500;font-size:24px;letter-spacing:.05em;color:#737373;"),
    ("prog", "position:absolute;left:0;bottom:0;height:6px;background:#1e2bfa;"),
]

for name in sorted(os.listdir(FR)):
    n = name[:2]
    path = os.path.join(FR, name)
    html = open(path, encoding="utf8").read()
    for sel, decl in CSS:
        html, k = re.subn(rf"(\.x{n}-{sel})\{{[^}}]*\}}", lambda m: m.group(1) + "{" + decl + "}", html)
        assert k <= 1, (name, sel)
    html, k = re.subn(r'data-width="1920" data-height="1080"', 'data-width="1080" data-height="1920"', html)
    assert k == 1 or 'data-width="1080" data-height="1920"' in html, name
    m = re.search(r'(<div id="root"[^>]*>\n\s*<div id="x\d\d-bg"[^>]*></div>\n\s*<div class="x\d\d-stage">\n)(.*?)(</div>\n<script>)', html, re.S)
    assert m, name
    html = html[:m.start(2)] + "  " + BODIES[n] + html[m.start(3):]
    open(path, "w", encoding="utf8").write(html)
    print("✓", name)
