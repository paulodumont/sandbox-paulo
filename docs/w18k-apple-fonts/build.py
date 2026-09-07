# -*- coding: utf-8 -*-
import html, os
OUT = os.path.join(os.path.dirname(__file__), "w18k-apple-fonts.html")

THEMES = {
  "A": dict(name="Opção A · SF Pro", display="'SF Pro Display'", text="'SF Pro Text'", num="'SF Pro Text'", numdisp="'SF Pro Display'", brand="'SF Pro Display'", brandw="600", brandls="0.12em"),
  "B": dict(name="Opção B · New York + SF Pro", display="'New York Medium'", text="'SF Pro Text'", num="'SF Pro Text'", numdisp="'New York Large'", brand="'New York Medium'", brandw="600", brandls="0.10em"),
}

CSS = r"""
:root{color-scheme:light only;--ink:#1c1a17;--ink2:#5c5750;--ink3:#8a847b;--line:#e6e1d9;--bg:#f6f4f0;--panel:#ffffff;--gold:#a8862c;--gold2:#c9a94a;--goldbg:#f7f0dd;--green:#2f7d4f;--greenbg:#e5f2ea;--red:#a63b2f;--redbg:#f7e6e2;--warm:#fbf9f5}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:"SF Pro Text",-apple-system,system-ui,sans-serif;font-size:13px;line-height:1.45}
@page{size:A4 landscape;margin:0}
.page{width:1123px;height:794px;overflow:hidden;position:relative;page-break-after:always;background:var(--bg);padding:44px 52px}
.page:last-child{page-break-after:auto}
.foot{position:absolute;left:52px;right:52px;bottom:22px;display:flex;justify-content:space-between;font-size:10px;color:var(--ink3);letter-spacing:.06em;text-transform:uppercase;font-family:"SF Pro Text"}
h1{font-family:"New York Large";font-weight:600;font-size:44px;line-height:1.05;margin:0 0 14px;letter-spacing:-.01em}
h2{font-family:"SF Pro Display";font-weight:600;font-size:22px;margin:0 0 6px;letter-spacing:-.01em}
.kicker{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:600;margin-bottom:10px;font-family:"SF Pro Text"}
p{margin:0 0 10px;color:var(--ink2);font-size:14px;max-width:760px}
.rec{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--gold);padding:18px 22px;border-radius:8px;max-width:760px;margin-top:22px}
.rec b{color:var(--ink)}
.grid{display:grid;gap:10px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 16px}
.card .lbl{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);font-weight:600;margin-bottom:8px}
.spec{font-size:26px;line-height:1.15;margin:2px 0 2px;white-space:nowrap;color:var(--ink)}
.spec.sm{font-size:14px;white-space:normal;color:var(--ink2)}
.spec.nums{font-size:22px;letter-spacing:.01em}
.use{font-size:11.5px;color:var(--ink3);margin-top:5px}
.tnum{font-variant-numeric:tabular-nums}
.pnum{font-variant-numeric:proportional-nums}
table.cmp{border-collapse:collapse;width:100%}
table.cmp td,table.cmp th{padding:5px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:middle}
table.cmp th{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);font-weight:600}
.r{text-align:right !important}
.tag{display:inline-block;font-size:10px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;padding:3px 8px;border-radius:999px;background:var(--goldbg);color:var(--gold)}

/* ---------- screen mockup ---------- */
.screen{width:1019px;height:632px;background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;box-shadow:0 8px 30px rgba(28,26,23,.08);font-family:var(--f-text);color:var(--ink)}
.screen .side{width:200px;background:#1e1b17;color:#d9d2c5;padding:22px 18px;display:flex;flex-direction:column}
.screen .brand{font-family:var(--f-brand);font-weight:var(--f-brandw);letter-spacing:var(--f-brandls);font-size:16px;color:#fff;margin-bottom:28px}
.screen .brand small{display:block;font-family:var(--f-text);font-weight:400;letter-spacing:.14em;font-size:9px;color:#9a917f;margin-top:4px;text-transform:uppercase}
.screen .nav a{display:block;padding:8px 10px;border-radius:6px;font-size:13px;color:#b9b1a2;margin-bottom:2px;font-family:var(--f-text)}
.screen .nav a.on{background:rgba(255,255,255,.08);color:#fff;font-weight:600}
.screen .side .who{margin-top:auto;font-size:11px;color:#9a917f}
.screen .main{flex:1;display:flex;flex-direction:column;min-width:0}
.screen .top{height:56px;border-bottom:1px solid var(--line);display:flex;align-items:center;padding:0 24px;gap:14px}
.screen .top .search{flex:1;height:32px;border:1px solid var(--line);border-radius:8px;background:var(--warm);display:flex;align-items:center;padding:0 12px;font-size:12px;color:var(--ink3)}
.screen .top .btn{height:32px;padding:0 14px;border-radius:8px;background:var(--ink);color:#fff;display:flex;align-items:center;font-size:12px;font-weight:600;font-family:var(--f-text)}
.screen .top .btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line)}
.screen .body{padding:22px 24px;flex:1;overflow:hidden}
.screen .ttl{font-family:var(--f-display);font-weight:600;font-size:26px;letter-spacing:-.01em;line-height:1.1;margin:0}
.screen .sub{font-size:12px;color:var(--ink3);margin-top:4px}
.screen .kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:14px 0}
.screen .kpi{border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:var(--panel)}
.screen .kpi .k{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);font-weight:600}
.screen .kpi .v{font-family:var(--f-numdisp);font-weight:600;font-size:22px;white-space:nowrap;letter-spacing:-.01em;margin-top:6px;font-variant-numeric:tabular-nums;color:var(--ink)}
.screen .kpi .d{font-size:11px;margin-top:4px;font-variant-numeric:tabular-nums}
.screen .kpi .d.up{color:var(--green)}
.screen .kpi .d.dn{color:var(--red)}
.screen .two{display:grid;grid-template-columns:minmax(0,1.9fr) minmax(0,1fr);gap:14px}
.screen .box{border:1px solid var(--line);border-radius:10px;background:var(--panel);overflow:hidden}
.screen .box .bh{padding:12px 16px;border-bottom:1px solid var(--line);font-weight:600;font-size:13px;display:flex;justify-content:space-between;align-items:center;font-family:var(--f-text)}
.screen .box .bh span.l{font-size:11px;color:var(--ink3);font-weight:500}
.screen table.t{width:100%;border-collapse:collapse;font-size:12px}
.screen table.t th{font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);text-align:left;padding:7px 10px;white-space:nowrap;border-bottom:1px solid var(--line);font-weight:600}
.screen table.t td{padding:8px 10px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;border-bottom:1px solid var(--line);vertical-align:middle;font-variant-numeric:tabular-nums}
.screen table.t tr:last-child td{border-bottom:0}
.screen .num{font-family:var(--f-num);font-variant-numeric:tabular-nums}
.screen .mono{font-family:"SF Mono";font-size:11px;letter-spacing:0;color:var(--ink2)}
.screen .pill{display:inline-block;font-size:10px;font-weight:600;padding:2px 8px;border-radius:999px;letter-spacing:.02em}
.screen .pill.ok{background:var(--greenbg);color:var(--green)}
.screen .pill.wait{background:var(--goldbg);color:var(--gold)}
.screen .pill.no{background:var(--redbg);color:var(--red)}
.screen .pill.gray{background:#efece6;color:var(--ink2)}
.screen .bars{display:flex;align-items:flex-end;gap:6px;height:110px;padding:14px 16px 8px}
.screen .bars i{flex:1;display:block;background:var(--gold2);border-radius:3px 3px 0 0;opacity:.9}
.screen .bars i.hi{background:var(--gold)}
.screen .axis{display:flex;justify-content:space-between;padding:0 16px 10px;font-size:10px;color:var(--ink3);font-variant-numeric:tabular-nums}
/* product */
.screen .phead{display:flex;align-items:flex-start;justify-content:space-between;gap:20px}
.screen .cols{display:grid;grid-template-columns:240px minmax(0,1fr) 270px;gap:14px;margin-top:14px}
.screen .img{height:210px;border-radius:10px;background:linear-gradient(135deg,#efe9dc,#e2d8c2);display:flex;align-items:center;justify-content:center;color:var(--gold);font-family:var(--f-display);font-size:14px;letter-spacing:.1em}
.screen .thumbs{display:flex;gap:8px;margin-top:8px}
.screen .thumbs i{flex:1;height:54px;border-radius:6px;background:#eee8dc;display:block}
.screen dl{margin:0;display:grid;grid-template-columns:1fr 1fr;gap:0 16px}
.screen dl div{padding:7px 0;border-bottom:1px solid var(--line)}
.screen dt{font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);font-weight:600}
.screen dd{margin:3px 0 0;font-size:13px;font-variant-numeric:tabular-nums}
.screen .price{font-family:var(--f-numdisp);font-weight:600;font-size:28px;white-space:nowrap;letter-spacing:-.01em;font-variant-numeric:tabular-nums}
.screen .price small{font-family:var(--f-text);font-size:12px;font-weight:500;color:var(--ink3);letter-spacing:0;margin-left:6px}
/* customer */
.screen .avatar{width:56px;height:56px;border-radius:50%;background:var(--goldbg);color:var(--gold);display:flex;align-items:center;justify-content:center;font-family:var(--f-display);font-weight:600;font-size:20px}
.screen .chead{display:flex;align-items:center;gap:16px}
.screen .meta{font-size:12px;color:var(--ink2);margin-top:3px;font-variant-numeric:tabular-nums}
.screen .meta b{color:var(--ink);font-weight:600}
/* form */
.screen .form{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px 14px;margin-top:4px}
.screen .fld label{display:block;font-size:11px;font-weight:600;color:var(--ink2);margin-bottom:3px;letter-spacing:.02em}
.screen .fld .in{height:30px;border:1px solid var(--line);border-radius:8px;background:#fff;display:flex;align-items:center;padding:0 12px;font-size:13px;color:var(--ink);font-variant-numeric:tabular-nums}
.screen .fld .in.ph{color:var(--ink3)}
.screen .fld.w2{grid-column:span 2}
.screen .fld.w3{grid-column:span 3}
.screen .sect{font-family:var(--f-display);font-weight:600;font-size:15px;margin:8px 0 2px;grid-column:span 3;padding-top:10px;border-top:1px solid var(--line)}
.screen .sect.first{border-top:0;padding-top:0;margin-top:2px}
.screen .actions{display:flex;justify-content:flex-end;gap:10px;margin-top:16px}
.screen .b{height:32px;padding:0 16px;border-radius:8px;display:flex;align-items:center;font-size:13px;font-weight:600;font-family:var(--f-text)}
.screen .b.pri{background:var(--ink);color:#fff}
.screen .b.sec{border:1px solid var(--line);color:var(--ink)}
.screen .b.gold{background:var(--gold);color:#fff}
"""

