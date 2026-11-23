# Run1123 디자인 10종 생성기: 공통 헤더 + 각 시안 본문 → NN.html
HEAD = """<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>Run1123 — {title}</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<style>
/* Tweaks: 포인트(운동화 밑창 블루) + 보조(양말 머스터드) */
:root {{ --accent:#7cc7f0; --accent2:#e0a860; }}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#000}}
.board{{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Noto Sans KR',sans-serif;color:#fff}}
.a{{font-family:'Anton';font-weight:400;line-height:1}}
.abs{{position:absolute}}
.route{{-webkit-mask:url(route.png) center/contain no-repeat;mask:url(route.png) center/contain no-repeat}}
.tex{{background:url(tex.jpg) center/cover}}
{css}
</style></head><body><div class="board">{body}</div></body></html>"""

D = dict(dist="5.22", time="42:28", pace="8'08\"", hr="129", cad="159", s="19:43", e="20:26")

designs = {}

designs["01"] = ("Split", """
.ph{left:0;top:0;width:1080px;height:820px;background:url(top.jpg) center/cover;filter:brightness(.9) contrast(1.1)}
.bl{left:0;top:820px;width:1080px;height:1100px;background:#0b0b0c}
.tag{left:80px;top:890px;font-size:26px;letter-spacing:.32em;font-weight:500;color:var(--accent)}
.n{left:66px;top:930px;font-size:430px;letter-spacing:-6px}
.u{left:740px;top:1222px;font-size:72px}
.rule{left:80px;right:80px;top:1420px;height:2px;background:rgba(255,255,255,.3)}
.g{left:80px;right:80px;top:1470px;display:grid;grid-template-columns:repeat(3,1fr)}
.g .v{font-size:86px}.g .l{font-size:24px;margin-top:12px;color:rgba(255,255,255,.75);letter-spacing:.1em}
.f{left:80px;right:80px;bottom:110px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.2em;color:rgba(255,255,255,.75)}
""", f"""
<div class="abs ph"></div><div class="abs bl"></div>
<div class="abs tag">RECOVERY RUN · 회복런</div>
<div class="abs a n">{D['dist']}</div><div class="abs a u">KM</div>
<div class="abs rule"></div>
<div class="abs g"><div><div class="a v">{D['time']}</div><div class="l">운동 시간</div></div>
<div><div class="a v">{D['pace']}</div><div class="l">페이스 /KM</div></div>
<div><div class="a v">{D['hr']}</div><div class="l">심박 BPM</div></div></div>
<div class="abs f"><span>2026.11.23 MON</span><span>{D['s']} — {D['e']}</span></div>
""")

designs["02"] = ("Route Hero", """
.board{background:radial-gradient(circle at 50% 30%,#1b2230,#0a0c10 70%)}
.r{left:240px;top:180px;width:600px;height:840px;background:var(--accent);filter:drop-shadow(0 0 24px rgba(124,199,240,.55))}
.d{left:80px;top:96px;font-size:24px;letter-spacing:.3em;font-weight:500;color:rgba(255,255,255,.8)}
.n{left:72px;top:1090px;font-size:330px;letter-spacing:-4px}
.u{left:80px;top:1420px;font-size:28px;letter-spacing:.3em;color:var(--accent)}
.s{left:80px;right:80px;top:1500px;display:grid;grid-template-columns:repeat(3,1fr)}
.s>div{margin:0}.s .v{font-size:74px}.s .l{font-size:22px;color:rgba(255,255,255,.75);margin-top:8px;letter-spacing:.1em}
.f{left:80px;bottom:110px;font-size:24px;letter-spacing:.2em;color:rgba(255,255,255,.75)}
""", f"""
<div class="abs d">11.23 MON · 회복런</div>
<div class="abs route r"></div>
<div class="abs a n">{D['dist']}</div><div class="abs u">KILOMETERS</div>
<div class="abs s"><div><div class="a v">{D['time']}</div><div class="l">운동 시간</div></div>
<div><div class="a v">{D['pace']}</div><div class="l">페이스 /KM</div></div>
<div><div class="a v">{D['hr']}</div><div class="l">심박 BPM</div></div></div>
<div class="abs f">{D['s']} — {D['e']} · {D['cad']} SPM</div>
""")

