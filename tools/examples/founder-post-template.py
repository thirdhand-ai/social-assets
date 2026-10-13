import os
D=os.path.dirname(os.path.abspath(__file__))
W='file:///tmp/claude-0/-home-claude/69543e69-ca71-5227-8fd6-9022059d6b43/scratchpad/logos/logo-white.png'
PH='file://'+D+'/tyler.jpg'
B='#2A73D9';G='#1A845C';GR='#5f5c58';OR='#FA4616';RD='#D50A0A';PA='#FF8000'
BASE='width:1080px;height:1350px;box-sizing:border-box;display:flex;flex-direction:column;font-family:Montserrat,sans-serif;'
def wrap(b): return '<!doctype html><meta charset=utf-8><style>body{margin:0;font-family:Montserrat,sans-serif}</style>'+b
def ico(path,c='#fff',s=64): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'
IC={'host':'<path d="M6.5 19a4.5 4.5 0 0 1-.6-8.96A6 6 0 0 1 17.5 9a4.8 4.8 0 0 1 0 10z"/>','sec':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>','txt':'<path d="M4 20l1-5L16 4l4 4L9 19z"/><path d="M14 6l4 4"/>','img':'<rect x="3" y="4" width="18" height="16" rx="1"/><circle cx="8.5" cy="9" r="1.8"/><path d="M3 18l6-6 4 4 3-3 5 5"/>','form':'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>','seo':'<circle cx="10" cy="10" r="6"/><path d="M15 15l6 6"/>'}
s={}
s['1']=f'''<div style="{BASE}background:{B};color:#fff">
<div style="height:385px;padding:64px 88px 0;box-sizing:border-box;display:flex;flex-direction:column;gap:14px">
<div style="font-size:30px;font-weight:700;letter-spacing:3px">HI, I'M TYLER</div>
<div style="font-size:112px;line-height:1.04;font-weight:800;letter-spacing:-3px">The human behind the AI.</div></div>
<div style="flex:1;padding:28px 150px 0;box-sizing:border-box;background:#fff;position:relative;overflow:hidden"><img src="{PH}" style="width:780px;height:100%;object-fit:cover;object-position:50% 22%;display:block" alt="Tyler Tyson, founder of Third Hand AI"></div>
<div style="height:130px;background:{G};padding:0 88px;display:flex;align-items:center;justify-content:space-between;font-size:38px;font-weight:800"><div>Let's get to know each other.</div><div>Swipe →</div></div></div>'''
def prow(tag,bg,fg,t,d): return f'<div style="flex:1;background:#f4f3f1;display:flex;align-items:stretch"><div style="width:250px;background:{bg};color:{fg};display:flex;align-items:center;justify-content:center;font-size:48px;font-weight:800;flex-shrink:0">{tag}</div><div style="flex:1;padding:0 32px;display:flex;flex-direction:column;justify-content:center;gap:6px"><div style="font-size:40px;font-weight:800;line-height:1.1">{t}</div><div style="font-size:32px;font-weight:600;line-height:1.2;color:#2b2b2b">{d}</div></div></div>'
s['2']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:88px;line-height:1.02;font-weight:800;letter-spacing:-2px">A little about me.</div>
<div style="font-size:36px;line-height:1.3">The fun stuff.</div>
<div style="flex:1;display:flex;flex-direction:column;gap:14px;margin-top:12px">'''+prow('UF',B,'#fff','Junior at UF','Information Systems major')+prow('JESUIT','#6E6E6E','#fff','Valedictorian','Jesuit High School. Played soccer.')+prow('GATORS',OR,'#fff','Never miss a game','Favorite moment: Feleipe Franks\' Hail Mary against Tennessee, 2017')+prow('TAMPA',RD,'#fff','Tampa born and raised','Avid Buccaneers, Rays, and Lightning fan')+prow('F1',PA,'#000','McLaren fan','Favorite driver: Liam Lawson. Went to the Miami Grand Prix in May.')+f'''</div></div>
<div style="height:150px;background:#000;color:#fff;padding:0 88px;display:flex;align-items:center;font-size:38px;font-weight:800">Now, why Third Hand AI?</div></div>'''
arrow=f'''<svg width="360" height="620" viewBox="0 0 360 620" role="img" aria-label="Arrow"><polygon points="0,170 180,0 360,170" fill="{G}"/><rect x="30" y="170" width="300" height="170" fill="{G}"/><rect x="30" y="340" width="300" height="280" fill="{B}"/><text x="180" y="278" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="68" fill="#fff">+ AI</text></svg>'''
bars=f'''<div style="display:flex;align-items:flex-end;justify-content:center;gap:56px;height:100%;padding:20px 0 0">
<div style="display:flex;flex-direction:column;align-items:center;gap:20px"><div style="width:300px;height:500px;background:#3a3a3a"></div><div style="font-size:36px;font-weight:800">Established firm</div></div>
<div style="display:flex;flex-direction:column;align-items:center;gap:20px">{arrow}<div style="font-size:36px;font-weight:800">Small business</div></div></div>'''
s['3']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:100px;line-height:1.02;font-weight:800;letter-spacing:-2px">AI levels the playing field.</div>
<div style="font-size:40px;line-height:1.3">For small businesses willing to adapt.</div>
<div style="flex:1;background:#f4f3f1;margin-top:12px;padding-bottom:24px;box-sizing:border-box">{bars}</div></div>
<div style="height:150px;background:{B};color:#fff;padding:0 88px;display:flex;align-items:center;font-size:38px;font-weight:800">That's why I started Third Hand AI.</div></div>'''
def chip(t,c): return f'<div style="background:#fff;border-left:16px solid {c};padding:0 28px;height:130px;display:flex;align-items:center;font-size:42px;font-weight:800">{t}</div>'
s['4']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:96px;line-height:1.02;font-weight:800;letter-spacing:-2px">I don't sell what you don't need.</div>
<div style="font-size:40px;line-height:1.3">I learn your business first.</div>
<div style="flex:1;background:#f4f3f1;margin-top:12px;padding:40px;display:flex;align-items:center;gap:20px">
<div style="flex:1;display:flex;flex-direction:column;gap:20px">{chip('Your needs',B)}{chip('Your mission',G)}{chip('Your values','#000')}</div>
<div style="font-size:80px;font-weight:800;color:{GR}">→</div>
<div style="flex:1;align-self:stretch;background:{G};color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 28px;gap:12px"><div style="font-size:64px;line-height:1.05;font-weight:800">Built for you.</div><div style="font-size:32px;font-weight:600;line-height:1.2">Custom tools, even if I've never built one before.</div></div></div></div>
<div style="height:150px;background:#000;color:#fff;padding:0 88px;display:flex;align-items:center;font-size:38px;font-weight:800">Everything fitted to how you work.</div></div>'''
def care(t,bg,ic,fg='#fff'): return f'<div style="background:{bg};color:{fg};padding:0 28px;display:flex;align-items:center;gap:22px;font-size:40px;font-weight:800;line-height:1.1">{ico(IC[ic],fg,72)}<span>{t}</span></div>'
s['5']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:112px;line-height:1.02;font-weight:800;letter-spacing:-3px">Not one and done.</div>
<div style="font-size:40px;line-height:1.3">Every site comes with Third Hand Care.</div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:16px;margin-top:12px">{care('Hosting',B,'host')}{care('Security (SSL)',G,'sec')}{care('Text updates',G,'txt')}{care('Image swaps','#000','img')}{care('Form monitoring','#000','form')}{care('SEO health checks',B,'seo')}</div></div>
<div style="height:150px;background:{G};color:#fff;padding:0 88px;display:flex;align-items:center;font-size:36px;font-weight:800">Included with every package. $75/month after.</div></div>'''
s['6']=f'''<div style="{BASE}background:{G};color:#fff;padding:88px;justify-content:space-between">
<img src="{W}" style="width:300px;height:100px;object-fit:contain" alt="Third Hand AI logo">
<div style="display:flex;flex-direction:column;gap:36px"><div style="font-size:120px;line-height:1.02;font-weight:800;letter-spacing:-3px">Tell me about your business.</div><div style="height:8px;width:160px;background:#fff"></div><div style="font-size:48px;line-height:1.3;max-width:860px">I'll build around it.</div></div>
<div style="background:#fff;padding:40px 48px;display:flex;justify-content:space-between;align-items:center;color:#000"><div style="font-size:44px;font-weight:800;color:{G}">Get a free quote</div><div style="font-size:34px;font-weight:700">Link in bio</div></div></div>'''
for k,v in s.items(): open(f'p9-{k}.html','w').write(wrap(v))
