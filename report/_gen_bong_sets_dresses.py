# -*- coding: utf-8 -*-
"""research/t2_bongstudio.md 2-A 표 → report/bong_sets_dresses.html (배경·드레스 사진 목록)"""
import re, os, html
from collections import OrderedDict, Counter

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
md = open(os.path.join(PROJ, "research/t2_bongstudio.md"), encoding="utf-8").read()
src = open(os.path.join(PROJ, "report/wedding_concept_report.html"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", src, re.S).group(1)

EXTRA = """
.toc{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0}
.toc a{font-size:.8rem;text-decoration:none;padding:3px 10px;border-radius:999px;background:var(--card);border:1px solid var(--line);color:var(--ink)}
.toc a b{color:var(--acc);margin-left:3px;font-weight:700}
.set{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:14px 0;scroll-margin-top:12px}
.set h4{margin:0 0 2px;font-size:1.02rem}
.set .meta{font-size:.8rem;color:var(--mut);margin:0 0 10px}
.strip{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.strip a{display:block;border-radius:8px;overflow:hidden;background:#efebe8}
.strip img{width:100%;height:210px;object-fit:cover;display:block;transition:transform .2s}
.strip a:hover img{transform:scale(1.03)}
.set .d{font-size:.84rem;margin:10px 0 0;color:var(--mut)}
.set .d b{color:var(--ink);font-weight:600}
.cnt{font-size:.74rem;font-weight:700;color:var(--acc);margin-left:6px}
@media (max-width:560px){.strip{grid-template-columns:repeat(2,1fr)}.strip img{height:180px}}
"""

SRC_PAGE = "https://www.directwedding.co.kr/studio/bong"
SRC_MALL = "https://www.directweddingmall.com/goods/view_comp.php?ccode=WSP01540"
SRC_KG = "https://kgwed.com/%EB%B4%89%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4-%ED%86%A0%ED%83%88%EC%9B%A8%EB%94%A9%EC%B4%AC%EC%98%81-%EA%B0%80%EA%B2%A9-%EB%B9%84%EC%9A%A9-%EA%B2%AC%EC%A0%81/"
SRC_W21 = "https://www.wedding21.co.kr/news/articleView.html?idxno=302097"
SRC_HOME = "http://studiobong.com/"

# ── 2-A 표 파싱 ─────────────────────────────────────────
rows = []
for line in md.splitlines():
    if not line.startswith("| BS-P"):
        continue
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    m = re.search(r"〈(.+?) / (.+?)〉", c[3])
    u = re.search(r"\((https://[^)]+)\)", c[7])
    rows.append(dict(id=c[0], cat=c[2], bg=re.sub(r"\s*〈.*", "", c[3]), set=m.group(1),
                     pose=c[4], outfit=c[5], season=c[6], url=u.group(1)))

CAT_ORDER = ["모던·미니멀", "자연광·창가 로맨틱", "플라워·로맨틱 세트", "야외 숲·가든",
             "캐주얼·라이프스타일", "클래식·엔틱"]
CAT_DESC = {
    "모던·미니멀": "화이트 벽·구조물·조명 위주의 깔끔한 실내 세트",
    "자연광·창가 로맨틱": "큰 창으로 들어오는 자연광을 쓰는 실내 세트",
    "플라워·로맨틱 세트": "꽃·아치·테이블 장식이 중심인 연출 세트",
    "야외 숲·가든": "스튜디오 바로 옆 숲길·잔디밭·정원",
    "캐주얼·라이프스타일": "풍선·피켓 등 소품을 들고 노는 캐주얼 컷",
    "클래식·엔틱": "야간 조명·엔틱 소품의 클래식한 분위기",
}

sets = OrderedDict()
for r in rows:
    if r["set"] == "클업":  # 클로즈업 컷 태그 — 세트가 아님
        continue
    sets.setdefault(r["set"], []).append(r)

by_cat = OrderedDict((c, []) for c in CAT_ORDER)
for name, rs in sets.items():
    by_cat.setdefault(rs[0]["cat"], []).append((name, rs))
for c in by_cat:
    by_cat[c].sort(key=lambda x: -len(x[1]))

# ── 드레스 실루엣 분류 (신부 의상 설명의 키워드 기준) ────────────
DRESS = [
    ("black", "블랙 드레스", "블랙 새틴·블랙 롱드레스. 화이트 드레스 사이에 넣는 반전 컷용", lambda s: "블랙" in s),
    ("slip", "슬립·민소매 슬림", "장식 없이 몸선을 따라 떨어지는 슬립·민소매 드레스. 화관·두건과 잘 어울림",
     lambda s: "슬립" in s or "민소매" in s),
    ("mermaid", "머메이드", "상체와 골반을 잡고 무릎 아래로 퍼지는 실루엣", lambda s: "머메이드" in s),
    ("satin", "새틴 슬림·롱베일", "광택 있는 새틴 소재의 슬림 라인. 롱베일과 함께 연출", lambda s: "새틴" in s),
    ("tiered", "티어드·하이로우", "층층이 러플을 쌓은 티어드, 앞이 짧고 뒤가 긴 하이로우", lambda s: "티어드" in s or "하이로우" in s),
    ("volume", "화이트 볼륨·A라인", "허리부터 크게 퍼지는 풍성한 볼륨 드레스. 가장 클래식한 본식 느낌",
     lambda s: "볼륨" in s and "튤" not in s),
    ("offtulle", "튤·오프숄더", "어깨를 드러낸 오프숄더에 가벼운 튤 스커트", lambda s: "오프숄더" in s),
    ("tulle", "튤·러플 (크림·아이보리 포함)", "얇은 망사를 겹친 튤·러플. 크림·아이보리 톤도 포함", lambda s: "튤" in s or "러플" in s),
    ("other", "기타 화이트·베일 연출", "설명상 실루엣이 특정되지 않은 화이트 드레스 + 베일 컷", lambda s: True),
]
dress = OrderedDict((k, []) for k, *_ in DRESS)
for r in rows:
    bride = r["outfit"].split(",")[0]
    if not bride.startswith("신부"):
        continue  # 신랑만 보이는 컷
    for k, _, _, test in DRESS:
        if test(bride):
            dress[k].append(r)
            break

ACC = [
    ("롱베일", lambda s: "베일" in s),
    ("화관", lambda s: "화관" in s),
    ("레이스 두건", lambda s: "두건" in s),
    ("꽃 코사지", lambda s: "코사지" in s),
]


def esc(s):
    return html.escape(s, quote=True)


def img(r, alt):
    return (f'<a href="{esc(r["url"])}" target="_blank" rel="noopener">'
            f'<img loading="lazy" src="{esc(r["url"])}" alt="{esc(alt)}"></a>')


# ── HTML ───────────────────────────────────────────────
n_sets = len(sets)
n_cuts = sum(len(v) for v in sets.values())
out = []
w = out.append
w(f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>봉스튜디오 배경·드레스 목록</title>
<style>{CSS}{EXTRA}</style></head><body>
<header><div class="wrap">
<h1>하남 봉스튜디오 촬영 배경 · 신부 드레스 목록</h1>
<p class="sub">제휴 포트폴리오 사진 {n_cuts}컷을 세트별·드레스 스타일별로 정리 · 조사일 2026-09-20 · 사진을 누르면 원본이 열립니다</p>
</div></header>
<div class="wrap">

<div class="grid2">
<div class="card"><p class="k">확인된 배경(세트)</p><p class="v">{n_sets}개</p><p class="n">실내 200평 세트장 + 바로 옆 숲길 야외 <span class="chip c-fact">사실</span></p></div>
<div class="card"><p class="k">기본 의상 구성</p><p class="v">드레스 3 + 캐주얼 1 + 한복 1~2</p><p class="n">추가 1벌당 10만원 <span class="chip c-fact">사실</span></p></div>
<div class="card"><p class="k">드레스 제공</p><p class="v">스튜디오 보유</p><p class="n">"샘플에 나오는 드레스 및 턱시도 소품 대다수 보유" · 개인 의상 지참도 가능 <span class="chip c-fact">사실</span></p></div>
</div>

<div class="note w"><p><b>보기 전에 알아둘 점</b></p>
<p>세트 이름은 포트폴리오 이미지 파일명 앞부분(예: <code>통창</code>, <code>합판벽</code>)에서 읽은 것입니다. 스튜디오가 공식으로 쓰는 명칭과 다를 수 있습니다. 샘플이 갱신되면서 없어진 세트가 있을 수 있고, 야외 세트는 계절과 날씨에 따라 모습이 크게 달라집니다. 예약 상담 때 <b>현재 운영 중인 세트</b>인지 꼭 확인하세요.</p></div>

<h2><span class="no">1</span>촬영 배경(세트) {n_sets}종</h2>
<p class="lede">분위기별로 묶었고, 같은 분위기 안에서는 사진이 많은 세트부터 보여 줍니다.</p>
<div class="toc">""")
for c, items in by_cat.items():
    for name, rs in items:
        w(f'<a href="#set-{esc(name)}">{esc(name)}<b>{len(rs)}</b></a>')
w("</div>")

for c, items in by_cat.items():
    if not items:
        continue
    w(f'<h3>{esc(c)} <span class="cnt">{len(items)}개 세트</span></h3>')
    w(f'<p class="lede">{esc(CAT_DESC.get(c, ""))}</p>')
    for name, rs in items:
        r0 = rs[0]
        seasons = sorted({r["season"] for r in rs})
        w(f'<section class="set" id="set-{esc(name)}"><h4>{esc(name)}<span class="cnt">사진 {len(rs)}장</span></h4>')
        w(f'<p class="meta">{esc(r0["bg"])} · {esc(" / ".join(seasons))}</p>')
        w('<div class="strip">' + "".join(img(r, f"{name} 세트 {r['id']}") for r in rs[:6]) + "</div>")
        w(f'<p class="d"><b>대표 구도</b> {esc(r0["pose"])} &nbsp;·&nbsp; <b>의상</b> {esc(r0["outfit"])}</p>')
        w("</section>")

w(f"""<p class="lede">사진 출처: <a href="{SRC_PAGE}" target="_blank" rel="noopener">다이렉트결혼준비 봉스튜디오 포트폴리오</a>. 연도별 공식 샘플은 <a href="{SRC_HOME}" target="_blank" rel="noopener">공식 홈페이지 갤러리</a>(2014~2024, 13개 시리즈)에서 볼 수 있습니다.</p>

<h2><span class="no">2</span>신부 드레스</h2>
<div class="note"><p><b>스튜디오가 드레스를 직접 갖고 있습니다</b> <span class="chip c-fact">사실</span></p>
<p>봉스튜디오는 샘플 사진에 나오는 드레스와 턱시도를 대부분 보유하고 있습니다. 기본 구성은 <b>화이트 드레스 3벌, 캐주얼 1벌, 한복 1~2벌</b>이고, 기본 벌 수를 넘기면 1벌당 10만원이 추가됩니다. 원하면 개인 의상을 가져가도 됩니다. 다른 제휴사는 "최대 4벌(드레스 3 + 자유 1)"로 안내하므로, 계약하는 패키지 조건을 확인하세요.</p>
<p>출처: <a href="{SRC_MALL}" target="_blank" rel="noopener">다이렉트웨딩몰 상품 안내</a> · <a href="{SRC_KG}" target="_blank" rel="noopener">KG웨딩</a> · <a href="{SRC_W21}" target="_blank" rel="noopener">웨딩21 기사</a></p></div>
<div class="note w"><p><b>아래 목록은 드레스 재고표가 아닙니다</b> <span class="chip c-est">추정</span></p>
<p>드레스 모델명·브랜드 목록은 공개된 자료가 없습니다. 아래는 포트폴리오 사진에서 <b>실제로 입은 드레스</b>를 실루엣별로 나눈 것입니다. 같은 드레스가 지금도 있는지는 상담 때 사진을 보여 주고 확인하세요.</p></div>
<div class="toc">""")
for k, label, *_ in DRESS:
    if dress[k]:
        w(f'<a href="#dress-{k}">{esc(label)}<b>{len(dress[k])}</b></a>')
w("</div>")

for k, label, desc, _ in DRESS:
    rs = dress[k]
    if not rs:
        continue
    # 세트가 겹치지 않게 골라 최대 6장
    seen, pick = set(), []
    for r in rs:
        if r["set"] not in seen:
            seen.add(r["set"]); pick.append(r)
    for r in rs:
        if len(pick) >= 6:
            break
        if r not in pick:
            pick.append(r)
    pick = pick[:6]
    variants = Counter(r["outfit"].split(",")[0].replace("신부 ", "") for r in rs)
    set_names = sorted({r["set"] for r in rs})
    w(f'<section class="set" id="dress-{k}"><h4>{esc(label)}<span class="cnt">사진 {len(rs)}장</span></h4>')
    w(f'<p class="meta">{esc(desc)}</p>')
    w('<div class="strip">' + "".join(img(r, f"{label} · {r['set']} 세트") for r in pick) + "</div>")
    w(f'<p class="d"><b>사진 속 표현</b> {esc(" / ".join(v for v, _ in variants.most_common()))}</p>')
    w(f'<p class="d"><b>찍힌 세트</b> {esc(", ".join(set_names))}</p>')
    w("</section>")

w('<h3>함께 쓴 헤드피스·소품</h3><div class="tw"><table><thead><tr><th>소품</th><th>사진 수</th><th>찍힌 세트</th></tr></thead><tbody>')
for name, test in ACC:
    rs = [r for r in rows if test(r["outfit"].split(",")[0])]
    if rs:
        w(f'<tr><td>{esc(name)}</td><td class="num">{len(rs)}</td><td>{esc(", ".join(sorted({r["set"] for r in rs})))}</td></tr>')
w("</tbody></table></div>")

w(f"""<footer>
<p>데이터: <code>research/t2_bongstudio.md</code> 2-A 표(제휴 포트폴리오 {len(rows)}컷, hook.md 검증 PASS). 세트 이름은 이미지 파일명 기준이고, 드레스 분류는 사진 설명의 키워드로 나눈 것입니다(추정). 사진 저작권은 봉스튜디오와 원 게시처에 있으며, 이 페이지는 원본 링크만 걸어 보여 줍니다.</p>
<p><a href="../index.html">← 보고서 목록</a></p>
</footer>
</div></body></html>""")

path = os.path.join(PROJ, "report/bong_sets_dresses.html")
open(path, "w", encoding="utf-8").write("\n".join(out))
print("wrote", path, "sets", n_sets, "cuts", n_cuts, {k: len(v) for k, v in dress.items()})
