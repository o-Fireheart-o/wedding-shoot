# -*- coding: utf-8 -*-
"""샴페인샷 시안 → report/champagne_shot.html

입력: research/champagne/out_blog.json, out_cafe.json, out_web.json
각 사진에 패션·소품·액세서리 태그가 붙어 있고, 페이지에서 태그를 눌러 걸러 볼 수 있다.
"""
import re, os, html, json
from collections import Counter, OrderedDict

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(PROJ, "research/champagne")
src = open(os.path.join(PROJ, "report/bong_sets_dresses.html"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", src, re.S).group(1)

photos, raw_tips, seen = [], {}, set()
for name in ("out_blog.json", "out_cafe.json", "out_web.json"):
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        continue
    d = json.load(open(path, encoding="utf-8"))
    for p in d.get("photos", []):
        if "postfiles.pstatic.net" in p["img"] and "?" not in p["img"]:
            p["img"] += "?type=w773"
        key = re.sub(r"\?.*", "", p["img"])
        if key in seen:
            continue
        seen.add(key)
        photos.append(p)
    raw_tips[name] = d.get("tips", [])

B, C, W = "out_blog.json", "out_cafe.json", "out_web.json"
TIPS = [
 ("준비물", "비싼 샴페인은 필요 없어요. 코르크 마개가 있는 1만 원 안팎 스파클링 와인이나 까바, 프로세코면 충분해요. 첫 병은 김이 빠지기 쉬워서 2~3병은 챙겨 가요.", [(B,0),(B,3),(W,5)]),
 ("준비물", "드레스에 얼룩이 남지 않게 투명한 음료를 고르세요. 한 번 터뜨린 병에 사이다나 탄산수를 채워 흔들면 한 번 더 찍을 수 있어요.", [(B,2),(C,0),(C,1),(C,2)]),
 ("준비물", "잔에 따르는 컷은 무알콜이어도 티가 안 나요. 데미소다 애플이 샴페인 색과 가장 비슷하고, 쿨라임 피지오나 사과주스를 쓴 커플도 있어요. 음료는 직접 새로 따서 쓰세요.", [(B,4),(C,3)]),
 ("준비물", "잔은 다이소 제품으로도 그럴듯하게 나와요. 다만 가벼운 플라스틱 잔은 바람 부는 곳에서 날아갈 수 있어요. 스튜디오에 병과 잔이 있는 경우도 있으니 사기 전에 먼저 물어보세요.", [(B,5),(C,4),(B,15)]),
 ("준비물", "병은 차갑게 해 두고 햇볕에 세워 두지 마세요. 차가운 병이 더 안정적으로 터져요. 수건과 물티슈도 챙기면 좋아요.", [(W,6),(W,7)]),
 ("터뜨리는 법", "코르크를 먼저 따 두는 게 핵심이에요. 코르크가 튀는 순간만으로는 물줄기가 1초도 안 가요. 딴 병 입구를 엄지로 막고 세게 흔든 다음 엄지를 조금씩 밀어 틈을 열면 물줄기가 길게 뻗어요.", [(W,0),(W,2),(B,1)]),
 ("터뜨리는 법", "한 번에 끝내지 말고 다시 막고 흔들어서 두세 번 뿌려요. 두 번째에 표정이 더 자연스럽게 나오는 경우가 많아요.", [(W,3)]),
 ("터뜨리는 법", "병 입구는 얼굴과 카메라 쪽을 피해 위나 앞쪽 빈 공간으로 향하게 하세요. 몸을 45도쯤 틀고 사진작가 어깨 위로 뿌리면 물방울은 잘 찍히고 사람은 안전해요.", [(B,6),(W,4),(W,8)]),
 ("터뜨리는 법", "코르크 따기와 흔들어 쏘는 동작은 미리 연습해 가세요. 연습 없이 하면 신랑이 엉거주춤한 자세가 되기 쉬워요.", [(B,9),(B,10)]),
 ("찍는 법", "촬영 맨 마지막 순서로 잡으세요. 드레스와 머리가 끈적하게 젖어요. 해 질 무렵 역광으로 서면 물방울이 반짝여서 예뻐요.", [(B,7),(B,12),(W,7),(W,9),(C,5)]),
 ("찍는 법", "누가 병을 들고 다른 사람은 어디에 설지 미리 정해 두세요. 샴페인이 튀어도 손으로 얼굴을 가리지 말고 그대로 웃는다고 마음먹으면 좋아요.", [(W,11),(B,7)]),
 ("찍는 법", "물방울이 멈춘 듯 나오려면 셔터 속도를 1/500초 이상으로 빠르게 둬야 해요. 연사로 찍은 컷을 이어 붙이는 방법도 있어요.", [(W,10),(B,8)]),
 ("찍는 법", "터뜨리는 컷이 실패해도 괜찮아요. 남은 샴페인을 잔에 따라 건배하거나 병째 먹여 주는 컷, 병을 들고 걷는 컷만으로도 분위기가 살아요.", [(B,11),(W,12),(B,13)]),
 ("미리 확인", "스튜디오나 작가님께 샴페인샷이 되는지, 어느 장소에서 할지 미리 물어보세요. 공원에서는 행인이 지나가지 않는지 한 번 더 보고 터뜨려요. 튄 코르크와 호일, 빈 병은 꼭 챙겨서 치워요.", [(C,6),(B,10),(W,13)]),
]

# 벤치 사진을 앞에, 그다음 최근 것부터
photos.sort(key=lambda p: (not p.get("bench"), -int(re.sub(r"\D", "", p.get("date") or "0")[:6] or 0)))

SRC_LABEL = {
    "blog": "네이버 블로그", "instagram_via_blog": "인스타그램 (블로그 인용)", "cafe": "네이버 카페",
    "tistory": "티스토리", "web": "웹사이트", "pinterest": "핀터레스트", "instagram": "인스타그램",
    "instagram_via_pinterest": "인스타그램 (핀터레스트 경유)",
}
SRC_GROUP = {  # 필터용으로 묶는다
    "blog": "블로그", "tistory": "블로그", "cafe": "카페", "web": "해외 사이트",
    "pinterest": "핀터레스트", "instagram": "인스타그램", "instagram_via_blog": "인스타그램",
    "instagram_via_pinterest": "인스타그램",
}
CATS = [("fashion", "패션"), ("props", "소품"), ("accessories", "액세서리")]
counts = {c: Counter(t for p in photos for t in p.get(c, [])) for c, _ in CATS}
src_counts = Counter(SRC_GROUP.get(p.get("source_type"), "기타") for p in photos)
n_pages = len({p.get("page") for p in photos})

EXTRA = """
.filters{position:sticky;top:0;z-index:5;background:var(--bg);padding:10px 0 6px;border-bottom:1px solid var(--line);margin-bottom:12px}
.frow{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:4px 0}
.frow .lab{font-size:.78rem;font-weight:700;color:var(--mut);width:64px;flex:none}
.chip-b{font:inherit;font-size:.78rem;padding:3px 10px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
.chip-b[aria-pressed="true"]{background:var(--acc);border-color:var(--acc);color:#fff}
.chip-b small{opacity:.7;margin-left:3px}
.stat{font-size:.82rem;color:var(--mut);margin:6px 0 0}
.stat button{font:inherit;font-size:.78rem;border:0;background:none;color:var(--acc);cursor:pointer;text-decoration:underline}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
.gal .ph{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px}
.gal .ph[hidden]{display:none}
.tags{display:flex;flex-wrap:wrap;gap:3px;margin-top:2px}
.tags span{font-size:.66rem;padding:0 6px;border-radius:999px;background:#f3ece7;color:#6a4a3f}
.tags span.b{background:var(--fact-s);color:var(--fact)}
@media (max-width:560px){.gal{grid-template-columns:repeat(2,1fr)}.frow .lab{width:100%}}
"""

esc = lambda s: html.escape(str(s or ""), quote=True)


def photo(p, i):
    tags = [t for c, _ in CATS for t in p.get(c, [])]
    group = SRC_GROUP.get(p.get("source_type"), "기타")
    data = " ".join(f'data-{c}="{esc("|".join(p.get(c, [])))}"' for c, _ in CATS)
    label = SRC_LABEL.get(p.get("source_type"), "웹")
    who = p.get("source_name") or ""
    date = f" · {esc(p['date'])}" if p.get("date") else ""
    chips = ('<span class="b">벤치</span>' if p.get("bench") else "") + "".join(f"<span>{esc(t)}</span>" for t in tags)
    return (f'<figure class="ph" {data} data-src="{esc(group)}" data-bench="{1 if p.get("bench") else 0}">'
            f'<a class="i" href="{esc(p["page"])}" target="_blank" rel="noopener">'
            f'<img loading="lazy" referrerpolicy="no-referrer" src="{esc(p["img"])}" alt="{esc(p.get("what"))}"></a>'
            f'<figcaption><div class="w">{esc(p.get("what"))}</div><div class="tags">{chips}</div>'
            f'<div class="s"><a href="{esc(p["page"])}" target="_blank" rel="noopener">{esc(label)}{" · " + esc(who) if who else ""}</a>{date}</div>'
            f'</figcaption></figure>')


out = []
w = out.append
w(f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>샴페인샷 시안 모음</title>
<style>{CSS}{EXTRA}</style></head><body>
<header><div class="wrap">
<h1>샴페인샷 시안 모음</h1>
<p class="sub">공원 벤치에 앉아 샴페인을 터뜨리는 장면을 중심으로 블로그, 카페, 핀터레스트, 인스타그램, 해외 웨딩 사이트에서 모았어요 · 2026년 9월 기준 · 사진을 누르면 원래 글로 이동해요</p>
</div></header>
<div class="wrap">

<div class="grid2">
<div class="card"><p class="k">모은 사진</p><p class="v">{len(photos)}장</p><p class="n">벤치에 앉은 사진 {sum(1 for p in photos if p.get("bench"))}장, 나머지는 공원·야외에서 찍은 비슷한 장면</p></div>
<div class="card"><p class="k">출처</p><p class="v">{n_pages}곳</p><p class="n">{esc(" · ".join(f"{k} {v}" for k, v in src_counts.most_common()))}</p></div>
<div class="card"><p class="k">보는 법</p><p class="v">태그로 거르기</p><p class="n">아래 버튼을 누르면 그 옷차림·소품·액세서리가 들어간 사진만 보여요. 여러 개를 누르면 모두 들어간 사진만 남아요.</p></div>
</div>

<div class="note w"><p><b>벤치 사진이 적은 이유</b></p><p>벤치에 앉아서 샴페인을 터뜨린 사진은 어느 출처에서도 드물었어요. 커플 사진은 제주에서 찍은 두 쌍뿐이에요. 그래서 공원 잔디, 피크닉 돗자리, 해변, 옥상처럼 앉거나 서서 비슷하게 찍은 장면을 함께 모았어요. <b>벤치만</b> 버튼을 누르면 벤치 사진만 볼 수 있어요.</p></div>

<div class="filters" id="filters">
<div class="frow"><span class="lab">장소·출처</span><button class="chip-b" data-f="bench" aria-pressed="false">벤치만</button>""")
for k, v in src_counts.most_common():
    w(f'<button class="chip-b" data-f="src" data-v="{esc(k)}" aria-pressed="false">{esc(k)}<small>{v}</small></button>')
w("</div>")
for c, label in CATS:
    w(f'<div class="frow"><span class="lab">{label}</span>')
    for t, n in counts[c].most_common():
        w(f'<button class="chip-b" data-f="{c}" data-v="{esc(t)}" aria-pressed="false">{esc(t)}<small>{n}</small></button>')
    w("</div>")
w('<p class="stat"><span id="shown"></span> <button id="reset" type="button">필터 지우기</button></p></div>')

w('<div class="gal" id="gal">' + "".join(photo(p, i) for i, p in enumerate(photos)) + "</div>")

w('<h2><span class="no">+</span>찍기 전에 알아둘 팁</h2>')
w('<p class="lede">블로그·카페 후기와 해외 사진작가 글에 나온 조언을 겹치는 것끼리 묶었어요.</p>')
tip_src = OrderedDict()
cur = None
for group, text, refs in TIPS:
    if group != cur:
        if cur:
            w("</ul>")
        w(f'<h3>{esc(group)}</h3><ul class="facts">')
        cur = group
    for f, i in refs:
        for u in raw_tips.get(f, [])[i].get("sources", []) if i < len(raw_tips.get(f, [])) else []:
            tip_src.setdefault(u, None)
    w(f"<li>{esc(text)}</li>")
w("</ul>")
w('<div class="note"><p><b>봉스튜디오에서 찍는다면</b></p><p>스튜디오와 공원 사이 길가에 나무 그늘 아래 흰 벤치가 있어요. 야외 촬영의 첫 장면으로 자주 들어가는 곳이라 샴페인샷을 넣고 싶으면 상담 때 미리 말해 두세요. 드레스가 젖으니 순서는 야외 마지막으로 잡는 게 좋아요. <a href="bong_sets_dresses.html#out-bench">벤치 배경 사진 보기</a></p></div>')

pages = OrderedDict()
for p in photos:
    pages.setdefault(p["page"], (p.get("title") or p["page"], SRC_LABEL.get(p.get("source_type"), "웹"), p.get("source_name")))
for u in tip_src:
    pages.setdefault(u, (u, "팁 출처", ""))
w(f'<h2><span class="no">+</span>출처</h2><p class="lede">사진 저작권은 각 원작자에게 있어요. 이 페이지는 원래 글의 사진을 링크로 불러와 보여 줄 뿐이고, 사진을 누르면 원래 글로 이동해요.</p><ol class="srcs">')
for u, (t, lab, who) in pages.items():
    w(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a> <span class="s">({esc(lab)}{" · " + esc(who) if who else ""})</span></li>')
w("""</ol>
<footer><p>원자료는 <code>research/champagne/</code>에 있어요.</p><p><a href="../index.html">← 보고서 목록</a></p></footer>
</div>
<script>
(function(){
  var sel={bench:false,src:null,fashion:[],props:[],accessories:[]};
  var figs=[].slice.call(document.querySelectorAll('#gal .ph'));
  var shown=document.getElementById('shown');
  function has(f,c,v){return (f.getAttribute('data-'+c)||'').split('|').indexOf(v)>=0;}
  function apply(){
    var n=0;
    figs.forEach(function(f){
      var ok=(!sel.bench||f.getAttribute('data-bench')==='1')&&(!sel.src||f.getAttribute('data-src')===sel.src);
      ['fashion','props','accessories'].forEach(function(c){sel[c].forEach(function(v){if(!has(f,c,v))ok=false;});});
      f.hidden=!ok; if(ok)n++;
    });
    shown.textContent=n+'장 보는 중';
  }
  document.getElementById('filters').addEventListener('click',function(e){
    var b=e.target.closest('.chip-b'); if(!b)return;
    var f=b.getAttribute('data-f'),v=b.getAttribute('data-v'),on=b.getAttribute('aria-pressed')!=='true';
    if(f==='bench'){sel.bench=on;}
    else if(f==='src'){[].forEach.call(document.querySelectorAll('.chip-b[data-f=src]'),function(x){x.setAttribute('aria-pressed','false');});sel.src=on?v:null;}
    else{var a=sel[f],i=a.indexOf(v); if(on&&i<0)a.push(v); if(!on&&i>=0)a.splice(i,1);}
    b.setAttribute('aria-pressed',on?'true':'false'); apply();
  });
  document.getElementById('reset').addEventListener('click',function(){
    sel={bench:false,src:null,fashion:[],props:[],accessories:[]};
    [].forEach.call(document.querySelectorAll('.chip-b'),function(x){x.setAttribute('aria-pressed','false');}); apply();
  });
  apply();
})();
</script>
</body></html>""")

path = os.path.join(PROJ, "report/champagne_shot.html")
open(path, "w", encoding="utf-8").write("\n".join(out))
print("wrote", path, "photos", len(photos), "pages", n_pages, dict(src_counts))