designs["03"] = ("Ground", """
.bg{inset:0;filter:brightness(.62) contrast(1.15)}
.v1{inset:0;background:radial-gradient(ellipse at 50% 60%,transparent 30%,rgba(0,0,0,.55))}
.plane{left:0;top:0;width:1080px;height:1920px;perspective:1100px}
.floor{position:absolute;left:150px;top:620px;width:900px;transform:rotateX(52deg) rotateZ(-14deg);transform-origin:50% 50%}
.floor .n{font-size:380px;letter-spacing:-6px;text-shadow:0 0 1px #fff}
.floor .row{display:flex;gap:60px;margin-top:20px}
.floor .row .v{font-size:110px}.floor .row .l{font-size:34px;margin-top:6px;letter-spacing:.1em}
.r{left:640px;top:1230px;width:340px;height:480px;background:#fff;opacity:.9;transform:rotate(-14deg)}
.d{left:80px;top:110px;font-size:26px;letter-spacing:.3em;font-weight:500}
.t{left:80px;top:150px;font-size:44px;font-weight:900}
.f{left:80px;bottom:110px;font-size:24px;letter-spacing:.2em}
.f b{color:var(--accent2);font-weight:700}
""", f"""
<div class="abs tex bg"></div><div class="abs v1"></div>
<div class="abs d">2026.11.23 MON</div><div class="abs t">천천히, 회복런</div>
<div class="abs plane"><div class="floor"><div class="a n">{D['dist']}<span style="font-size:120px"> KM</span></div>
<div class="row"><div><div class="a v">{D['time']}</div><div class="l">운동 시간</div></div>
<div><div class="a v">{D['pace']}</div><div class="l">페이스</div></div>
<div><div class="a v">{D['hr']}</div><div class="l">심박</div></div></div></div></div>
<div class="abs route r"></div>
<div class="abs f"><b>{D['s']} — {D['e']}</b> · {D['cad']} SPM</div>
""")

designs["04"] = ("Low Heart", """
.board{background:linear-gradient(180deg,#0f1b2b,#16283c 60%,#1d3450)}
.ph{left:80px;top:150px;width:920px;height:520px;background:url(top.jpg) center/cover;border-radius:18px;filter:brightness(.85) saturate(.8)}
.d{left:80px;top:80px;font-size:24px;letter-spacing:.3em;font-weight:500;color:rgba(255,255,255,.85)}
.n{left:70px;top:740px;font-size:330px;letter-spacing:-4px}
.u{left:600px;top:960px;font-size:60px;color:rgba(255,255,255,.9)}
.gauge{left:80px;right:80px;top:1190px}
.gauge .cap{font-size:24px;letter-spacing:.2em;color:var(--accent)}
.gauge .bar{position:relative;height:16px;border-radius:8px;margin-top:70px;background:linear-gradient(90deg,#4c8fbf,#7cc7f0 30%,#e0a860 65%,#e8665a)}
.gauge .mk{position:absolute;top:-62px;transform:translateX(-50%);text-align:center}
.gauge .mk b{font-family:'Anton';font-weight:400;font-size:52px}
.gauge .mk i{display:block;width:4px;height:30px;background:#fff;margin:6px auto 0}
.gauge .sc{display:flex;justify-content:space-between;font-size:22px;margin-top:14px;color:rgba(255,255,255,.75)}
.g{left:80px;right:80px;top:1480px;display:grid;grid-template-columns:repeat(3,1fr)}
.g .v{font-size:78px}.g .l{font-size:22px;margin-top:10px;color:rgba(255,255,255,.75)}
.f{left:80px;bottom:110px;font-size:26px;font-weight:300;color:rgba(255,255,255,.85)}
""", f"""
<div class="abs d">11.23 MON · ZONE 2</div>
<div class="abs ph"></div>
<div class="abs a n">{D['dist']}</div><div class="abs a u">KM</div>
<div class="abs gauge"><div class="cap">낮게 유지한 심박</div>
<div class="bar"><div class="mk" style="left:29%"><b>{D['hr']}</b><i></i></div></div>
<div class="sc"><span>100</span><span>BPM</span><span>200</span></div></div>
<div class="abs g"><div><div class="a v">{D['time']}</div><div class="l">운동 시간</div></div>
<div><div class="a v">{D['pace']}</div><div class="l">페이스 /KM</div></div>
<div><div class="a v">{D['cad']}</div><div class="l">케이던스</div></div></div>
<div class="abs f">오후 7:43 – 8:26 · 회복런</div>
""")

