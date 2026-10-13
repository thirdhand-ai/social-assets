# "How we did it" process post (post 9). Writes p9-*.html next to this script's cwd.
# Layout grid: content in the center square (x 150-930, y 135-1215); logo 280px wide,
# right edge x=930, centered y=1080; footer cue on one line at y=1080 left; circuit line y~1185.
import os, sys
L=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','logos'))
LC='file://'+L+'/logo-color.png'; LW='file://'+L+'/logo-white.png'
B='#2A73D9';G='#1A845C';K='#000';GR='#5f5c58';LG='#f4f3f1'
FONT='<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=block" rel="stylesheet">'
def wrap(b): return f'<!doctype html><meta charset=utf-8>{FONT}<style>body{{margin:0;font-family:Montserrat,sans-serif}}*{{box-sizing:border-box}}.a{{position:absolute}}</style><div style="position:relative;width:1080px;height:1350px;overflow:hidden">{b}</div>'
def ico(p,c='#fff',s=64): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
IC={'chat':'<path d="M4 4h16v12H9l-5 4z"/>','img':'<rect x="3" y="4" width="18" height="16" rx="1"/><circle cx="8.5" cy="9" r="1.8"/><path d="M3 18l6-6 4 4 3-3 5 5"/>',
'code':'<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>','eye':'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>','sec':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
'mail':'<rect x="3" y="5" width="18" height="14"/><path d="M3 6l9 7 9-7"/>'}
def logo(src): return f'<img class="a" src="{src}" style="left:650px;top:{1080-47}px;width:280px;height:94px;object-fit:contain" alt="">'
def cue(t,c): return f'<div class="a" style="left:150px;top:1080px;transform:translateY(-50%);font-size:34px;font-weight:800;color:{c};white-space:nowrap">{t}</div>'
def circuit(c): return f'<svg class="a" style="left:0;top:0" width="1080" height="1350" aria-hidden="true"><polyline points="150,1185 620,1185 645,1205 908,1205" fill="none" stroke="{c}" stroke-width="5"/><circle cx="150" cy="1185" r="9" fill="{c}"/><circle cx="920" cy="1205" r="10" fill="none" stroke="{c}" stroke-width="5"/></svg>'
s={}
# Slide 1: cover. Blue headline block, six-step circuit board on white, green base strip.
def chip(n,t,c): return f'<div style="background:{c};color:#fff;height:160px;padding:18px 22px;display:flex;flex-direction:column;justify-content:space-between"><div style="font-size:60px;line-height:1;font-weight:800">{n}</div><div style="font-size:32px;font-weight:800;white-space:nowrap">{t}</div></div>'
row=lambda items:'<div style="display:grid;grid-template-columns:repeat(3,240px);gap:30px">'+''.join(chip(*i) for i in items)+'</div>'
board=f'''<svg class="a" style="left:0;top:0" width="1080" height="1350" aria-hidden="true"><g stroke="{GR}" stroke-width="5" fill="{GR}">
<line x1="390" y1="684" x2="420" y2="684"/><line x1="660" y1="684" x2="690" y2="684"/><line x1="810" y1="764" x2="810" y2="824"/>
<line x1="390" y1="904" x2="420" y2="904"/><line x1="660" y1="904" x2="690" y2="904"/><circle cx="810" cy="794" r="9"/></g></svg>'''
s['1']=f'''<div class="a" style="left:0;top:0;width:1080px;height:550px;background:{B}"></div>
<div class="a" style="left:0;top:1290px;width:1080px;height:60px;background:{G}"></div>
<div class="a" style="left:150px;top:140px;width:780px;color:#fff">
<div style="font-size:30px;font-weight:700;letter-spacing:4px">HOW WE DID IT</div>
<div style="font-size:108px;line-height:1.02;font-weight:800;letter-spacing:-2px;margin-top:22px">First call to launch day.</div></div>
{board}<div class="a" style="left:150px;top:604px">{row([('01','Discovery',B),('02','Content',G),('03','Build',K)])}</div>
<div class="a" style="left:150px;top:824px">{row([('06','Care',G),('05','Launch',K),('04','Review',B)])}</div>
{logo(LC)}{cue('Swipe →',K)}{circuit(B)}'''
# Slides 2-3: bold winding circuit path through three big icon nodes, zig-zag left/right.
ROWS=[420,655,890]; LX,RX=235,845
def node(n,c,ic,cx,cy):
    return f'''<div class="a" style="left:{cx-90}px;top:{cy-90}px;width:180px;height:180px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;border:8px solid {LG}">{ico(IC[ic],'#fff',92)}</div>'''
