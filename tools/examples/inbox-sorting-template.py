W='file:///tmp/claude-0/-home-claude/69543e69-ca71-5227-8fd6-9022059d6b43/scratchpad/logos/logo-white.png'
B='#2A73D9';G='#1A845C';GR='#5f5c58';RED='#C5221F';AMB='#B45309'
BASE='width:1080px;height:1350px;box-sizing:border-box;display:flex;flex-direction:column;font-family:Montserrat,sans-serif;'
def wrap(b): return '<!doctype html><meta charset=utf-8><style>body{margin:0;font-family:Montserrat,sans-serif}</style>'+b
flag=lambda c,s=56: f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="{c}" aria-hidden="true"><path d="M5 2h2v20H5z"/><path d="M8 3h12l-3 5 3 5H8z"/></svg>'
CATS=[('Bookings',6,B),('Questions',4,G),('Changes',3,GR),('Needs you',1,RED)]
def chip(n,c,t,h=130,fs=44):
    return f'<div style="background:{c};color:#fff;height:{h}px;display:flex;align-items:center;justify-content:space-between;padding:0 32px"><div style="font-size:{fs}px;font-weight:800">{n}</div><div style="font-size:{fs+16}px;font-weight:800">{t}</div></div>'
s={}
s['1']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="height:640px;background:{B};color:#fff;padding:72px 88px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between">
<div style="font-size:30px;font-weight:700;letter-spacing:3px">EXAMPLE: A NAIL SALON</div>
<div style="font-size:108px;line-height:1.04;font-weight:800;letter-spacing:-3px">Every message, sorted before you open it.</div></div>
<div style="flex:1;padding:40px 88px 48px;display:flex;flex-direction:column;gap:28px">
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:20px">{''.join(chip(n,c,t,"auto",46) for n,t,c in CATS)}</div>
<div style="display:flex;justify-content:flex-end;font-size:40px;font-weight:800">Swipe →</div></div></div>'''
def row(name,msg,hl=False):
    bg='#fff'
    return f'<div style="flex:1;background:{bg};display:flex;align-items:center;gap:28px;padding:0 32px"><div style="width:84px;height:84px;border-radius:50%;background:#d9d6d1;flex-shrink:0"></div><div style="display:flex;flex-direction:column;gap:4px"><div style="font-size:38px;font-weight:800">{name}</div><div style="font-size:32px;font-weight:600;color:{GR};line-height:1.2">{msg}</div></div></div>'
s['2']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:104px;line-height:1.02;font-weight:800;letter-spacing:-2px">Monday morning.</div>
<div style="font-size:42px;line-height:1.3">14 unread. Which ones matter?</div>
<div style="flex:1;background:#f4f3f1;margin-top:12px;padding:20px;display:flex;flex-direction:column;gap:14px">'''+row('Jess','Can I book a fill for Saturday?')+row('Taylor','Do you do gel-X extensions?')+row('Priya','I need to move my 3 PM.')+row('Dana','My nails chipped. I\'m not happy.')+row('Kim','What are your Sunday hours?')+f'''</div></div>
<div style="height:150px;background:#000;color:#fff;padding:0 88px;display:flex;align-items:center;font-size:38px;font-weight:800">Sorting this by hand eats your day.</div></div>'''
def card(n,c,t,sub):
    return f'<div style="background:{c};color:#fff;padding:36px 40px;display:flex;flex-direction:column;justify-content:space-between"><div style="font-size:150px;line-height:1;font-weight:800">{t}</div><div><div style="font-size:50px;font-weight:800">{n}</div><div style="font-size:32px;font-weight:600;margin-top:6px">{sub}</div></div></div>'
subs=['Appointment requests','Hours, prices, services','Reschedules, cancels','Waiting on a person']
s['3']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:104px;line-height:1.02;font-weight:800;letter-spacing:-2px">Sorted for you.</div>
<div style="font-size:42px;line-height:1.3">Every message lands in the right folder.</div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:20px;margin-top:12px">{''.join(card(n,c,t,subs[i]) for i,(n,t,c) in enumerate(CATS))}</div></div>
<div style="height:150px;background:{B};color:#fff;padding:0 88px;display:flex;align-items:center;font-size:38px;font-weight:800">Your folders, named your way.</div></div>'''
def pill(t): return f'<div style="display:flex;align-items:center;gap:16px;background:#000;color:#fff;padding:14px 26px;font-size:36px;font-weight:800">{flag("#fff",40)}{t}</div>'
s['4']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:104px;line-height:1.02;font-weight:800;letter-spacing:-2px">Some need a human.</div>
<div style="font-size:42px;line-height:1.3">Flagged, not auto-answered.</div>
<div style="flex:1;background:#f4f3f1;margin-top:12px;padding:40px;display:flex;flex-direction:column;justify-content:space-between;gap:28px">
<div style="background:#fff;border-left:16px solid #000;padding:48px 44px;display:flex;flex-direction:column;gap:24px;flex:1;justify-content:center">
<div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:42px;font-weight:800">Dana</div><div style="display:flex;align-items:center;gap:12px;background:#000;color:#fff;font-size:32px;font-weight:800;padding:8px 20px">{flag("#fff",36)}NEEDS YOU</div></div>
<div style="font-size:48px;font-weight:700;line-height:1.25">“My nails chipped. I'm not happy.”</div>
<div style="font-size:32px;font-weight:700;color:{GR}">Reason: complaint</div></div>
<div><div style="font-size:34px;font-weight:800;letter-spacing:2px;margin-bottom:16px;color:{GR}">YOU CHOOSE WHAT GETS FLAGGED</div><div style="display:flex;flex-wrap:wrap;gap:14px">{pill('Complaints')}{pill('Refunds')}{pill('Unclear asks')}</div></div></div></div>
<div style="height:150px;background:{G};color:#fff;padding:0 88px;display:flex;align-items:center;font-size:38px;font-weight:800">A person handles what a person should.</div></div>'''
s['5']=f'''<div style="{BASE}background:{B};color:#fff;padding:88px;justify-content:space-between">
<img src="{W}" style="width:300px;height:100px;object-fit:contain" alt="Third Hand AI logo">
<div style="display:flex;flex-direction:column;gap:36px"><div style="font-size:124px;line-height:1.02;font-weight:800;letter-spacing:-3px">Your inbox. Your rules.</div><div style="height:8px;width:160px;background:#fff"></div><div style="font-size:48px;line-height:1.3;max-width:860px">Tell us how you'd sort yours.</div></div>
<div style="background:#fff;padding:40px 48px;display:flex;justify-content:space-between;align-items:center;color:#000"><div style="font-size:44px;font-weight:800;color:{B}">Get a free quote</div><div style="font-size:34px;font-weight:700">Link in bio</div></div></div>'''