designs["05"] = ("Film Stamp", """
.board{background:#111}
.fr{left:60px;top:300px;width:960px;height:1000px;background:#000;padding:30px 30px 30px}
.fr .ph{width:100%;height:100%;background:url(top.jpg) 30% center/cover;filter:contrast(1.1) saturate(1.1) sepia(.15)}
.holes{left:60px;width:960px;height:30px;background:radial-gradient(circle,#111 6px,transparent 7px) 0 0/40px 30px}
.st{left:640px;top:1200px;font-family:'Anton';font-size:64px;color:#ff8a2a;letter-spacing:4px;text-shadow:0 0 10px rgba(255,120,30,.8),0 0 2px #ffb070}
.n{left:60px;top:1370px;font-size:280px;letter-spacing:-3px}
.u{left:560px;top:1560px;font-size:54px;color:var(--accent2)}
.g{left:680px;top:1380px;right:60px}
.g div{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(255,255,255,.25);padding:10px 0}
.g .v{font-size:50px}.g .l{font-size:22px;color:rgba(255,255,255,.75)}
.t{left:60px;top:170px;font-size:30px;font-weight:300;letter-spacing:.1em}
.t b{font-weight:900}
.f{left:60px;bottom:110px;font-size:22px;letter-spacing:.3em;color:rgba(255,255,255,.7)}
""", f"""
<div class="abs t"><b>RECOVERY</b> / 회복런 필름</div>
<div class="abs holes" style="top:262px"></div>
<div class="abs fr"><div class="ph"></div></div>
<div class="abs holes" style="top:1305px"></div>
<div class="abs st">'26 11 23</div>
<div class="abs a n">{D['dist']}</div><div class="abs a u">KM</div>
<div class="abs g"><div><span class="a v">{D['time']}</span><span class="l">시간</span></div>
<div><span class="a v">{D['pace']}</span><span class="l">페이스</span></div>
<div><span class="a v">{D['hr']}</span><span class="l">심박</span></div></div>
<div class="abs f">{D['s']} — {D['e']} · {D['cad']} SPM</div>
""")

designs["06"] = ("Receipt", """
.bg{inset:0;filter:brightness(.55)}
.rc{left:150px;top:170px;width:780px;background:#f7f5ef;color:#151515;padding:60px 60px 90px;transform:rotate(-2.5deg);box-shadow:0 30px 60px rgba(0,0,0,.5);
  -webkit-mask:linear-gradient(#000,#000) top/100% calc(100% - 24px) no-repeat,conic-gradient(from 135deg at top,#000 90deg,transparent 0) bottom/48px 24px repeat-x}
.rc h1{font-family:'Anton';font-weight:400;font-size:84px;text-align:center;letter-spacing:6px}
.rc .sub{text-align:center;font-size:22px;letter-spacing:.3em;margin-top:6px}
.rc hr{border:0;border-top:3px dashed #151515;margin:34px 0}
.rc .li{display:flex;justify-content:space-between;align-items:baseline;font-size:30px;font-weight:500;margin:16px 0}
.rc .li b{font-family:'Anton';font-weight:400;font-size:56px}
.rc .tot{display:flex;justify-content:space-between;align-items:flex-end}
.rc .tot span{font-size:34px;font-weight:900}
.rc .tot b{font-family:'Anton';font-weight:400;font-size:220px;line-height:.9}
.rc .tot b small{font-size:60px}
.rc .bc{height:110px;margin-top:40px;background:repeating-linear-gradient(90deg,#151515 0 4px,transparent 4px 9px,#151515 9px 16px,transparent 16px 19px,#151515 19px 21px,transparent 21px 28px)}
.rc .th{text-align:center;font-size:24px;margin-top:20px;letter-spacing:.2em}
""", f"""
<div class="abs tex bg"></div>
<div class="abs rc"><h1>RUN RECEIPT</h1><div class="sub">2026.11.23 MON · {D['s']}–{D['e']}</div>
<hr><div class="li"><span>운동 시간</span><b>{D['time']}</b></div>
<div class="li"><span>페이스 /KM</span><b>{D['pace']}</b></div>
<div class="li"><span>심박 BPM</span><b>{D['hr']}</b></div>
<div class="li"><span>케이던스 SPM</span><b>{D['cad']}</b></div>
<hr><div class="tot"><span>TOTAL</span><b>{D['dist']}<small>KM</small></b></div>
<div class="bc"></div><div class="th">회복런 · THANK YOU, LEGS</div></div>
""")