def theme_style(t):
    return f'style="--f-display:{t["display"]};--f-text:{t["text"]};--f-num:{t["num"]};--f-numdisp:{t["numdisp"]};--f-brand:{t["brand"]};--f-brandw:{t["brandw"]};--f-brandls:{t["brandls"]}"'

def side(active):
    items = ["Dashboard","Products","Customers","Orders","Inventory","Reports"]
    nav = "".join(f'<a class="{"on" if i==active else ""}">{i}</a>' for i in items)
    return f'''<div class="side"><div class="brand">W18K<small>Fine Jewelry 18K</small></div><div class="nav">{nav}</div><div class="who">Paulo · Admin</div></div>'''

def top(btn="New order", ghost=None):
    g = f'<div class="btn ghost">{ghost}</div>' if ghost else ""
    return f'<div class="top"><div class="search">Search products, customers, orders…</div>{g}<div class="btn">{btn}</div></div>'

def dashboard(t):
    bars = [42,55,48,70,64,80,58,92,74,88,100,86]
    b = "".join(f'<i style="height:{h}%" class="{"hi" if h==100 else ""}"></i>' for h in bars)
    rows = [
      ("#10482","Mariana Costa","Yellow Gold Bracelet","R$ 8.940,00","Paid"),
      ("#10481","Ricardo Almeida","Diamond Solitaire Ring","R$ 21.500,00","Pending"),
      ("#10480","Beatriz Nunes","Pearl Drop Earrings","R$ 3.280,00","Paid"),
      ("#10479","Fernanda Lima","Rose Gold Chain 45 cm","R$ 5.120,00","Shipped"),
      ("#10478","João P. Silva","Emerald Pendant","R$ 12.760,00","Cancelled"),
      ("#10477","Camila Rocha","Wedding Band Set","R$ 9.870,00","Paid"),
    ]
    pill = {"Paid":"ok","Pending":"wait","Shipped":"gray","Cancelled":"no"}
    tr = "".join(f'<tr><td class="mono">{o}</td><td>{c}</td><td>{p}</td><td class="r num">{v}</td><td><span class="pill {pill[s]}">{s}</span></td></tr>' for o,c,p,v,s in rows)
    return f'''<div class="screen" {theme_style(t)}>{side("Dashboard")}<div class="main">{top()}
<div class="body"><div class="ttl">Good morning, Paulo</div><div class="sub">Monday, 7 September 2026 · Store: São Paulo Flagship</div>
<div class="kpis">
<div class="kpi"><div class="k">Revenue · Sep</div><div class="v">R$ 148.920,00</div><div class="d up">+12,4% vs Aug</div></div>
<div class="kpi"><div class="k">Orders</div><div class="v">312</div><div class="d up">+38 vs Aug</div></div>
<div class="kpi"><div class="k">Average ticket</div><div class="v">R$ 4.772,00</div><div class="d dn">−1,8% vs Aug</div></div>
<div class="kpi"><div class="k">Gold in stock</div><div class="v">6.418,5 g</div><div class="d up">18K · 22 SKUs low</div></div>
</div>
<div class="two">
<div class="box"><div class="bh">Recent orders <span class="l">Last 24 hours</span></div><table class="t" style="table-layout:fixed"><colgroup><col style="width:62px"><col style="width:108px"><col><col style="width:94px"><col style="width:80px"></colgroup><tr><th>Order</th><th>Customer</th><th>Item</th><th class="r">Total</th><th>Status</th></tr>{tr}</table></div>
<div class="box"><div class="bh">Sales by month <span class="l">12 months</span></div><div class="bars">{b}</div><div class="axis"><span>Oct</span><span>Dec</span><span>Feb</span><span>Apr</span><span>Jun</span><span>Aug</span></div>
<table class="t"><tr><th>Top categories</th><th class="r">Share</th></tr><tr><td>Rings</td><td class="r num">38,2%</td></tr><tr><td>Necklaces</td><td class="r num">24,7%</td></tr><tr><td>Earrings</td><td class="r num">19,1%</td></tr><tr><td>Bracelets</td><td class="r num">18,0%</td></tr></table></div>
</div></div></div></div>'''