def label(n,t,d,cy,left,c,nc):
    x='left:362px;text-align:left' if left else 'left:150px;text-align:right'
    return f'<div class="a" style="{x};top:{cy}px;width:568px;transform:translateY(-50%)"><div style="font-size:44px;line-height:1;font-weight:800;color:{nc};margin-bottom:6px">{n}</div><div style="font-size:46px;line-height:1.05;font-weight:800;letter-spacing:-1px;color:{c}">{t}</div><div style="font-size:32px;font-weight:600;color:{GR};margin-top:8px;white-space:nowrap">{d}</div></div>'
def path(c):
    y1,y2,y3=ROWS; m1,m2=(y1+y2)//2,(y2+y3)//2
    d=f'M{LX},{y1} V{m1-30} Q{LX},{m1} {LX+30},{m1} H{RX-30} Q{RX},{m1} {RX},{m1+30} V{m2-30} Q{RX},{m2} {RX-30},{m2} H{LX+30} Q{LX},{m2} {LX},{m2+30} V{y3}'
    return f'<svg class="a" style="left:0;top:0" width="1080" height="1350" aria-hidden="true"><path d="{d}" fill="none" stroke="{c}" stroke-width="14" stroke-linejoin="round"/><circle cx="{(LX+RX)//2}" cy="{m1}" r="14" fill="{c}"/><circle cx="{(LX+RX)//2}" cy="{m2}" r="14" fill="{c}"/></svg>'
def winding(items):
    out=path(GR)
    for i,(n,c,t,d,ic) in enumerate(items):
        left=i%2==0; cx=LX if left else RX
        out+=node(n,c,ic,cx,ROWS[i])+label(n,t,d,ROWS[i],left,c if n=='06' else K,c)
    return out
def head(k,h,kc): return f'<div class="a" style="left:150px;top:150px;width:780px"><div style="font-size:30px;font-weight:700;letter-spacing:4px;color:{kc}">{k}</div><div style="font-size:88px;line-height:1.04;font-weight:800;letter-spacing:-2px;margin-top:14px">{h}</div></div>'
s['2']=f'''<div class="a" style="inset:0;background:{LG}"></div><div class="a" style="left:0;top:0;width:24px;height:1350px;background:{B}"></div>
{head('STEPS 01 TO 03','Before we build.',B)}
{winding([('01',B,'Discovery','Your goals. Your package.','chat'),('02',G,'Content Collection','You send logo, photos, info.','img'),('03',K,'Design & Development','Built for every screen.','code')])}
{logo(LC)}{cue("Swipe →",K)}{circuit(B)}'''
s['3']=f'''<div class="a" style="inset:0;background:{LG}"></div><div class="a" style="left:0;top:0;width:24px;height:1350px;background:{G}"></div>
{head('STEPS 04 TO 06','Then we go live.',G)}
{winding([('04',B,'Review & Revisions','You review. We revise.','eye'),('05',K,'Launch','Domain, testing, publish.','globe'),('06',G,'Third Hand Care','Hosting, updates, monitoring.','sec')])}
{logo(LC)}{cue('Swipe →',K)}{circuit(G)}'''
def contact(ic,t): return f'<div style="background:#fff;color:{K};height:110px;display:flex;align-items:center;gap:26px;padding:0 32px;font-size:40px;font-weight:800;white-space:nowrap">{ico(IC[ic],B,52)}{t}</div>'
s['4']=f'''<div class="a" style="inset:0;background:{B}"></div>
<div class="a" style="left:150px;top:160px;width:780px;color:#fff">
<div style="font-size:30px;font-weight:700;letter-spacing:4px">YOUR TURN</div>
<div style="font-size:112px;line-height:1.02;font-weight:800;letter-spacing:-3px;margin-top:22px">Ready for step 01?</div>
<div style="height:8px;width:160px;background:#fff;margin:40px 0 34px"></div>
<div style="font-size:40px;line-height:1.3;font-weight:600">Tell us about your business. We'll send a free, custom quote.</div>
<div style="display:flex;flex-direction:column;gap:20px;margin-top:48px">{contact('globe','thirdhandai.com')}{contact('mail','tyler@thirdhandai.com')}</div></div>
{logo(LW)}{cue('Link in bio',"#fff")}{circuit('#fff')}'''
for k,v in s.items(): open(f'p9c-{k}.html','w').write(wrap(v))
