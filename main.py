import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; BG=(250,246,235); INK=(20,20,20); RED=(178,34,34); NAVY=(23,48,84); GOLD=(176,132,28)
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; SANS="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; SANSB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def F(s,b=False,serif=False):
    try: return ImageFont.truetype(SERIF if serif else (SANSB if b else SANS),s)
    except Exception: return ImageFont.load_default()
def wrap(d,t,f,mw):
    words=t.split(); lines=[]; cur=""
    for w in words:
        x=(cur+" "+w).strip()
        if d.textlength(x,font=f)<=mw: cur=x
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def txt(d,x,y,t,f,fill=INK,anchor="la"):
    d.text((x,y),t,font=f,fill=fill,anchor=anchor)
def chip(d,x,y,t,c):
    f=F(7,True); w=int(d.textlength(t,font=f))+8
    d.rounded_rectangle([x,y,x+w,y+12],radius=2,fill=c); d.text((x+4,y+1),t,font=f,fill=(255,255,255)); return w
CHIP={"CONFIRMED":(34,139,34),"OFFICIAL":(30,90,168),"REPORTED":(90,90,90),"CLAIM":(200,90,20)}
def scene(d,x,y,w,h,kind):
    sky={"tower":(30,30,60),"party":(150,30,30),"court":(40,60,90),"war":(25,25,40),"trophy":(20,90,60),"ship":(20,70,110),"chart":(20,60,40),"server":(90,10,10),"heli":(90,90,110),"shop":(120,80,40),"desert":(180,140,70),"strike":(140,60,30),"rocket":(15,20,50),"generic":(60,80,110)}[kind]
    d.rectangle([x,y,x+w,y+h],fill=sky)
    if h<60:
        d.rectangle([x,y+h-6,x+w,y+h],fill=(40,32,22) if kind!="ship" else (15,45,80))
        if kind in ("tower","party","court"): d.rectangle([x+w*0.44,y+6,x+w*0.56,y+h-6],fill=(220,220,220)); d.polygon([(x+w*0.42,y+6),(x+w*0.5,y-2),(x+w*0.58,y+6)],fill=(240,240,240))
        elif kind=="trophy": d.ellipse([x+w*0.44,y+4,x+w*0.56,y+16],fill=(255,215,0)); d.rectangle([x+w*0.48,y+16,x+w*0.52,y+h-6],fill=(255,215,0))
        elif kind=="ship": d.rectangle([x+w*0.3,y+16,x+w*0.7,y+24],fill=(180,60,40)); d.rectangle([x+w*0.4,y+8,x+w*0.6,y+16],fill=(230,230,230))
        elif kind=="chart": d.line([x+10,y+h-10,x+w*0.4,y+14,x+w-10,y+6],fill=(34,139,34),width=2); d.line([x+10,y+h-10,x+w-10,y+h-10],fill=(255,255,255),width=1)
        elif kind=="server":
            for r in range(2): d.rectangle([x+w*0.3,y+6+r*12,x+w*0.7,y+14+r*12],fill=(50,50,60)); d.ellipse([x+w*0.33,y+8+r*12,x+w*0.36,y+12+r*12],fill=(255,40,40))
        elif kind=="heli": d.ellipse([x+w*0.35,y+12,x+w*0.6,y+22],fill=(200,220,200)); d.line([x+w*0.25,y+10,x+w*0.7,y+10],fill=(60,60,60),width=2); d.line([x+w*0.6,y+17,x+w*0.85,y+17],fill=(60,60,60),width=2)
        elif kind=="shop": d.rectangle([x+w*0.2,y+8,x+w*0.8,y+16],fill=(200,40,40)); d.rectangle([x+w*0.46,y+16,x+w*0.54,y+h-6],fill=(90,60,30))
        elif kind=="desert": d.ellipse([x+w*0.68,y+4,x+w*0.78,y+14],fill=(255,220,90)); d.polygon([(x+w*0.1,y+h-6),(x+w*0.35,y+16),(x+w*0.6,y+h-6)],fill=(220,180,110))
        elif kind=="strike": d.ellipse([x+w*0.42,y+6,x+w*0.58,y+22],fill=(255,140,40)); d.ellipse([x+w*0.47,y+11,x+w*0.53,y+17],fill=(255,220,90))
        elif kind=="rocket": d.polygon([(x+w*0.46,y+4),(x+w*0.54,y+4),(x+w*0.56,y+20),(x+w*0.44,y+20)],fill=(230,230,230)); d.ellipse([x+w*0.46,y+20,x+w*0.54,y+26],fill=(255,150,40))
        elif kind=="war":
            for i in range(3): d.ellipse([x+w*0.2+i*w*0.25,y+6+i*3,x+w*0.3+i*w*0.25,y+16+i*3],fill=(255,150,40))
        else: d.ellipse([x+w*0.7,y+4,x+w*0.82,y+16],fill=(255,220,90)); d.rectangle([x+w*0.2,y+18,x+w*0.8,y+h-6],fill=(120,140,170))
        return
    d.rectangle([x,y+h-14,x+w,y+h],fill=(40,32,22) if kind!="ship" else (15,45,80))
    if kind=="tower":
        d.rectangle([x+w*0.42,y+8,x+w*0.58,y+h-14],fill=(210,210,220)); d.polygon([(x+w*0.42,y+8),(x+w*0.5,y-2),(x+w*0.58,y+8)],fill=(230,230,240))
        for i in range(5): d.rectangle([x+w*0.45,y+14+i*12,x+w*0.55,y+20+i*12],fill=(255,220,90))
        d.ellipse([x+w*0.66,y+18,x+w*0.78,y+30],fill=(255,120,30)); d.ellipse([x+w*0.70,y+22,x+w*0.74,y+26],fill=(255,200,60))
        d.polygon([(x+w*0.15,y+h-14),(x+w*0.2,y+40),(x+w*0.3,y+40),(x+w*0.35,y+h-14)],fill=(90,90,100)); d.polygon([(x+w*0.68,y+h-14),(x+w*0.72,y+48),(x+w*0.82,y+48),(x+w*0.86,y+h-14)],fill=(80,80,95))
        d.ellipse([x+w*0.60,y+34,x+w*0.66,y+40],fill=(200,200,200)); d.line([x+w*0.60,y+37,x+w*0.72,y+30],fill=(220,220,220),width=2)
    elif kind=="party":
        d.rectangle([x+w*0.2,y+30,x+w*0.8,y+h-14],fill=(150,40,40)); d.polygon([(x+w*0.2,y+30),(x+w*0.5,y+8),(x+w*0.8,y+30)],fill=(120,25,25))
        d.rectangle([x+w*0.44,y+55,x+w*0.56,y+h-14],fill=(60,30,20)); d.rectangle([x+w*0.30,y+45,x+w*0.38,y+53],fill=(255,220,90)); d.rectangle([x+w*0.62,y+45,x+w*0.70,y+53],fill=(255,220,90))
        d.rectangle([x+w*0.12,y+62,x+w*0.30,y+70],fill=(255,255,255)); d.line([x+w*0.12,y+66,x+w*0.30,y+66],fill=(200,0,0),width=2); d.ellipse([x+w*0.82,y+14,x+w*0.92,y+24],fill=(255,220,90))
    elif kind=="court":
        d.rectangle([x+w*0.15,y+28,x+w*0.85,y+h-14],fill=(220,215,200)); d.polygon([(x+w*0.1,y+28),(x+w*0.5,y+4),(x+w*0.9,y+28)],fill=(180,170,155))
        for i in range(4): d.rectangle([x+w*0.2+i*w*0.15,y+30,x+w*0.25+i*w*0.15,y+h-14],fill=(200,195,180))
        d.rectangle([x+w*0.42,y+52,x+w*0.58,y+h-14],fill=(90,60,30)); d.ellipse([x+w*0.66,y+20,x+w*0.78,y+32],fill=(255,220,90))
    elif kind=="war":
        for i in range(3): d.ellipse([x+w*0.1+i*w*0.3,y+10+i*8,x+w*0.22+i*w*0.3,y+22+i*8],fill=(255,150,40))
        d.polygon([(x+w*0.08,y+h-14),(x+w*0.14,y+45),(x+w*0.26,y+45),(x+w*0.32,y+h-14)],fill=(70,70,80)); d.polygon([(x+w*0.6,y+h-14),(x+w*0.66,y+50),(x+w*0.78,y+50),(x+w*0.84,y+h-14)],fill=(60,60,70))
        d.line([x+w*0.35,y+30,x+w*0.45,y+26],fill=(200,200,200),width=2); d.ellipse([x+w*0.43,y+22,x+w*0.47,y+26],fill=(180,180,180))
    elif kind=="trophy":
        d.polygon([(x+w*0.42,y+15),(x+w*0.58,y+15),(x+w*0.55,y+45),(x+w*0.45,y+45)],fill=(255,215,0)); d.ellipse([x+w*0.38,y+12,x+w*0.62,y+28],fill=(255,215,0))
        d.rectangle([x+w*0.44,y+45,x+w*0.56,y+55],fill=(180,140,0)); d.rectangle([x+w*0.38,y+55,x+w*0.62,y+60],fill=(150,110,0))
        d.rectangle([x+w*0.10,y+62,x+w*0.18,y+h-14],fill=(0,120,60)); d.rectangle([x+w*0.82,y+62,x+w*0.90,y+h-14],fill=(200,30,30))
    elif kind=="ship":
        d.rectangle([x+w*0.1,y+52,x+w*0.9,y+64],fill=(180,60,40)); d.rectangle([x+w*0.2,y+40,x+w*0.5,y+52],fill=(220,220,220)); d.rectangle([x+w*0.55,y+44,x+w*0.8,y+52],fill=(200,200,200))
        d.rectangle([x+w*0.3,y+30,x+w*0.34,y+40],fill=(150,150,150)); d.ellipse([x+w*0.62,y+14,x+w*0.74,y+26],fill=(255,120,30))
        for i in range(3): d.line([x+w*0.1+i*w*0.3,y+h-8,x+w*0.25+i*w*0.3,y+h-8],fill=(120,180,220),width=2)
    elif kind=="chart":
        d.rectangle([x+8,y+8,x+w-8,y+h-22],fill=(255,255,255)); d.line([x+14,y+h-28,x+w-14,y+18],fill=(34,139,34),width=3)
        d.line([x+14,y+h-28,x+w-14,y+h-28],fill=(100,100,100),width=1); d.line([x+14,y+14,x+w-14,y+14],fill=(200,0,0),width=1)
        d.text((x+16,y+12),"50,018",font=F(10,True),fill=RED)
    elif kind=="server":
        for r in range(3):
            d.rectangle([x+w*0.2,y+10+r*18,x+w*0.8,y+24+r*18],fill=(40,40,50)); d.ellipse([x+w*0.24,y+14+r*18,x+w*0.28,y+20+r*18],fill=(255,40,40))
        d.rectangle([x+w*0.1,y+10,x+w*0.16,y+62],fill=(120,20,20))
    elif kind=="heli":
        d.ellipse([x+w*0.25,y+30,x+w*0.65,y+48],fill=(90,110,90)); d.ellipse([x+w*0.6,y+32,x+w*0.72,y+44],fill=(140,180,200)); d.line([x+w*0.2,y+28,x+w*0.8,y+28],fill=(60,60,60),width=3); d.line([x+w*0.65,y+38,x+w*0.9,y+38],fill=(60,60,60),width=2)
        d.polygon([(x+w*0.05,y+h-14),(x+w*0.3,y+55),(x+w*0.7,y+55),(x+w*0.95,y+h-14)],fill=(70,80,70))
    elif kind=="shop":
        d.rectangle([x+w*0.15,y+25,x+w*0.85,y+h-14],fill=(200,190,170)); d.rectangle([x+w*0.15,y+25,x+w*0.85,y+38],fill=(200,40,40)); d.rectangle([x+w*0.42,y+50,x+w*0.58,y+h-14],fill=(90,60,30))
        d.rectangle([x+w*0.22,y+45,x+w*0.34,y+58],fill=(140,200,230)); d.rectangle([x+w*0.66,y+45,x+w*0.78,y+58],fill=(140,200,230))
    elif kind=="desert":
        d.ellipse([x+w*0.7,y+10,x+w*0.85,y+25],fill=(255,220,90)); d.polygon([(x+w*0.05,y+h-14),(x+w*0.3,y+45),(x+w*0.6,y+h-14)],fill=(220,180,110)); d.polygon([(x+w*0.45,y+h-14),(x+w*0.65,y+40),(x+w*0.9,y+h-14)],fill=(200,160,90))
        d.rectangle([x+w*0.15,y+52,x+w*0.3,y+60],fill=(120,90,50))
    elif kind=="strike":
        d.ellipse([x+w*0.65,y+12,x+w*0.8,y+27],fill=(255,140,40)); d.polygon([(x+w*0.1,y+h-14),(x+w*0.2,y+50),(x+w*0.4,y+50),(x+w*0.5,y+h-14)],fill=(120,100,80)); d.polygon([(x+w*0.55,y+h-14),(x+w*0.62,y+45),(x+w*0.8,y+45),(x+w*0.88,y+h-14)],fill=(100,85,70))
        d.line([x+w*0.3,y+40,x+w*0.5,y+30],fill=(255,220,90),width=2)
    elif kind=="rocket":
        d.polygon([(x+w*0.45,y+8),(x+w*0.55,y+8),(x+w*0.58,y+40),(x+w*0.42,y+40)],fill=(230,230,230)); d.polygon([(x+w*0.45,y+8),(x+w*0.5,y-2),(x+w*0.55,y+8)],fill=(200,40,40))
        d.polygon([(x+w*0.42,y+32),(x+w*0.35,y+48),(x+w*0.42,y+40)],fill=(200,40,40)); d.polygon([(x+w*0.58,y+32),(x+w*0.65,y+48),(x+w*0.58,y+40)],fill=(200,40,40))
        d.ellipse([x+w*0.46,y+48,x+w*0.54,y+58],fill=(255,150,40)); d.ellipse([x+w*0.7,y+14,x+w*0.82,y+26],fill=(255,255,255)); d.ellipse([x+w*0.72,y+16,x+w*0.80,y+24],fill=(180,180,200))
    else:
        d.ellipse([x+w*0.7,y+10,x+w*0.85,y+25],fill=(255,220,90)); d.rectangle([x+w*0.2,y+40,x+w*0.8,y+h-14],fill=(120,140,170))