def product(t):
    hist = [("07 Sep 2026","R$ 21.500,00","R$ 618,40"),("21 Aug 2026","R$ 20.900,00","R$ 604,10"),("03 Jul 2026","R$ 19.750,00","R$ 571,20"),("15 May 2026","R$ 19.750,00","R$ 566,90")]
    tr = "".join(f'<tr><td>{d}</td><td class="r num">{p}</td><td class="r num">{g}</td></tr>' for d,p,g in hist)
    return f'''<div class="screen" {theme_style(t)}>{side("Products")}<div class="main">{top("Save changes","Duplicate")}
<div class="body"><div class="phead"><div><div class="ttl">Diamond Solitaire Ring 0.50 ct</div><div class="sub"><span class="mono">SKU W18K-RG-00417</span> &nbsp;·&nbsp; Rings &nbsp;·&nbsp; <span class="pill ok">Active</span></div></div>
<div style="text-align:right"><div class="price">R$ 21.500,00<small>retail</small></div><div class="meta">Cost <b class="num">R$ 11.240,00</b> &nbsp;·&nbsp; Margin <b class="num">47,7%</b></div></div></div>
<div class="cols">
<div><div class="img">W18K</div><div class="thumbs"><i></i><i></i><i></i><i></i></div></div>
<div class="box"><div class="bh">Specifications</div><div style="padding:4px 16px 10px"><dl>
<div><dt>Metal</dt><dd>18K Yellow Gold · 750</dd></div><div><dt>Gold weight</dt><dd class="num">3,85 g</dd></div>
<div><dt>Main stone</dt><dd>Diamond, round</dd></div><div><dt>Carat</dt><dd class="num">0,50 ct</dd></div>
<div><dt>Clarity / Color</dt><dd>VS1 / G</dd></div><div><dt>Certificate</dt><dd class="mono">GIA 2215478930</dd></div>
<div><dt>Ring size</dt><dd class="num">14 – 22 (BR)</dd></div><div><dt>Setting</dt><dd>4-prong</dd></div>
<div><dt>Supplier</dt><dd>Atelier Rocha</dd></div><div><dt>Lead time</dt><dd class="num">12 days</dd></div>
</dl></div></div>
<div><div class="box"><div class="bh">Stock</div><table class="t"><tr><th>Store</th><th class="r">Qty</th></tr><tr><td>São Paulo Flagship</td><td class="r num">3</td></tr><tr><td>Rio · Ipanema</td><td class="r num">1</td></tr><tr><td>Online</td><td class="r num">2</td></tr><tr><td><b>Total</b></td><td class="r num"><b>6</b></td></tr></table></div>
<div class="box" style="margin-top:14px"><div class="bh">Price history</div><table class="t"><tr><th>Date</th><th class="r">Retail</th><th class="r">Gold /g</th></tr>{tr}</table></div></div>
</div></div></div></div>'''