def srow(name,msg,tag,c,fl=False):
    tg=f'<div style="display:flex;align-items:center;gap:10px;background:{c};color:#fff;font-size:30px;font-weight:800;padding:10px 20px;flex-shrink:0">{flag("#fff",32) if fl else ""}{tag}</div>'
    bg='#FDECEA' if fl else '#fff'
    return f'<div style="flex:1;background:{bg};border-left:14px solid {c};display:flex;align-items:center;gap:22px;padding:0 24px"><div style="width:76px;height:76px;border-radius:50%;background:#d9d6d1;flex-shrink:0"></div><div style="display:flex;flex-direction:column;gap:4px;flex:1"><div style="font-size:36px;font-weight:800">{name}</div><div style="font-size:30px;font-weight:600;color:{GR};line-height:1.2">{msg}</div></div>{tg}</div>'
def fchip(n,c,t): return f'<div style="background:{c};color:#fff;font-size:30px;font-weight:800;padding:12px 18px;display:flex;gap:12px;flex:1;justify-content:center;white-space:nowrap">{n}<span>{t}</span></div>'
s['3']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:104px;line-height:1.02;font-weight:800;letter-spacing:-2px">Same inbox. Sorted.</div>
<div style="font-size:42px;line-height:1.3">Labeled, filed, and flagged.</div>
<div style="display:flex;gap:10px;margin-top:8px">{''.join(fchip(n,c,t) for n,t,c in CATS)}</div>
<div style="flex:1;background:#f4f3f1;padding:20px;display:flex;flex-direction:column;gap:12px">'''+srow('Jess','Can I book a fill for Saturday?','Bookings',B)+srow('Taylor','Do you do gel-X extensions?','Questions',G)+srow('Kim','What are your Sunday hours?','Questions',G)+srow('Priya','I need to move my 3 PM.','Changes',GR)+srow('Dana','My nails chipped. I\'m not happy.','Needs you',RED,True)+f'''</div></div>
<div style="height:150px;background:{B};color:#fff;padding:0 88px;display:flex;align-items:center;font-size:38px;font-weight:800">Your folders, named your way.</div></div>'''
def pill(t,c): return f'<div style="display:flex;align-items:center;gap:16px;background:#fff;border-left:14px solid {c};color:#000;padding:16px 28px;font-size:38px;font-weight:800">{flag(c,44)}{t}</div>'
s['4']=f'''<div style="{BASE}background:#fff;color:#000">
<div style="flex:1;padding:72px 88px 40px;display:flex;flex-direction:column;gap:20px">
<div style="font-size:104px;line-height:1.02;font-weight:800;letter-spacing:-2px">Some need a human.</div>
<div style="font-size:42px;line-height:1.3">Flagged, not auto-answered.</div>
<div style="flex:1;background:#f4f3f1;margin-top:12px;padding:40px;display:flex;flex-direction:column;justify-content:space-between;gap:28px">
<div style="background:#FDECEA;border-left:16px solid {RED};padding:48px 44px;display:flex;flex-direction:column;gap:24px;flex:1;justify-content:center">
<div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:42px;font-weight:800">Dana</div><div style="display:flex;align-items:center;gap:12px;background:{RED};color:#fff;font-size:32px;font-weight:800;padding:8px 20px">{flag("#fff",36)}NEEDS YOU</div></div>
<div style="font-size:48px;font-weight:700;line-height:1.25">“My nails chipped. I'm not happy.”</div>
<div style="font-size:32px;font-weight:700;color:{RED}">Flagged: complaint. No auto-reply.</div></div>
<div><div style="font-size:34px;font-weight:800;letter-spacing:2px;margin-bottom:16px;color:{GR}">YOU CHOOSE WHAT GETS FLAGGED</div><div style="display:flex;flex-wrap:wrap;gap:14px">{pill('Complaints',RED)}{pill('Refunds',AMB)}{pill('Unclear asks',B)}</div></div></div></div>
<div style="height:150px;background:{G};color:#fff;padding:0 88px;display:flex;align-items:center;font-size:38px;font-weight:800">A person handles what a person should.</div></div>'''
for k,v in s.items(): open(f'p7-{k}.html','w').write(wrap(v))
