# -*- coding: utf-8 -*-
"""세미 웨딩룩 캐주얼샷 레퍼런스 → report/semi_wedding_look.html

입력: research/semiwedding/out_blog.json, out_cafe.json, out_pin.json
각 사진에 코디·소품·액세서리·포즈·장소 태그와 유사도(sim 1~3)가 붙어 있다.
"""
import re, os, html, json
from collections import Counter, OrderedDict

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(PROJ, "research/semiwedding")
src = open(os.path.join(PROJ, "report/bong_sets_dresses.html"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", src, re.S).group(1)

photos, raw_tips, seen = [], {}, set()
for name in ("out_blog.json", "out_cafe.json", "out_pin.json"):
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

B, C = "out_blog.json", "out_cafe.json"
TIPS = [
 ("옷 준비", "드레스 대신 청바지를 입을 땐 미니 원피스나 벌룬 원피스를 청바지 위에 겹쳐 입는 조합이 많아요. 싼 흰 원피스에 원래 있던 청바지를 겹쳐도 캐주얼 컷이 쉽게 나와요. 앉았을 때와 걸을 때 다리가 짧아 보이지 않는지 미리 확인하세요.", [(C,3),(B,10)]),
 ("옷 준비", "신부 옷은 쉬인, 알리, 쿠팡, 에이블리에서 싸게 모으는 경우가 많아요. 원피스 4벌을 7~8만 원에 사서 소품까지 10만 원 안팎으로 끝낸 커플도 있어요.", [(B,10)]),
 ("옷 준비", "블랙 원피스는 피로연이나 하객룩으로 다시 입을 수 있는 디자인이 좋아요. 후기에 나온 제품은 8만 원대가 많았고(안나앤로즈, 비치팜), 쿠팡 새틴 끈 원피스나 자라 롱원피스를 쓴 커플도 있어요.", [(C,1),(B,11)]),
 ("옷 준비", "신랑은 비싼 옷이 없어도 돼요. 탑텐 셋업, 무신사 와이드 셔츠, 쿠팡 1만 5,800원짜리 청남방으로 맞춘 사례가 있어요. 잔디에 앉으면 발목이 드러나니 긴 양말을 챙기세요.", [(B,12),(C,9)]),
 ("소품", "베일은 흰색과 검은색을 하나씩 준비하면 같은 옷으로 분위기를 두 번 바꿀 수 있어요. 당근마켓에서 두 개 3,000~5,000원, 스마트스토어 숏베일은 3,500~4,500원 정도예요. 집에 있는 망사 테이블보를 써도 돼요.", [(C,0),(B,18)]),
 ("소품", "부케는 다이소 조화 2,000~3,000원이면 충분해요. 꽃집에 웨딩용이라고 하면 8만 원 이상 부르는 경우가 많아서, 커플 스냅용 꽃다발로 부탁해 3만 원에 맞춘 후기가 있어요.", [(B,7),(B,8)]),
 ("소품", "올블랙은 심심해 보일 수 있어요. 리본 반묶음, 빨간 케이크, 커플 운동화처럼 포인트를 하나 넣어 주세요. 비눗방울, 풍선, 스파클러는 다이소가 가장 싸고, 신랑 손에 필름카메라를 쥐여 주면 포즈가 자연스러워져요.", [(C,2),(C,6),(B,9)]),
 ("장소", "노을공원은 캐주얼 촬영지로 인기가 많아요. 주차장 옆에서 맹꽁이 열차(왕복 3,000원)를 타고 올라가고 짐도 실을 수 있어요. 평일 오전이 한산하고, 가을엔 오후 4시쯤부터 촬영팀이 늘어요.", [(B,0),(B,1),(C,4)]),
 ("장소", "월드컵공원(노을공원 포함)에서 작가를 불러 찍는 촬영은 서울시 공공서비스예약으로 미리 신청하고 시간당 사용료를 내야 해요. 둘이 찍는 셀프 촬영은 개방 시간 안에서 금지 구역(계단, 캠핑장, 놀이터 일대)만 피하면 돼요. 신청 기한과 요금은 안내문마다 달라서 촬영 전에 최신 공고를 확인하세요.", [(C,5)]),
 ("장소", "다른 곳으로는 올림픽공원(주차 1시간 3,600원), 서래섬(반포 주차장에서 바로), 경주 고분군이 후기에 나와요. 빛은 오전 10시 전이나 오후 4시 이후가 부드러워요.", [(B,14),(B,15),(B,16),(B,13)]),
 ("셀프로 찍기", "작가 없이 찍을 땐 삼각대와 블루투스 리모컨이면 충분해요. 리모컨은 반응이 느려서 뛰는 컷은 연달아 눌러 여러 장 찍고 고르세요. 삼각대는 높이 올라가는 걸로 가져가야 전신 비율이 좋아요.", [(B,2),(B,3),(B,4)]),
 ("셀프로 찍기", "야외에서는 바람과 땀 때문에 머리와 화장이 금방 흐트러져요. 거울, 빗, 헤어스프레이, 선크림, 벌레 기피제, 보조배터리를 챙기고, 영상을 같이 찍어 두면 어색한 포즈를 확인하기 좋아요.", [(C,7),(B,17)]),
 ("셀프로 찍기", "작가 스냅으로 가볍게 찍는다면 노을공원 1시간 30분 원본 전체 제공 상품이 23만 원부터 있었어요. 베일과 부케를 빌려주는 작가도 있어요.", [(B,19),(C,11)]),
 ("포즈", "가만히 서 있기보다 달려가기, 마주 보고 웃기, 업기처럼 움직이는 포즈가 훨씬 자연스러워요. 캐주얼 옷은 드레스보다 편해서 뛰고 눕는 컷을 찍기 좋아요. 완벽한 시안을 따라 하기보다 둘이 평소 하던 장난을 떠올려 가세요.", [(B,5),(B,6),(C,14)]),
]

# 비슷한 사진을 앞에, 그다음 최근 것부터
photos.sort(key=lambda p: (-int(p.get("sim") or 1), -int(re.sub(r"\D", "", p.get("date") or "0")[:6] or 0)))

SRC_LABEL = {
    "blog": "네이버 블로그", "instagram_via_blog": "인스타그램 (블로그 인용)", "cafe": "네이버 카페", "studio": "스냅·대여 업체", "magazine": "웨딩 매거진",
    "tistory": "티스토리", "web": "웹사이트", "pinterest": "핀터레스트", "instagram": "인스타그램",
    "instagram_via_pinterest": "인스타그램 (핀터레스트 경유)",
}
SRC_GROUP = {  # 필터용으로 묶는다
    "blog": "블로그", "tistory": "블로그", "cafe": "카페", "studio": "스냅·대여 업체", "magazine": "웨딩 매거진", "web": "웹사이트",
    "pinterest": "핀터레스트", "instagram": "인스타그램", "instagram_via_blog": "인스타그램",
    "instagram_via_pinterest": "인스타그램",
}
CATS = [("look", "코디"), ("props", "소품"), ("accessories", "액세서리"), ("pose", "포즈"), ("place", "장소")]
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
SIM_LABEL = {3: "아주 비슷", 2: "조금 비슷", 1: "아이디어"}


def photo(p, i):
    tags = [t for c, _ in CATS for t in p.get(c, [])]
    group = SRC_GROUP.get(p.get("source_type"), "기타")
    data = " ".join(f'data-{c}="{esc("|".join(p.get(c, [])))}"' for c, _ in CATS)
    label = SRC_LABEL.get(p.get("source_type"), "웹")
    who = p.get("source_name") or ""
    date = f" · {esc(p['date'])}" if p.get("date") else ""
    sim = int(p.get("sim") or 1)
    chips = f'<span class="b">{SIM_LABEL[sim]}</span>' + "".join(f"<span>{esc(t)}</span>" for t in tags)
    return (f'<figure class="ph" {data} data-src="{esc(group)}" data-sim="{sim}">'
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
<title>세미 웨딩룩 레퍼런스</title>
<style>{CSS}{EXTRA}</style></head><body>
<header><div class="wrap">
<h1>세미 웨딩룩 캐주얼샷 레퍼런스</h1>
<p class="sub">청바지나 올블랙처럼 가볍게 입고 초록 잔디에서 뛰노는 느낌의 한국 사진을 블로그, 카페, 인스타그램(핀터레스트 경유)에서 모았어요 · 2026년 9월 기준 · 사진을 누르면 원래 글로 이동해요</p>
</div></header>
<div class="wrap">

<div class="grid2">
<div class="card"><p class="k">모은 사진</p><p class="v">{len(photos)}장</p><p class="n">보내주신 사진과 아주 비슷한 것 {sum(1 for p in photos if int(p.get("sim") or 1) == 3)}장, 일부 비슷한 것 {sum(1 for p in photos if int(p.get("sim") or 1) == 2)}장</p></div>
<div class="card"><p class="k">출처</p><p class="v">{n_pages}곳</p><p class="n">{esc(" · ".join(f"{k} {v}" for k, v in src_counts.most_common()))}</p></div>
<div class="card"><p class="k">보는 법</p><p class="v">태그로 거르기</p><p class="n">아래 버튼을 누르면 그 옷차림·소품·액세서리가 들어간 사진만 보여요. 여러 개를 누르면 모두 들어간 사진만 남아요.</p></div>
</div>

<div class="note"><p><b>보내주신 두 사진의 느낌</b></p><ul class="facts">
<li><a href="https://www.instagram.com/haru.zip.archive/" target="_blank" rel="noopener">@haru.zip.archive</a> (노을공원): 신랑은 연청 셔츠에 청바지, 신부는 블랙 민소매 상의에 청바지를 입었어요. 긴 생울타리 앞 잔디밭에서 서로 춤추듯 다가가는 장면을 이어 찍었어요.</li>
<li><a href="https://www.instagram.com/umlive_/" target="_blank" rel="noopener">@umlive_</a> (제주): 둘 다 올블랙이에요. 신부는 어깨 리본 블랙 롱원피스에 선글라스, 신랑은 선글라스를 머리에 올렸어요. 풀밭에 앉아 휴대폰으로 셀카를 찍고, 신부는 안개꽃 부케를 들었어요.</li>
</ul><p>공통점은 드레스 대신 편한 옷, 초록 잔디나 들판, 자연스럽게 노는 분위기예요. 사진마다 이 느낌과 얼마나 비슷한지 <b>아주 비슷·조금 비슷·아이디어</b>로 표시했어요.</p></div>

<div class="filters" id="filters">
<div class="frow"><span class="lab">보기</span><button class="chip-b" data-f="sim" aria-pressed="false">아주 비슷한 것만</button>""")
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
w('<p class="lede">블로그·카페 후기에 나온 조언을 겹치는 것끼리 묶었어요.</p>')
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
w('<div class="note"><p><b>봉스튜디오에서 찍는다면</b></p><p>봉스튜디오 기본 구성에는 개인이 준비하는 캐주얼 1벌이 들어 있어요. 스튜디오 드레스로는 비 오는 날 야외에 못 나가지만 개인 옷은 괜찮아요. 바로 옆 미사경정공원의 넓은 잔디밭과 풀밭이 이 느낌과 잘 맞아요. <a href="bong_sets_dresses.html#out-lawn">잔디밭 배경 보기</a> · <a href="bong_sets_dresses.html#out-meadow">풀밭 배경 보기</a></p></div>')

pages = OrderedDict()
for p in photos:
    pages.setdefault(p["page"], (p.get("title") or p["page"], SRC_LABEL.get(p.get("source_type"), "웹"), p.get("source_name")))
for u in tip_src:
    pages.setdefault(u, (u, "팁 출처", ""))
w(f'<h2><span class="no">+</span>출처</h2><p class="lede">사진 저작권은 각 원작자에게 있어요. 이 페이지는 원래 글의 사진을 링크로 불러와 보여 줄 뿐이고, 사진을 누르면 원래 글로 이동해요.</p><ol class="srcs">')
for u, (t, lab, who) in pages.items():
    w(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a> <span class="s">({esc(lab)}{" · " + esc(who) if who else ""})</span></li>')
w("""</ol>
<footer><p>원자료는 <code>research/semiwedding/</code>에 있어요.</p><p><a href="../index.html">← 보고서 목록</a></p></footer>
</div>
<script>
(function(){
  var CATS=['look','props','accessories','pose','place'];
  function fresh(){var o={sim:false,src:null};CATS.forEach(function(c){o[c]=[];});return o;}
  var sel=fresh();
  var figs=[].slice.call(document.querySelectorAll('#gal .ph'));
  var shown=document.getElementById('shown');
  function has(f,c,v){return (f.getAttribute('data-'+c)||'').split('|').indexOf(v)>=0;}
  function apply(){
    var n=0;
    figs.forEach(function(f){
      var ok=(!sel.sim||f.getAttribute('data-sim')==='3')&&(!sel.src||f.getAttribute('data-src')===sel.src);
      CATS.forEach(function(c){sel[c].forEach(function(v){if(!has(f,c,v))ok=false;});});
      f.hidden=!ok; if(ok)n++;
    });
    shown.textContent=n+'장 보는 중';
  }
  document.getElementById('filters').addEventListener('click',function(e){
    var b=e.target.closest('.chip-b'); if(!b)return;
    var f=b.getAttribute('data-f'),v=b.getAttribute('data-v'),on=b.getAttribute('aria-pressed')!=='true';
    if(f==='sim'){sel.sim=on;}
    else if(f==='src'){[].forEach.call(document.querySelectorAll('.chip-b[data-f=src]'),function(x){x.setAttribute('aria-pressed','false');});sel.src=on?v:null;}
    else{var a=sel[f],i=a.indexOf(v); if(on&&i<0)a.push(v); if(!on&&i>=0)a.splice(i,1);}
    b.setAttribute('aria-pressed',on?'true':'false'); apply();
  });
  document.getElementById('reset').addEventListener('click',function(){
    sel=fresh();
    [].forEach.call(document.querySelectorAll('.chip-b'),function(x){x.setAttribute('aria-pressed','false');}); apply();
  });
  apply();
})();
</script>
</body></html>""")

path = os.path.join(PROJ, "report/semi_wedding_look.html")
open(path, "w", encoding="utf-8").write("\n".join(out))
print("wrote", path, "photos", len(photos), "pages", n_pages, dict(src_counts))