def customer(t):
    rows = [("#10481","07 Sep 2026","Diamond Solitaire Ring 0.50 ct","R$ 21.500,00","Pending"),("#10233","14 Jun 2026","18K Yellow Gold Bracelet","R$ 8.940,00","Paid"),("#09871","02 Mar 2026","Pearl Drop Earrings","R$ 3.280,00","Paid"),("#09402","19 Dec 2025","18K Rose Gold Chain 45 cm","R$ 5.120,00","Paid")]
    pill = {"Paid":"ok","Pending":"wait"}
    tr = "".join(f'<tr><td class="mono">{o}</td><td class="num">{d}</td><td>{p}</td><td class="r num">{v}</td><td><span class="pill {pill[s]}">{s}</span></td></tr>' for o,d,p,v,s in rows)
    return f'''<div class="screen" {theme_style(t)}>{side("Customers")}<div class="main">{top("New order","Edit")}
<div class="body"><div class="chead"><div class="avatar">RA</div><div><div class="ttl">Ricardo Almeida</div><div class="meta"><span class="num">+55 11 98765-4321</span> &nbsp;·&nbsp; ricardo.almeida@email.com &nbsp;·&nbsp; São Paulo, SP &nbsp;·&nbsp; <span class="pill wait">VIP</span></div></div></div>
<div class="kpis">
<div class="kpi"><div class="k">Lifetime value</div><div class="v">R$ 48.710,00</div><div class="d">5 orders</div></div>
<div class="kpi"><div class="k">Average ticket</div><div class="v">R$ 9.742,00</div><div class="d up">Above store avg</div></div>
<div class="kpi"><div class="k">Last purchase</div><div class="v">07 Sep 2026</div><div class="d">Diamond Solitaire Ring</div></div>
<div class="kpi"><div class="k">Customer since</div><div class="v">Sep 2025</div><div class="d">12 months</div></div>
</div>
<div class="two">
<div class="box"><div class="bh">Orders <span class="l">Latest</span></div><table class="t" style="table-layout:fixed"><colgroup><col style="width:64px"><col style="width:96px"><col><col style="width:96px"><col style="width:82px"></colgroup><tr><th>Order</th><th>Date</th><th>Item</th><th class="r">Total</th><th>Status</th></tr>{tr}</table></div>
<div class="box"><div class="bh">Profile</div><div style="padding:4px 16px 10px"><dl style="grid-template-columns:1fr">
<div><dt>CPF</dt><dd class="num">123.456.789-00</dd></div><div><dt>Birth date</dt><dd class="num">14 Mar 1979</dd></div>
<div><dt>Ring size</dt><dd class="num">19 (BR)</dd></div><div><dt>Preferred metal</dt><dd>Yellow gold 18K</dd></div>
<div><dt>Address</dt><dd>Rua Oscar Freire, 1200 · Jardins<br>São Paulo, SP · <span class="num">01426-001</span></dd></div></dl></div></div>
</div></div></div></div>'''