designs["07"] = ("Magazine", """
.bg{inset:0;filter:brightness(.6) contrast(1.1)}
.ph{left:0;top:600px;width:1080px;height:900px;background:url(top.jpg) 25% center/cover;filter:brightness(.85)}
.mh{left:40px;top:40px;font-size:400px;letter-spacing:-4px;color:#fff}
.iss{left:56px;top:470px;right:56px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.25em;font-weight:500;border-top:2px solid #fff;padding-top:16px}
.badge{left:700px;top:1340px;width:320px;height:320px;border-radius:50%;background:var(--accent);color:#0c1720;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg)}
.badge b{font-family:'Anton';font-weight:400;font-size:140px;line-height:1}
.badge span{font-size:28px;font-weight:900;letter-spacing:.2em}
.cl{left:56px;top:1560px;width:600px}
.cl p{font-size:30px;font-weight:700;margin-bottom:14px}
.cl p b{font-family:'Anton';font-weight:400;font-size:56px;margin-right:12px;color:var(--accent2)}
""", f"""
<div class="abs tex bg"></div><div class="abs ph"></div>
<div class="abs a mh">SLOW</div>
<div class="abs iss"><span>RECOVERY ISSUE</span><span>NOV 23 2026</span></div>
<div class="abs badge"><b>{D['dist']}</b><span>KM</span></div>
<div class="abs cl"><p><b>{D['time']}</b>운동 시간</p><p><b>{D['pace']}</b>페이스</p><p><b>{D['hr']}</b>심박, 낮게</p></div>
""")

designs["08"] = ("Left Stack", """
.bg{inset:0;filter:brightness(.5) contrast(1.2)}
.st{left:80px;top:300px}
.st .l{font-size:26px;font-weight:700;letter-spacing:.2em;color:var(--accent)}
.st .v{margin:6px 0 50px}
.d .v{font-size:300px;letter-spacing:-3px}
.r{right:70px;top:120px;width:260px;height:364px;background:#fff}
.dt{left:80px;top:120px;font-size:26px;letter-spacing:.3em;font-weight:500}
.f{left:80px;bottom:110px;font-size:24px;letter-spacing:.2em;color:rgba(255,255,255,.85)}
""", f"""
<div class="abs tex bg"></div>
<div class="abs dt">11.23 MON<br>회복런</div>
<div class="abs route r"></div>
<div class="abs st"><div class="d"><div class="l">DISTANCE</div><div class="a v">{D['dist']}<span style="font-size:90px"> KM</span></div></div>
<div><div class="l">TIME</div><div class="a v" style="font-size:150px">{D['time']}</div></div>
<div><div class="l">PACE</div><div class="a v" style="font-size:130px">{D['pace']}</div></div>
<div><div class="l">HEART RATE</div><div class="a v" style="font-size:110px">{D['hr']}<span style="font-size:44px"> BPM</span></div></div></div>
<div class="abs f">{D['s']} — {D['e']} · {D['cad']} SPM</div>
""")

