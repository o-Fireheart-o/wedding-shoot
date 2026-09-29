# -*- coding: utf-8 -*-
"""블로그 후기 + 제휴 포트폴리오 → report/bong_sets_dresses.html

입력
- research/blog/out_indoor.json, out_outdoor.json, out_dress.json : 블로그 사진 선별 결과
- research/t2_bongstudio.md 2-A 표 : 제휴 포트폴리오 컷
"""
import re, os, html, json
from collections import OrderedDict

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(PROJ, "research/blog")
load = lambda n: json.load(open(os.path.join(BLOG, n), encoding="utf-8"))
indoor, outdoor, dress = load("out_indoor.json"), load("out_outdoor.json"), load("out_dress.json")
posts = {p["url"]: p for p in load("posts_meta.json")}  # 후기 글 제목·날짜만 (본문은 올리지 않음)
md = open(os.path.join(PROJ, "research/t2_bongstudio.md"), encoding="utf-8").read()
src = open(os.path.join(PROJ, "report/wedding_concept_report.html"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", src, re.S).group(1)

EXTRA = """
.toc{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0}
.toc a{font-size:.8rem;text-decoration:none;padding:3px 10px;border-radius:999px;background:var(--card);border:1px solid var(--line);color:var(--ink)}
.toc a:hover{background:var(--acc-s)}
.set{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:14px 0;scroll-margin-top:12px}
.set h4{margin:0;font-size:1.06rem}
.set .alias{font-size:.8rem;color:var(--mut);margin:2px 0 8px}
.set .feat{font-size:.9rem;margin:0 0 4px}
.set .tip{font-size:.84rem;margin:0 0 10px;color:#6a4a3f}
.set .tip b{color:var(--acc)}
.fee{display:inline-block;font-size:.74rem;font-weight:700;padding:1px 8px;border-radius:999px;margin-left:6px;vertical-align:2px}
.fee.free{background:var(--fact-s);color:var(--fact)}
.fee.paid{background:var(--est-s);color:var(--est)}
.strip{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px}
.ph{margin:0;display:flex;flex-direction:column;gap:4px}
.ph a.i{display:block;border-radius:8px;overflow:hidden;background:#efebe8;aspect-ratio:3/4}
.ph img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .2s}
.ph a.i:hover img{transform:scale(1.03)}
.ph .w{font-size:.76rem;line-height:1.45}
.ph .s{font-size:.7rem;color:var(--mut)}
.ph .s a{color:var(--mut)}
.ph.pf .s{color:var(--acc)}
.tier{font-size:1.02rem;margin:30px 0 4px}
ul.facts{padding-left:18px;margin:8px 0}ul.facts li{margin:3px 0;font-size:.9rem}
.srcs{columns:2 280px;font-size:.78rem;padding-left:18px}.srcs li{break-inside:avoid;margin:2px 0}
@media (max-width:560px){.strip{grid-template-columns:repeat(2,1fr)}}
"""

esc = lambda s: html.escape(str(s or ""), quote=True)
used_posts = OrderedDict()


def blog_id(url):
    m = re.search(r"blog\.naver\.com/([^/]+)/", url)
    return m.group(1) if m else ""


def pdate(p):
    d = p.get("date") or posts.get(p.get("post"), {}).get("date", "")
    m = re.match(r"(\d{4})[.\-]\s*(\d{1,2})", d)
    return f"{m.group(1)}.{int(m.group(2)):02d}" if m else ""


def blog_photo(p):
    used_posts[p["post"]] = p.get("blog_title") or posts.get(p["post"], {}).get("title", "")
    img = p["img"].split("?")[0] + "?type=w773"
    who = blog_id(p["post"])
    via = " · 인스타그램 사진 인용" if p.get("source_type") == "instagram_via_blog" else ""
    season = f" · {esc(p['season'])}" if p.get("season") else ""
    return (f'<figure class="ph"><a class="i" href="{esc(p["post"])}" target="_blank" rel="noopener">'
            f'<img loading="lazy" referrerpolicy="no-referrer" src="{esc(img)}" alt="{esc(p.get("what"))}"></a>'
            f'<figcaption><div class="w">{esc(p.get("what"))}</div>'
            f'<div class="s"><a href="{esc(p["post"])}" target="_blank" rel="noopener">{esc(who)} 블로그</a> · {pdate(p)}{season}{via}</div>'
            f'</figcaption></figure>')


# ── 제휴 포트폴리오 컷 ──────────────────────────────
PF_PAGE = "https://www.directwedding.co.kr/studio/bong"
pf = OrderedDict()
for line in md.splitlines():
    if not line.startswith("| BS-P"):
        continue
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    m = re.search(r"〈(.+?) / ", c[3])
    u = re.search(r"\((https://[^)]+)\)", c[7])
    pf.setdefault(m.group(1), []).append(dict(url=u.group(1), bg=re.sub(r"\s*〈.*", "", c[3])))
GUESS = {"반반", "화이트", "갤러리", "문앞", "야간", "프로젝터", "한화"}  # 에이전트가 추정이라고 한 매칭은 뺀다
pmap = {k: v for k, v in indoor.get("portfolio_map", {}).items() if k not in GUESS}
pf_by_key = OrderedDict()
for old, key in pmap.items():
    pf_by_key.setdefault(key, []).extend(pf.get(old, []))


def pf_photo(r):
    return (f'<figure class="ph pf"><a class="i" href="{esc(r["url"])}" target="_blank" rel="noopener">'
            f'<img loading="lazy" src="{esc(r["url"])}" alt="{esc(r["bg"])}"></a>'
            f'<figcaption><div class="w">{esc(r["bg"])}</div>'
            f'<div class="s">스튜디오 샘플 사진</div></figcaption></figure>')


# ── 세트 제목: 배경 특징으로 짓는다 (블로거 호칭은 부제로) ─────────────
TITLE = {
    # 1세트장
    "gate": "흰 박공지붕 건물의 양문 대문",
    "bigwindow": "초록 숲이 비치는 큰 통창과 흰 소파",
    "anglewindow": "여러 칸으로 꺾인 창틀",
    "smallwindow": "흰 벽에 난 작은 네모 창",
    "wood": "나뭇결 벽과 검은 가죽 소파",
    "flowerarch": "흰 꽃이 감싼 아치 홀",
    "whitearch": "나무 벽 앞 두꺼운 흰 아치",
    "greenarch": "초록 잎으로 감싼 아치 계단",
    "party": "창가의 케이크·촛불 파티 테이블",
    "whitewall": "아무것도 없는 매끈한 흰 벽",
    "hoteldoor": "몰딩이 들어간 높은 흰 양문",
    "corridor": "벽등이 이어지는 좁고 긴 복도",
    "stairs": "흰 벽이 감싸는 나선형 계단",
    "flowerwall": "보라·핑크 조화꽃이 가득한 벽",
    # 2세트장·기타
    "set2_struct": "둥근 흰 기둥과 곡선 벽",
    "set2_curtain": "흰 커튼 앞 긴 테이블",
    "set2_color": "검정·빨강 단색 벽",
    "bamboo": "대나무 터널과 전구 켜진 마당",
    "backgate": "샹들리에 달린 나무 양문과 잔디 마당",
    # 야외
    "lawn": "탁 트인 넓은 잔디밭",
    "sunset": "노을 지는 잔디밭",
    "meadow": "큰 나무가 선 풀밭",
    "road": "가로수가 늘어선 흙길",
    "forest_path": "수풀 사이 좁은 산책길",
    "bench": "나무 그늘 아래 흰 벤치",
}

# 야외 설명은 해요체로 다시 쓴다
OUT_TEXT = {
    "lawn": ("미사경정공원의 넓은 잔디밭이에요. 멀리 나무와 조명탑이 걸리고, 하늘을 크게 넣으면 화보 같은 사진이 나와요.",
             "주말에는 돗자리 편 사람이 많아서 드레스 입고 지나가기가 좀 민망했대요. 비눗방울 같은 소품을 챙겨 가면 좋고, 이동할 때는 크록스로 갈아 신어도 돼요(발은 안 보여요)."),
    "sunset": ("해 질 무렵 잔디밭과 나무 사이로 역광이 들어와서 베일과 실루엣이 금빛으로 물들어요. 흑백으로 뽑아도 분위기가 좋아요.",
               "오후 타임(2시 반 전후 시작)이어야 찍을 수 있어요. 6월에는 6시 40분쯤 나가니 해 지는 시간과 맞았대요. 작가님이 알아서 시간을 맞춰 주기도 해요."),
    "meadow": ("손질하지 않은 풀밭에 큰 나무가 서 있는 공원 안쪽이에요. '제주 애월 같다'는 후기가 나올 만큼 스냅 느낌이 강해요.",
               "풀숲이라 벌이나 무당벌레가 많아요. 누워서 찍을 때는 신랑 재킷을 깔아 줘요."),
    "road": ("공원 옆으로 큰 나무가 양쪽에 줄지어 선 흙길이에요. 손잡고 걸어오는 컷을 주로 찍어요.",
             "길이 울퉁불퉁해서 걷기 불편해요. 자칫 70~80년대 사진처럼 올드해 보였다는 후기도 있어서, 포즈를 자연스럽게 가져가는 게 좋아요."),
    "forest_path": ("스튜디오와 공원 사이, 수풀이 벽처럼 둘러싼 좁은 포장길이에요. 공원을 오가는 길에 걷는 컷을 찍어요.",
                    "여름에는 덥고 습해서 드레스가 몸에 붙어요. 푸릇한 배경을 원하면 4~5월이 좋고 장마철은 피하라는 말이 많아요."),
    "bench": ("길가 나무 그늘 아래 놓인 흰 벤치에 나란히 앉아 찍어요. 야외 첫 장면이나 쉬어 가는 장면으로 자주 들어가요.",
              "신랑은 넥타이를 빼고 단추를 하나 풀면 캐주얼하게 잘 어울린대요."),
}


def set_card(s, anchor):
    title = TITLE.get(s["key"], s["name_ko"])
    aliases = [a for a in s.get("aliases", []) if a] or [s["name_ko"]]
    w(f'<section class="set" id="{anchor}"><h4>{esc(title)}</h4>')
    w(f'<p class="alias">후기에서 부르는 이름: {esc(", ".join(aliases))}</p>')
    w(f'<p class="feat">{esc(s.get("feature"))}</p>')
    if s.get("tip"):
        w(f'<p class="tip"><b>후기 팁</b> {esc(s["tip"])}</p>')
    pfs = pf_by_key.get(s["key"], [])[:1]  # 한 줄(5칸)에 맞춘다: 블로그 4 + 샘플 1
    cells = [blog_photo(p) for p in s.get("photos", [])[:5 - len(pfs)]] + [pf_photo(r) for r in pfs]
    w('<div class="strip">' + "".join(cells) + "</div></section>")


# ── 드레스 묶음 ─────────────────────────────────────
TIERS = [
    ("추가금 없는 기본 드레스", "패키지 안에서 고를 수 있는 드레스예요. 후기를 보면 거의 다 이 중에서 1~2벌을 골랐어요.",
     ["slim_mermaid", "beads_aline", "lace_aline", "plain_aline", "shell_organza", "silk_aline_slim"]),
    ("추가금 있는 화이트 드레스", "대부분 1벌에 20만원이에요(부가세 포함 22만원).",
     ["hanyeseul", "nunkkot", "flower3d", "big_lace", "puff_sheer", "silk_halter", "drape_silk",
      "ribbon_organza", "glitter_sleeve", "lace_mermaid", "glitter_mermaid"]),
    ("색이 있는 드레스", "초록 배경이나 야외에서 눈에 확 띄어요. 대부분 20만원이고, 연두 드레스는 글마다 금액이 달라요.",
     ["drape_pink_sage", "coral", "lime_tinkerbell", "yellow_ruffle", "pink_signature", "floral_print", "purple"]),
    ("블랙 드레스", "흰 드레스 사이에 한 벌 넣으면 분위기가 확 바뀌어요. 벌마다 요금이 달라서 현장에서 물어봐야 해요.",
     ["black_aline", "black_halter", "black_square"]),
    ("그 밖의 의상", "", ["hanbok"]),
]
DNAME = {  # 드레스 제목도 생김새가 먼저 보이게
    "slim_mermaid": "몸에 붙는 실크 머메이드",
    "beads_aline": "잔잔한 비즈가 반짝이는 풍성 드레스",
    "lace_aline": "꽃 레이스를 흩뿌린 A라인",
    "plain_aline": "장식 없는 민자 튤 A라인",
    "shell_organza": "조개 모양 상의에 오간자 치마",
    "silk_aline_slim": "살짝 퍼지는 실크 슬림",
    "hanyeseul": "하트넥 튤 풍성 드레스 (일명 한예슬 드레스)",
    "nunkkot": "꽃잎 레이스 반팔 드레스 (일명 눈꽃)",
    "flower3d": "입체 꽃잎이 붙은 오프숄더 풍성",
    "big_lace": "큰 잎사귀 레이스 풍성",
    "puff_sheer": "시스루 퍼프 소매 풍성",
    "silk_halter": "실크 A라인 + 홀터넥",
    "drape_silk": "가슴 주름 실크 풍성",
    "ribbon_organza": "허리 리본 오간자 러플",
    "glitter_sleeve": "스팽글 시스루 반팔 풍성",
    "lace_mermaid": "패턴 레이스 머메이드",
    "glitter_mermaid": "스팽글 슬림 머메이드",
    "drape_pink_sage": "어깨 드레이프 풍성 (세이지 그린·연핑크)",
    "coral": "코랄빛 층층 튤",
    "lime_tinkerbell": "연두색 층층 튤 (일명 팅커벨)",
    "yellow_ruffle": "레몬색 러플 풍성",
    "pink_signature": "인디핑크 퍼프 풍성 (시그니처)",
    "floral_print": "수채화 꽃무늬 풍성",
    "purple": "연보라 러플",
    "black_aline": "블랙 끈 A라인",
    "black_halter": "블랙 홀터넥 롱드레스",
    "black_square": "블랙 스퀘어넥 리본 원피스",
    "hanbok": "한복",
}
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _dress_text import DTEXT
dtypes = {t["key"]: t for t in dress["types"]}

# 야외 'night'는 스튜디오 마당(대나무 터널·캠핑카)이라 실내 쪽 bamboo에 합친다
night = next((x for x in outdoor["scenes"] if x["key"] == "night"), None)
if night:
    outdoor["scenes"].remove(night)
    bamboo = next(x for x in indoor["sets"] if x["key"] == "bamboo")
    seen = {p["img"] for p in bamboo["photos"]}
    bamboo["photos"] += [p for p in night["photos"] if p["img"] not in seen]
    bamboo["aliases"] = list(dict.fromkeys(bamboo["aliases"] + ["캠핑카 야간씬"]))
for x in outdoor["scenes"]:
    if x["key"] in OUT_TEXT:
        x["feature"], x["tip"] = OUT_TEXT[x["key"]]

FACTS = [
    "기본은 드레스 3벌에 캐주얼 1벌이에요. 캐주얼은 직접 챙겨 가고, 드레스 3벌 중에 추가금 드레스를 섞어도 돼요.",
    "피팅은 6벌까지라고 안내받지만, 실제로는 7~9벌 입어 봤다는 후기가 많아요.",
    "추가금 드레스는 대부분 20만원(부가세 포함 22만원)이고, 블랙이나 리본 오간자처럼 10만원 선인 것도 있어요.",
    "추가금은 촬영 끝나고 원본비와 같이 한 번에 결제해요.",
    "촬영 날이 아니라 미리 가서 피팅하면 5만원이 더 붙어요.",
    "외부 드레스는 1벌 가져갈 수 있어요. 단, 지퍼형이어야 하고(끈 조임형은 안 돼요) 발목 위 길이만 돼요.",
    "같은 드레스가 한 벌씩밖에 없어서 먼저 온 팀이 먼저 골라요. 인기 많은 핑크 시그니처만 2벌 있어요.",
    "첫 드레스가 메인이라 가장 많은 배경에서 찍어요. 그래서 추가금을 쓸 거면 첫 벌에 쓰라는 조언이 많아요.",
    "추가금 드레스는 야외에서 못 입어요. 야외에는 슬림·머메이드나 가벼운 오간자, 캐주얼이 좋대요.",
    "신랑은 턱시도만 빌려줘요. 정장, 구두, 양말, 넥타이는 직접 챙겨야 해요.",
    "부케(조화·생화)와 신부 구두는 스튜디오에 있어요. 구두가 7cm 굽부터라 낮은 굽이 편하면 따로 챙기고, 누브라는 공용이라 개인 것을 가져가는 게 좋아요.",
]

# ── HTML ─────────────────────────────────────────
out = []
w = out.append
n_in = len(indoor["sets"]); n_out = len(outdoor["scenes"])
n_dress = sum(len(k) for _, _, k in TIERS)
w(f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>봉스튜디오 배경·드레스 목록</title>
<style>{CSS}{EXTRA}</style></head><body>
<header><div class="wrap">
<h1>하남 봉스튜디오 배경과 드레스 한눈에 보기</h1>
<p class="sub">여기서 직접 찍은 신부들의 블로그 후기와 스튜디오 샘플 사진 모음 · 2026년 9월 기준 · 사진을 누르면 원래 글로 이동해요</p>
</div></header>
<div class="wrap">

<div class="grid2">
<div class="card"><p class="k">실내 배경</p><p class="v">{n_in}곳</p><p class="n">1세트장에서 대부분 찍고, 2세트장은 주로 준비 공간</p></div>
<div class="card"><p class="k">야외 배경</p><p class="v">{n_out}곳</p><p class="n">걸어서 3분 거리 미사경정공원과 스튜디오 마당</p></div>
<div class="card"><p class="k">후기에 나온 드레스</p><p class="v">{n_dress}종</p><p class="n">기본 3벌 + 캐주얼 1벌, 추가금 드레스는 대부분 22만원</p></div>
</div>

<div class="note"><p><b>스튜디오 구조</b></p>
<p>하남 촬영장은 나란히 붙은 건물 두 동이에요. 흰 건물인 <b>1세트장</b>에 샘플에서 본 배경이 거의 다 있고, 파란 컨테이너 건물인 <b>2세트장</b>에서는 드레스 피팅과 헤어·메이크업을 하고 쉬어요. 야외는 걸어서 3분 거리인 미사경정공원에서 찍어요. 사진 셀렉과 앨범 수령은 강남(청담) 사무실로 가야 해요.</p></div>
<div class="note w"><p><b>보기 전에</b></p>
<p>봉스튜디오는 2024년에 세트를 새로 꾸몄어요. 그래서 사진은 2024년 이후 후기 위주로 골랐고, 스튜디오 샘플 사진 중에는 예전 세트가 섞여 있을 수 있어요. 꽃 장식과 드레스도 자주 바뀌니까 꼭 찍고 싶은 배경이나 드레스는 상담 때 사진을 보여 주고 확인해 보세요.</p></div>

<h2><span class="no">1</span>실내 배경</h2>
<p class="lede">제목은 배경 생김새대로 붙였어요. 후기에서 부르는 이름은 제목 바로 아래에 있어요.</p>
<div class="toc">""")
AREAS = ["1세트장", "2세트장", "기타"]
for s in indoor["sets"]:
    w(f'<a href="#in-{esc(s["key"])}">{esc(TITLE.get(s["key"], s["name_ko"]))}</a>')
w("</div>")
for area in AREAS:
    ss = [s for s in indoor["sets"] if s.get("area", "기타") == area]
    if not ss:
        continue
    label = {"1세트장": "1세트장 (메인 촬영장)", "2세트장": "2세트장 (준비 공간 겸 배경)", "기타": "그 밖의 공간"}[area]
    w(f'<h3>{label}</h3>')
    for s in ss:
        set_card(s, f'in-{s["key"]}')

w("""<h2><span class="no">2</span>야외 배경</h2>
<p class="lede">계절과 날씨에 따라 가장 많이 달라지는 곳이에요. 사진 아래에 찍은 달을 적어 뒀어요.</p>
<div class="toc">""")
for s in outdoor["scenes"]:
    w(f'<a href="#out-{esc(s["key"])}">{esc(TITLE.get(s["key"], s["name_ko"]))}</a>')
w("</div>")
w("""<div class="note"><p><b>야외 촬영 전에 알아둘 점</b></p><ul class="facts">
<li>비가 오면 스튜디오 드레스로는 야외에 안 나가요. 개인 의상은 괜찮아요.</li>
<li>추가금 드레스는 야외에서 못 입어요. 슬림이나 가벼운 드레스, 부드러운 색 캐주얼이 잘 어울려요.</li>
<li>6~8월은 덥고 습한 데다 벌레도 많아요. 4~5월이나 가을이 좋았다는 후기가 많아요.</li>
<li>노을과 야간 장면은 오후 타임이어야 찍을 수 있어요. 한낮에는 역광 때문에 얼굴이 어둡게 나왔다는 후기도 있어요.</li>
</ul></div>""")
for s in outdoor["scenes"]:
    set_card(s, f'out-{s["key"]}')

w("""<h2><span class="no">3</span>신부 드레스</h2>
<p class="lede">봉스튜디오는 드레스를 직접 갖고 있어서 촬영 날 입어 보고 골라요. 아래는 후기에 실제로 나온 드레스예요. 드레스는 계속 바뀌니까 마음에 드는 게 있으면 캡처해 가서 물어보세요.</p>
<div class="note"><p><b>드레스 고를 때 알아둘 점</b></p><ul class="facts">""")
for f in FACTS:
    w(f"<li>{esc(f)}</li>")
w("</ul></div>")
for tname, tdesc, keys in TIERS:
    w(f'<h3 class="tier">{esc(tname)}</h3>')
    if tdesc:
        w(f'<p class="lede">{esc(tdesc)}</p>')
    for k in keys:
        t = dtypes.get(k)
        if not t:
            continue
        free = "없음" in t["extra_fee"] and "있음" not in t["extra_fee"] and k != "black_square"
        fee_short = "추가금 없음" if free else ("요금 엇갈림" if k == "black_square" else re.sub(r"\s*[—(].*", "", t["extra_fee"]).replace("+부가세", "").strip())
        w(f'<section class="set" id="dress-{esc(k)}"><h4>{esc(DNAME.get(k, t["name_ko"]))}'
          f'<span class="fee {"free" if free else "paid"}">{esc(fee_short)}</span></h4>')
        look, review, feenote = DTEXT[k]
        w(f'<p class="alias">후기 {t["mention_count"]}편에 나옴</p>')
        w(f'<p class="feat">{esc(look)}</p>')
        w(f'<p class="tip"><b>후기 한마디</b> {esc(review)}</p>')
        if feenote:
            w(f'<p class="tip"><b>요금 참고</b> {esc(feenote)}</p>')
        w('<div class="strip">' + "".join(blog_photo(p) for p in t["photos"]) + "</div></section>")

w('<h2><span class="no">4</span>참고한 후기</h2>')
w(f'<p class="lede">사진을 가져온 블로그 글 {len(used_posts)}편이에요. 사진 저작권은 각 글쓴이에게 있고, 이 페이지는 원래 글의 사진을 링크로 불러와 보여 줄 뿐이에요. 결혼 준비 업체에서 추천 포인트를 받고 쓴 글도 섞여 있어서, 요금 같은 정보는 두 편 이상에서 똑같이 나온 것만 적었어요.</p><ol class="srcs">')
for u, t in sorted(used_posts.items(), key=lambda x: posts.get(x[0], {}).get("date", ""), reverse=True):
    w(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a> <span class="s">({esc(blog_id(u))})</span></li>')
w(f"""</ol>
<footer>
<p>스튜디오 샘플 사진: <a href="{PF_PAGE}" target="_blank" rel="noopener">다이렉트결혼준비 봉스튜디오 포트폴리오</a> · 드레스 구성: <a href="https://www.directweddingmall.com/goods/view_comp.php?ccode=WSP01540" target="_blank" rel="noopener">다이렉트웨딩몰</a> · 원자료는 <code>research/blog/</code>와 <code>research/t2_bongstudio.md</code>에 있어요.</p>
<p><a href="../index.html">← 보고서 목록</a></p>
</footer>
</div></body></html>""")

path = os.path.join(PROJ, "report/bong_sets_dresses.html")
open(path, "w", encoding="utf-8").write("\n".join(out))
print("wrote", path, "indoor", n_in, "outdoor", n_out, "dress", n_dress, "posts", len(used_posts))