def form(t):
    def f(label, val="", ph=False, w=""):
        return f'<div class="fld {w}"><label>{label}</label><div class="in {"ph" if ph else ""}">{val}</div></div>'
    return f'''<div class="screen" {theme_style(t)}>{side("Customers")}<div class="main">{top("Save customer","Cancel")}
<div class="body"><div class="ttl">New customer</div><div class="sub">Customers / New</div>
<div class="form">
<div class="sect first">Identity</div>
{f("Full name","Mariana Costa Ferreira")}{f("CPF","987.654.321-00")}{f("Birth date","22 / 08 / 1986")}
{f("Email","mariana.ferreira@email.com")}{f("Phone","+55 11 91234-5678")}{f("Preferred contact","WhatsApp")}
<div class="sect">Address</div>
{f("Street","Alameda Santos, 1800","", "w2")}{f("Number / Unit","1800 · apt 142")}
{f("Neighborhood","Cerqueira César")}{f("City","São Paulo")}{f("State / ZIP","SP · 01418-200")}
<div class="sect">Preferences</div>
{f("Ring size","16 (BR)")}{f("Preferred metal","Yellow gold 18K")}{f("Segment","VIP")}
</div>
<div class="actions"><div class="b sec">Cancel</div><div class="b gold">Save customer</div></div>
</div></div></div>'''