designs["09"] = ("Boarding Pass", """
.board{background:linear-gradient(160deg,#1a2a3a,#0b1118)}
.tk{left:80px;top:220px;width:920px;height:1480px;background:#f4f1ea;color:#121820;border-radius:36px;overflow:hidden}
.tk .hd{height:150px;background:var(--accent);display:flex;align-items:center;justify-content:space-between;padding:0 50px}
.tk .hd b{font-family:'Anton';font-weight:400;font-size:64px;letter-spacing:3px}
.tk .hd span{font-size:24px;font-weight:700;letter-spacing:.2em}
.tk .rt{display:flex;justify-content:space-between;align-items:center;padding:60px 50px 20px}
.tk .rt .c b{display:block;font-family:'Anton';font-weight:400;font-size:120px;line-height:1}
.tk .rt .c span{font-size:24px;font-weight:700;letter-spacing:.2em}
.tk .map{height:420px;margin:0 50px;background:#121820;-webkit-mask:url(route.png) center/contain no-repeat;mask:url(route.png) center/contain no-repeat}
.tk .row{display:grid;grid-template-columns:repeat(3,1fr);padding:40px 50px 0}
.tk .row span{font-size:22px;font-weight:700;letter-spacing:.15em;color:#55606c}
.tk .row b{display:block;font-family:'Anton';font-weight:400;font-size:70px;margin-top:6px}
.tk .cut{border-top:4px dashed #b9b4aa;margin:56px 0 0;position:relative}
.tk .bt{display:flex;justify-content:space-between;align-items:flex-end;padding:30px 50px}
.tk .bt b{font-family:'Anton';font-weight:400;font-size:210px;line-height:.9}
.tk .bt b small{font-size:60px}
.tk .bt span{font-size:26px;font-weight:900;letter-spacing:.2em;margin-bottom:20px}
.tk .rt .c.r{text-align:right}
.tk .rt .mid{font-size:24px;font-weight:700;letter-spacing:.2em;color:#55606c}
""", f"""
<div class="abs tk"><div class="hd"><b>RUN PASS</b><span>2026.11.23 MON</span></div>
<div class="rt"><div class="c"><span>START</span><b>{D['s']}</b></div><div class="mid">SEOUL ⟶</div><div class="c r"><span>FINISH</span><b>{D['e']}</b></div></div>
<div class="map"></div>
<div class="row"><div><span>TIME</span><b>{D['time']}</b></div><div><span>PACE</span><b>{D['pace']}</b></div><div><span>BPM</span><b>{D['hr']}</b></div></div>
<div class="cut"></div><div class="bt"><b>{D['dist']}<small>KM</small></b><span>회복런</span></div></div>
""")

designs["10"] = ("Swiss Grid", """
.board{background:#f1efe9;color:#111}
.gl{inset:0;background:linear-gradient(90deg,rgba(0,0,0,.08) 1px,transparent 1px) 0 0/270px 100%}
.n{left:40px;top:150px;font-size:520px;letter-spacing:-8px}
.km{left:60px;top:690px;font-size:30px;font-weight:900;letter-spacing:.4em}
.blk{left:540px;top:800px;width:540px;height:540px;background:var(--accent)}
.ph{left:540px;top:800px;width:540px;height:540px;background:url(top.jpg) 30% center/cover;mix-blend-mode:multiply;filter:grayscale(1) contrast(1.2)}
.c{position:absolute;width:250px}
.c span{font-size:22px;font-weight:700;letter-spacing:.15em}
.c b{display:block;font-family:'Anton';font-weight:400;font-size:96px;line-height:1;margin-top:8px}
.d{left:60px;top:90px;font-size:24px;font-weight:700;letter-spacing:.3em}
.ty{left:60px;top:1440px;font-size:120px;font-weight:900;letter-spacing:-4px;line-height:1}
.ty i{font-style:normal;color:var(--accent2)}
.f{left:60px;bottom:100px;font-size:22px;font-weight:700;letter-spacing:.3em}
""", f"""
<div class="abs gl"></div>
<div class="abs d">2026 — 11 — 23 MON</div>
<div class="abs a n">{D['dist']}</div><div class="abs km">KILOMETERS</div>
<div class="abs blk"></div><div class="abs ph"></div>
<div class="c" style="left:60px;top:820px"><span>운동 시간</span><b>{D['time']}</b></div>
<div class="c" style="left:60px;top:1000px"><span>페이스</span><b>{D['pace']}</b></div>
<div class="c" style="left:300px;top:820px"><span>심박</span><b>{D['hr']}</b></div>
<div class="c" style="left:300px;top:1000px"><span>케이던스</span><b>{D['cad']}</b></div>
<div class="abs ty">회복<i>런</i>.</div>
<div class="abs f">{D['s']} — {D['e']} · SEOUL</div>
""")

import base64
ROUTE = "data:image/png;base64," + base64.b64encode(open("route.png","rb").read()).decode()  # file:// 에서 mask가 막혀 인라인
for k,(t,css,body) in designs.items():
    open(f"{k}.html","w").write(HEAD.format(title=t,css=css,body=body).replace("url(route.png)", f"url({ROUTE})"))
print("ok", len(designs))