CONT=[ [(-168,66),(-140,70),(-120,71),(-95,69),(-80,73),(-65,60),(-55,52),(-60,45),(-75,35),(-80,26),(-90,21),(-97,16),(-105,20),(-115,28),(-125,40),(-125,49),(-140,60),(-165,60)], [(-80,10),(-70,12),(-60,8),(-50,0),(-40,-5),(-35,-10),(-40,-20),(-48,-28),(-58,-35),(-65,-45),(-70,-55),(-73,-40),(-72,-20),(-80,-5),(-80,5)], [(-17,15),(-10,30),(0,36),(10,37),(20,32),(32,31),(35,28),(40,15),(48,11),(51,10),(43,0),(40,-10),(35,-20),(32,-29),(25,-34),(18,-35),(12,-18),(8,4),(-8,5),(-15,11)], [(-10,36),(-9,43),(-2,48),(0,50),(5,58),(10,60),(18,69),(30,70),(40,68),(55,68),(70,72),(90,75),(110,76),(130,72),(160,70),(178,66),(170,60),(160,55),(142,50),(140,40),(130,33),(122,30),(110,20),(105,10),(100,8),(95,15),(90,22),(80,15),(75,8),(70,20),(65,25),(58,25),(52,27),(48,30),(43,12),(40,15),(35,28),(30,36),(22,36),(18,40),(12,44),(3,43),(-2,37),(-9,37)], [(113,-22),(114,-30),(115,-35),(124,-33),(129,-32),(137,-35),(140,-38),(147,-39),(150,-37),(153,-27),(146,-19),(142,-11),(136,-12),(132,-11),(126,-14),(122,-17),(114,-21)], [(-55,60),(-45,60),(-40,65),(-30,68),(-20,70),(-25,76),(-40,80),(-55,76),(-58,70)] ]
HERO=[ ("1  RIYADH · MIDDLE EAST","CONFIRMED","Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, Riyadh's tallest, for the second time in a week. (Saudi officials)","tower"), ("2  SHANGHAI · ASIA","OFFICIAL","China probes Shanghai party chief Chen Jining","Chen Jining, 62, faces a probe over serious violations. He is the fourth Politburo member investigated. (CCDI)","party"), ("3  NEW YORK · US / TECH","CONFIRMED","Huawei guilty on 10 of 12 counts","A US jury found Huawei guilty of trade-secret theft and bank fraud. It was cleared of racketeering. (US court)","court") ]
CARDS=[ ("4  ZAPORIZHZHIA · EUROPE / WAR","REPORTED","Russian attacks kill 9 across Ukraine in a day","Nine people were killed and 81 hurt as Russia launched 96 drones; 73 were shot down. (Ukraine officials)","war"), ("5  CAS · AFRICA / SPORT","OFFICIAL","CAS hands Senegal back the AFCON title","Morocco forfeited 3-0, so Senegal won 1-0 and took the title back. (CAS)","trophy"), ("6  HORMUZ · MIDDLE EAST","REPORTED","IRGC attacks container ship in Hormuz","A container ship was attacked at 18:58 UTC and its navigation was disabled near Khasab. (UKMTO)","ship"), ("7  NEW YORK · WORLD / MARKETS","CONFIRMED","Dow closes above 50,000 for the first time","The Dow closed at 50,018 while the Taiex jumped 8.99% to a record 40,122. (Market close)","chart"), ("8  REDMOND · WORLD / TECH","REPORTED","Microsoft declares 'Code Red' after historic outage","After a 24-hour outage, Microsoft targets full recovery within one hour. (Reuters)","server"), ("9  ESKISEHIR · EUROPE","REPORTED","Turkish military helicopter crash kills 5","An AS-532 military helicopter crashed in Eskisehir, killing five people. (Turkish officials)","heli"), ("10  CARTAGENA · AMERICAS","REPORTED","Supermarket hostages: 25 held in Cartagena","Twenty-five hostages were held; five elderly women were freed. (Colombian officials)","shop"), ("11  ADEN · MIDDLE EAST","REPORTED","Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of Aden in Yemen. (Wires)","desert"), ("12  LAHJ · MIDDLE EAST","REPORTED","Saudi strikes kill 25, wound 6 in Yemen","Strikes on a bus and truck in Wadi Maabaq killed or left missing 25 people. (Yemeni officials)","strike"), ("13  JIUQUAN · WORLD / SPACE","OFFICIAL","China names first foreign astronaut for Tiangong","Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali of Pakistan were named for Shenzhou-24. (CMSA)","rocket") ]
ALSO=[ (14,"Ankara: Haftar visits Turkey for first time","REPORTED"), (15,"London: UK sanctions Houthis + 4 officials","OFFICIAL"), (16,"Villavicencio: Car bomb injures 23","REPORTED"), (17,"Gaza: Israel kills Hamas internal security chief","REPORTED"), (18,"Baghdad: Iraq orders federal control of Kurdish oilfields","OFFICIAL"), (19,"Gaza: Meningitis epidemic alert, 272 cases in Oct","OFFICIAL"), (20,"DR Congo: Missing Cessna 208, rebels claim shootdown","CLAIM"), (21,"Hanoi: Hot-pot explosion kills at least 6","REPORTED"), (22,"Gulf of Finland: Ukraine hits Russian ship Sparta II","REPORTED"), (23,"Kuala Lumpur: Malaysia to return thousands of migrants","OFFICIAL"), (24,"Ulleungdo: S. Korea shelter order as Russian jets enter ADIZ","OFFICIAL"), (25,"Dhaka: Hasina plans return on 16 Dec","REPORTED"), (26,"The Hague: 14 nations endorse ICJ Myanmar ruling","REPORTED"), (27,"Jakarta: Indonesia nominates 2 VP candidates","OFFICIAL"), (28,"Beijing: China sentences official Ma to death for spying","OFFICIAL"), (29,"Brussels: NATO vows defence against space threat","OFFICIAL"), (30,"Mexico City: US drone aided El Chapo Isidro capture","REPORTED"), (31,"San Salvador: Bukele names 3 soldiers killed in Haiti","OFFICIAL"), (32,"Ottawa: Pentagon rebukes Canada, only 41.9% air fleet ready","REPORTED"), (33,"Washington: US adds Megaspeed to trade blacklist","OFFICIAL"), (34,"Kyiv: Zelensky urges Ukraine-Russia-US-Europe talks soon","REPORTED"), (35,"Ras Al Khaimah: UAE bus-truck crash kills 13","REPORTED"), (36,"London: England record 5,258 heat deaths, summer 2026","OFFICIAL"), (37,"Kourou: Ariane 6 lofts 36 Amazon satellites","OFFICIAL"), (38,"Cikande: Factory-fire toll rises to 26","REPORTED") ]
UTC=[ ("02:15","NATO vows space defence"), ("08:16","Hanoi blast"), ("10:42","Saudi strikes Yemen"), ("14:27","Riyadh tower hit"), ("16:51","Houthis 60 km from Aden"), ("18:58","Hormuz ship attack"), ("20:41","Huawei guilty") ]
NUM=[ ("11","hurt in Riyadh"), ("9","killed in Ukraine"), ("50,018","Dow close"), ("+8.99%","Taiex record"), ("25","killed in Yemen"), ("26","Cikande toll"), ("10/12","Huawei counts"), ("96","drones launched") ]
REG=[ ("Europe",9,(30,90,168)), ("Middle East",8,(178,34,34)), ("Asia",8,(34,139,34)), ("Africa",2,(200,140,20)), ("Americas",7,(120,60,140)), ("World / Space",4,(90,90,90)) ]
PINS=[ (1,24.7,46.7,-8,-8),(2,31.2,121.5,0,0),(3,40.7,-74.0,0,-14),(4,47.8,35.2,0,0),(5,14.7,-17.4,0,0),(6,26.5,56.3,0,0),(7,40.7,-74.0,-8,8),(8,47.6,-122.1,0,0),(9,39.8,30.5,0,0),(10,10.4,-75.5,0,0),(11,12.8,45.0,0,-12),(12,13.0,44.9,10,10),(13,39.7,98.5,0,0) ]
def ll(mx,my,mw,mh,lat,lon): return mx+(lon+180)/360*mw, my+(85-lat)/145*mh
def main():
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,26],fill=RED); txt(d,16,5,"THE WORLD ON ONE PAGE",F(11,True),(255,255,255)); txt(d,W-16,5,"38 STORIES  ·  6 REGIONS  ·  ALL FROM TUESDAY 24 NOVEMBER 2026",F(10,True),(255,255,255),anchor="ra")
    txt(d,W//2,34,"Tuesday 24 November 2026",F(30,serif=True),anchor="ma")
    txt(d,W//2,68,"Riyadh tower hit again  ·  Shanghai party chief probed  ·  Huawei guilty on 10 of 12 counts",F(12,serif=True),fill=RED,anchor="ma")
    x=16
    for name,n,c in REG:
        w=int(992*n/38); d.rectangle([x,92,x+w-3,108],fill=c); txt(d,x+4,95,f"{name} {n}",F(8,True),(255,255,255)); x+=w
    txt(d,16,114,"THE DAY IN UTC",F(9,True),fill=RED)
    xx=16
    for t,ev in UTC:
        txt(d,xx,126,f"{t}  {ev}",F(8),fill=NAVY); xx+=int(d.textlength(f"{t}  {ev}",font=F(8)))+22
    d.line([16,142,W-16,142],fill=(180,180,180),width=1)
    txt(d,16,146,"THE DAY IN NUMBERS",F(9,True),fill=RED)
    xx=16
    for v,lab in NUM:
        txt(d,xx,158,v,F(15,True),fill=RED); txt(d,xx,176,lab,F(7)); xx+=max(int(d.textlength(v,font=F(15,True))),int(d.textlength(lab,font=F(7))))+26
    hy=196; hw=322; hx=16
    for kick,ch,head,deck,kind in HERO:
        d.rectangle([hx,hy,hx+hw,hy+168],fill=(255,255,255),outline=(200,200,200))
        scene(d,hx+1,hy+1,hw-2,86,kind); txt(d,hx+6,hy+92,kick,F(8,True),fill=RED); chip(d,hx+6,hy+106,ch,CHIP[ch]); yy=hy+122
        for ln in wrap(d,head,F(11,True),hw-12): txt(d,hx+6,yy,ln,F(11,True)); yy+=13
        for ln in wrap(d,deck,F(8),hw-12): txt(d,hx+6,yy,ln,F(8)); yy+=10
        hx+=hw+8
    cy=374; cw=194
    for i,(kick,ch,head,deck,kind) in enumerate(CARDS):
        r=i//5; c=i%5; x=16+c*(cw+8); y=cy+r*118
        d.rectangle([x,y,x+cw,y+110],fill=(255,255,255),outline=(200,200,200))
        scene(d,x+1,y+1,cw-2,34,kind); txt(d,x+5,y+38,kick,F(7,True),fill=RED); chip(d,x+5,y+50,ch,CHIP[ch]); yy=y+64
        for ln in wrap(d,head,F(9,True),cw-10): txt(d,x+5,yy,ln,F(9,True)); yy+=11
        for ln in wrap(d,deck,F(7),cw-10): txt(d,x+5,yy,ln,F(7)); yy+=9
    my=626; mh=168; mx=16; mw=420
    txt(d,mx,my-16,"WHERE IT HAPPENED — WORLD MAP",F(10,True),fill=RED)
    d.rectangle([mx,my,mx+mw,my+mh],fill=(185,210,225),outline=(150,150,150))
    for poly in CONT:
        pts=[ll(mx,my,mw,mh,la,lo) for lo,la in poly]; d.polygon(pts,fill=(150,190,130),outline=(90,130,80))
    for n,la,lo,dx,dy in PINS:
        px,py=ll(mx,my,mw,mh,la,lo); px+=dx; py+=dy
        if dx or dy:
            bx,by=ll(mx,my,mw,mh,la,lo); d.line([bx,by,px,py],fill=RED,width=1)
        d.ellipse([px-7,py-7,px+7,py+7],fill=RED,outline=(255,255,255)); txt(d,px,py-5,str(n),F(7,True),(255,255,255),anchor="ma")
    lx=456; txt(d,lx,my-16,"PINNED STORIES",F(10,True),fill=RED)
    leg=["1 Riyadh tower","2 Shanghai probe","3 Huawei guilty","4 Ukraine 9 killed","5 Senegal AFCON","6 Hormuz ship","7 Dow 50,018","8 Microsoft Code Red","9 Eskisehir crash","10 Cartagena 25 held","11 Houthis near Aden","12 Saudi strikes Yemen","13 Tiangong astronaut"]
    for i,t in enumerate(leg):
        col=0 if i<7 else 1; row=i if i<7 else i-7; txt(d,lx+col*270,my+row*16,t,F(9))
    ay=800; txt(d,16,ay,"ALSO ON TUESDAY — 25 MORE STORIES",F(10,True),fill=RED)
    for i,(n,t,ch) in enumerate(ALSO):
        col=i//9; row=i%9; x=16+col*330; y=ay+18+row*12
        txt(d,x,y,f"{n}. {t}",F(7)); chip(d,x+int(d.textlength(f"{n}. {t}",font=F(7)))+4,y-1,ch,CHIP[ch])
    dy=928; d.rectangle([16,dy,W-16,dy+66],fill=(255,235,235),outline=RED)
    dc="DATE CHECK — Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC. LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov); Nvidia's Huang returns as CEO (23 Nov); EU 22nd sanctions package (23 Nov); COP31 ends with no deal (22 Nov); Merkury corvette sinks (22 Nov); El Chapo Isidro arrested (Fri 20 Nov); Cikande fire starts (Sat 21 Nov); Trump hush-money appeal ruling (23 Nov); ATP Finals (22 Nov); F1 Las Vegas GP (21 Nov). NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC); MPR session picks VP (11 Dec); Huawei sentencing (Sep 2027); Hasina returns (16 Dec)."
    yy=dy+4
    for ln in wrap(d,dc,F(8),W-40): txt(d,22,yy,ln,F(8)); yy+=10
    txt(d,16,1000,"Sources: dailysummaryof.com · Reuters · AP · UKMTO · CAS · CMSA · Focus Taiwan/CNA.  CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side's claim. Scenes are drawn illustrations, not photographs.",F(7))
    out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out),exist_ok=True); im.save(out,optimize=True)
if __name__=="__main__": main()