def page(inner, foot_r=""):
    return f'<section class="page">{inner}<div class="foot"><span>W18K · Tipografia Apple</span><span>{foot_r}</span></div></section>'

# ---------- pages ----------
pages = []

pages.append(page('''
<div class="kicker">W18K · Sistema interno</div>
<h1>Fontes da Apple<br>aplicadas às telas da W18K</h1>
<p>Comparativo visual das famílias tipográficas que a Apple usa no iOS e no macOS, aplicadas ao Dashboard, à tela de Produto, à tela de Cliente e ao cadastro de Cliente. Os dados nas telas são ilustrativos.</p>
<div class="rec"><div class="kicker">Recomendação</div>
<p><b>Opção A · SF Pro</b> em todo o sistema: <b>SF Pro Display Semibold</b> nos títulos e valores grandes, <b>SF Pro Text</b> no corpo, com <b>números tabulares</b> ativados em KPIs, tabelas e formulários. <b>SF Mono</b> apenas em SKU, pedidos e certificados.</p>
<p style="margin:0">A Opção B (New York nos títulos) dá um ar mais "joalheria" e vale para o site e para materiais de cliente. Para uso operacional, todo dia, a A é mais legível e mais rápida de ler.</p></div>
<div style="margin-top:26px;display:flex;gap:10px"><span class="tag">SF Pro Text</span><span class="tag">SF Pro Display</span><span class="tag">SF Pro Rounded</span><span class="tag">SF Mono</span><span class="tag">New York</span></div>
''', "01"))

# specimens
def specimen(fam, w, use, sample="Diamond Solitaire Ring 0.50 ct", nums="0123456789 R$ 21.500,00", extra=""):
    return f'''<div class="card"><div class="lbl">{fam.strip(chr(39))}</div>
<div class="spec" style="font-family:{fam};font-weight:{w}">{sample}</div>
<div class="spec sm" style="font-family:{fam};font-weight:400">The quick brown fox jumps over the lazy dog · ÁÉÍÓÚÇÃÕ áéíóúçãõ</div>
<div class="spec nums tnum" style="font-family:{fam};font-weight:500">{nums}</div>
<div class="use">{use}</div></div>'''

