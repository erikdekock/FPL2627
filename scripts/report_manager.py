import csv, json
import sys
A=sys.argv[1] if len(sys.argv)>1 else '41757'
MGR={'41757':'Alex Imam','1218083':'R.W. de Kock'}[A]
TPL={'41757':'docs/reports/alex_template.html','1218083':'docs/reports/rw_template.html'}[A]
OUT=sys.argv[2] if len(sys.argv)>2 else '/tmp/claude-0/-home-claude/4a9f91a2-7922-5c2e-8370-59a609816362/scratchpad/alex.html'
R=[r for r in csv.DictReader(open('data/audit/rivals_gw.csv')) if r['entry']==A]
avg=[50,81,51,69,48,58,59,45,47,55]
pts=[int(r['points']) for r in R]
T={}
for r in csv.DictReader(open('data/audit/rivals_gw.csv')): T.setdefault(int(r['gw']),{})[r['manager']]=int(r['total'])
lpos=[sorted(T[g].values(),reverse=True).index(T[g][MGR])+1 for g in range(1,11)]
C=[r for r in csv.DictReader(open('data/audit/captains.csv')) if r['entry']==A]

# chart 1: bars vs average + league position
W,H=640,210; l,r_,t,b=34,40,14,26
x=lambda i:l+(W-l-r_)/10*i
bw=(W-l-r_)/10
y=lambda v:H-b-(v/120)*(H-t-b)
s=[f'<svg viewBox="0 0 {W} {H}" width="100%">']
for v in (0,40,80,120):
    s.append(f'<line x1="{l}" x2="{W-r_}" y1="{y(v)}" y2="{y(v)}" stroke="#E7DDEA"/><text x="{l-6}" y="{y(v)+3.5}" text-anchor="end" class="ax">{v}</text>')
for i,(p,a) in enumerate(zip(pts,avg)):
    col='#37003C' if p>=a else '#E90052'
    s.append(f'<rect x="{x(i)+bw*.18}" y="{y(p)}" width="{bw*.64}" height="{y(0)-y(p)}" rx="3" fill="{col}"/>')
    s.append(f'<text x="{x(i)+bw/2}" y="{y(p)-4}" text-anchor="middle" class="lb">{p}</text>')
    s.append(f'<line x1="{x(i)+bw*.1}" x2="{x(i)+bw*.9}" y1="{y(a)}" y2="{y(a)}" stroke="#00C46A" stroke-width="2.5"/>')
    s.append(f'<text x="{x(i)+bw/2}" y="{H-8}" text-anchor="middle" class="ax">GW{i+1}</text>')
# league position dots on right scale 1..10
yp=lambda p:t+ (p-1)/9*(H-t-b)
pp=" ".join(f"{x(i)+bw/2},{yp(p)}" for i,p in enumerate(lpos))
s.append(f'<polyline points="{pp}" fill="none" stroke="#04C8D8" stroke-width="2" stroke-dasharray="4 3"/>')
for i,p in enumerate(lpos): s.append(f'<circle cx="{x(i)+bw/2}" cy="{yp(p)}" r="4" fill="#04C8D8" stroke="#fff" stroke-width="1.5"/>')
for p in (1,5,10): s.append(f'<text x="{W-r_+8}" y="{yp(p)+3.5}" class="ax">P{p}</text>')
s.append('</svg>'); chart1="".join(s)

# chart 2: captain points per GW vs Haaland benchmark
W2,H2=640,150; y2=lambda v:H2-24-((v+20)/70)*(H2-34)
s=[f'<svg viewBox="0 0 {W2} {H2}" width="100%">']
for v in (-20,0,25,50):
    s.append(f'<line x1="{l}" x2="{W2-12}" y1="{y2(v)}" y2="{y2(v)}" stroke="{"#9B8AA0" if v==0 else "#E7DDEA"}"/><text x="{l-6}" y="{y2(v)+3.5}" text-anchor="end" class="ax">{v}</text>')
bw2=(W2-l-12)/10
for i,c in enumerate(C):
    v=int(c['vs_haaland']); xx=l+bw2*i
    col='#00C46A' if v>0 else ('#E90052' if v<0 else '#C9BDCC')
    top,bot=(y2(v),y2(0)) if v>=0 else (y2(0),y2(v))
    s.append(f'<rect x="{xx+bw2*.2}" y="{top}" width="{bw2*.6}" height="{max(bot-top,2)}" rx="2" fill="{col}"/>')
    s.append(f'<text x="{xx+bw2/2}" y="{(top-4) if v>=0 else (bot+11)}" text-anchor="middle" class="lb">{("+" if v>0 else "")+str(v)}</text>')
    s.append(f'<text x="{xx+bw2/2}" y="{H2-6}" text-anchor="middle" class="ax">{c["captain"].replace("B.Fernandes","Bruno").replace("João Pedro","J.Pedro")}</text>')
s.append('</svg>'); chart2="".join(s)

cap_rows="".join(f'<tr><td>GW{c["gw"]}</td><td>{c["captain"]}{" (TC)" if c["chip"]=="TC" else ""}</td><td>{c["raw"]}</td><td>{c["captain_pts"]}</td><td class="{"pos" if int(c["vs_haaland"])>0 else "neg" if int(c["vs_haaland"])<0 else ""}">{int(c["vs_haaland"]):+d}</td></tr>' for c in C)
html=open(TPL).read().replace('{{chart1}}',chart1).replace('{{chart2}}',chart2).replace('{{caprows}}',cap_rows)
open(OUT,'w').write(html)
print(lpos, sum(p-a for p,a in zip(pts,avg)))