pages.append(page('''
<div class="kicker">As famílias</div>
<h2>O que a Apple usa e onde</h2>
<div class="grid" style="grid-template-columns:1fr 1fr;margin-top:8px">
''' + specimen("'SF Pro Text'", 600, "Corpo de texto, tabelas, formulários, botões. Fonte padrão de iOS e macOS abaixo de 20 pt.") +
     specimen("'SF Pro Display'", 600, "Títulos, valores de KPI, preços grandes. Mesma família, desenhada para tamanhos acima de 20 pt.") +
     specimen("'SF Pro Rounded'", 600, "Apple Watch, Saúde, Fitness. Mais amigável, menos formal. Não combina com joalheria de luxo.") +
     specimen("'SF Mono'", 500, "Xcode, Terminal. Cada caractere tem a mesma largura. Ideal para SKU, número de pedido, certificado GIA.", nums="W18K-RG-00417 · GIA 2215478930") +
     specimen("'New York Medium'", 600, "Apple Books, Apple News, títulos editoriais. Serifa elegante. Boa para títulos, nome de produto e materiais de cliente.") +
'''<div class="card" style="background:var(--goldbg);border-color:#e9dcb4"><div class="lbl">Onde cada uma entra na W18K</div>
<table class="cmp"><tr><th>Elemento</th><th>Fonte</th><th>Peso</th></tr>
<tr><td>Título de tela, preço, KPI</td><td>SF Pro Display</td><td>Semibold 600</td></tr>
<tr><td>Texto, tabelas, campos, botões</td><td>SF Pro Text</td><td>Regular 400 / Semibold 600</td></tr>
<tr><td>Rótulos pequenos (caixa alta)</td><td>SF Pro Text</td><td>Semibold 600, 10–11 px</td></tr>
<tr><td>SKU, pedido, certificado</td><td>SF Mono</td><td>Regular 400</td></tr>
<tr><td>Título editorial (Opção B)</td><td>New York Medium</td><td>Semibold 600</td></tr></table></div>
</div>''', "02"))

# numbers page
fams = [("'SF Pro Text'",500,'SF Pro Text · Medium'),("'SF Pro Display'",600,'SF Pro Display · Semibold'),("'SF Pro Rounded'",600,'SF Pro Rounded · Semibold'),("'SF Mono'",500,'SF Mono · Medium'),("'New York Medium'",600,'New York Medium · Semibold')]
big = "".join(f'<tr><td style="width:150px;color:var(--ink3);font-size:10px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;line-height:1.3">{n}</td><td class="tnum" style="font-family:{f};font-weight:{w};font-size:22px;padding:6px 8px;white-space:nowrap">R$ 148.920,00 &nbsp; 6.418,5 g &nbsp; 0,50 ct<div style="font-size:15px;color:var(--ink2);font-weight:400;margin-top:2px;letter-spacing:.04em">0O &nbsp; 1lI &nbsp; 5S &nbsp; 8B &nbsp; 6b &nbsp; 3E &nbsp; 2Z</div></td></tr>' for f,w,n in fams)
prices = ["R$ 21.500,00","R$ 1.111,11","R$ 8.940,00","R$ 777,77","R$ 12.760,00"]
def col(cls, fam, w=500, size=15):
    return "".join(f'<div class="{cls}" style="font-family:{fam};font-weight:{w};font-size:{size}px;text-align:right;padding:3px 0;border-bottom:1px solid var(--line)">{p}</div>' for p in prices)
pages.append(page(f'''
<div class="kicker">Números</div>
<h2>Legibilidade dos algarismos</h2>
<p>Todas as fontes SF têm <b>números tabulares</b> (cada dígito com a mesma largura). Isso alinha colunas de preço e peso sem esforço e evita confusão entre 1, l e I, e entre 0 e O.</p>
<div class="grid" style="grid-template-columns:minmax(0,1fr) 330px;margin-top:8px;align-items:start">
<div class="card" style="padding:6px 18px"><table class="cmp">{big}</table></div>
<div class="grid" style="grid-template-columns:1fr 1fr;gap:10px;align-content:start">
<div class="card"><div class="lbl">SF Pro · proporcional</div>{col("pnum","'SF Pro Text'")}</div>
<div class="card" style="border-color:var(--gold2)"><div class="lbl" style="color:var(--gold)">SF Pro · tabular</div>{col("tnum","'SF Pro Text'")}</div>
<div class="card"><div class="lbl">SF Mono</div>{col("tnum","'SF Mono'",500,13)}</div>
<div class="card"><div class="lbl">New York · tabular</div>{col("tnum","'New York Medium'",600)}</div>
</div></div>
<div class="rec" style="max-width:100%;margin-top:14px"><b>Para fixar mais legível:</b> SF Pro Text com <b>tabular-nums</b> em todas as tabelas e campos, peso Medium 500 nos valores; SF Pro Display Semibold 600 nos KPIs e preços em destaque; SF Mono só em códigos. Rounded fica menos preciso em joalheria e New York, apesar de bonita, perde clareza em tabelas densas.</div>
''', "03"))

n = 4
for label, fn in [("Dashboard",dashboard),("Product",product),("Customer",customer),("New customer",form)]:
    for k in ("A","B"):
        t = THEMES[k]
        pages.append(page(f'<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:10px"><div><div class="kicker">{label}</div><h2 style="margin:0">{t["name"]}</h2></div><div style="font-size:12px;color:var(--ink3)">Títulos {t["display"].strip(chr(39))} · Texto SF Pro Text · Números tabulares · Códigos SF Mono</div></div>{fn(t)}', f"{n:02d}"))
        n += 1

pages.append(page('''
<div class="kicker">Implementação</div>
<h2>Como aplicar no sistema</h2>
<p>No Mac, iPhone e iPad as fontes já estão no aparelho e o navegador usa a SF Pro e a New York nativas. No Windows e no Android elas não existem e a licença da Apple não permite embutir os arquivos no site, então o sistema cai para a fonte de reserva. A mais parecida com a SF Pro é a <b>Inter</b> (gratuita).</p>
<div class="grid" style="grid-template-columns:1fr 1fr;margin-top:10px">
<div class="card"><div class="lbl">CSS · Opção A</div><pre style="font-family:'SF Mono';font-size:12px;line-height:1.6;margin:0;color:var(--ink)">:root {
  --font-text: -apple-system, "SF Pro Text",
               "Inter", system-ui, sans-serif;
  --font-display: -apple-system, "SF Pro Display",
               "Inter", system-ui, sans-serif;
  --font-mono: ui-monospace, "SF Mono",
               "JetBrains Mono", monospace;
}
body       { font-family: var(--font-text);
             font-variant-numeric: tabular-nums; }
h1, h2, .kpi-value, .price
           { font-family: var(--font-display);
             font-weight: 600; letter-spacing: -0.01em; }
.sku, .order-id, .certificate
           { font-family: var(--font-mono); }</pre></div>
<div class="card"><div class="lbl">CSS · Opção B (títulos)</div><pre style="font-family:'SF Mono';font-size:12px;line-height:1.6;margin:0;color:var(--ink)">:root {
  --font-title: ui-serif, "New York",
                "Source Serif 4", Georgia, serif;
}
h1, h2, .product-name, .customer-name
           { font-family: var(--font-title);
             font-weight: 600; }</pre>
<div class="lbl" style="margin-top:18px">Checklist</div>
<table class="cmp"><tr><td>Números tabulares em tabelas, KPIs e campos</td><td class="r">tabular-nums</td></tr>
<tr><td>Valores de destaque</td><td class="r">Display · 600</td></tr>
<tr><td>Corpo e formulários</td><td class="r">Text · 400 / 500</td></tr>
<tr><td>Rótulos em caixa alta</td><td class="r">10–11 px · 600 · +0,08 em</td></tr>
<tr><td>Códigos</td><td class="r">SF Mono · 400</td></tr></table></div>
</div>
''', f"{n:02d}"))

doc = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="color-scheme" content="light only"><title>W18K · Tipografia Apple</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(OUT,"w",encoding="utf-8").write(doc)
print("wrote", OUT, len(doc))
