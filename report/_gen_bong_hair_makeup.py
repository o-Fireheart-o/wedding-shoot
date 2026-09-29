# -*- coding: utf-8 -*-
"""블로그 후기 → report/bong_hair_makeup.html (신랑·신부 헤어·메이크업)

입력: research/blog/out_hair.json, out_makeup.json, out_groom.json, posts_meta.json
"""
import re, os, html, json
from collections import OrderedDict

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(PROJ, "research/blog")
load = lambda n: json.load(open(os.path.join(BLOG, n), encoding="utf-8"))
hair, makeup, groom = load("out_hair.json"), load("out_makeup.json"), load("out_groom.json")
posts = {p["url"]: p for p in load("posts_meta.json")}
src = open(os.path.join(PROJ, "report/bong_sets_dresses.html"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", src, re.S).group(1)  # 배경·드레스 페이지와 같은 모양

EXTRA = """
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin:14px 0}
.two .card ul{margin:6px 0 0;padding-left:18px}.two .card li{font-size:.88rem;margin:3px 0}
.opt td:first-child{font-weight:700;white-space:nowrap}
.opt td{font-size:.84rem}
"""

esc = lambda s: html.escape(str(s or ""), quote=True)
used_posts = OrderedDict()


def blog_id(url):
    m = re.search(r"blog\.naver\.com/([^/]+)/", url or "")
    return m.group(1) if m else ""


def pdate(p):
    d = p.get("date") or posts.get(p.get("post"), {}).get("date", "")
    m = re.match(r"(\d{4})[.\-]\s*(\d{1,2})", d)
    return f"{m.group(1)}.{int(m.group(2)):02d}" if m else ""


def cite(urls):
    for u in urls or []:
        used_posts.setdefault(u, posts.get(u, {}).get("title", ""))


def blog_photo(p):
    used_posts[p["post"]] = p.get("blog_title") or posts.get(p["post"], {}).get("title", "")
    img = p["img"].split("?")[0] + "?type=w773"
    what = re.sub(r"\s*\([^)]*[a-z_]{3,}[^)]*\)", "", p.get("what") or "")  # 블로거 아이디 괄호 제거
    return (f'<figure class="ph"><a class="i" href="{esc(p["post"])}" target="_blank" rel="noopener">'
            f'<img loading="lazy" referrerpolicy="no-referrer" src="{esc(img)}" alt="{esc(what)}"></a>'
            f'<figcaption><div class="w">{esc(what)}</div>'
            f'<div class="s"><a href="{esc(p["post"])}" target="_blank" rel="noopener">{esc(blog_id(p["post"]))} 블로그</a> · {pdate(p)}</div>'
            f'</figcaption></figure>')


def card(title, rows, photos, anchor, count=None):
    w(f'<section class="set" id="{anchor}"><h4>{esc(title)}</h4>')
    if count:
        w(f'<p class="alias">후기 {count}편에 나옴</p>')
    for label, text in rows:
        if not text:
            continue
        if label:
            w(f'<p class="tip"><b>{esc(label)}</b> {esc(text)}</p>')
        else:
            w(f'<p class="feat">{esc(text)}</p>')
    if photos:
        w('<div class="strip">' + "".join(blog_photo(p) for p in photos[:5]) + "</div>")
    w("</section>")


def bullets(items):
    w('<ul class="facts">')
    for it in items:
        text = it["text"] if isinstance(it, dict) else it
        cite(it.get("sources") if isinstance(it, dict) else None)
        w(f"<li>{esc(text)}</li>")
    w("</ul>")


out = []
w = out.append
styles, opts, looks = hair["styles"], hair["change_options"], makeup["looks"]
w(f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>봉스튜디오 헤어·메이크업</title>
<style>{CSS}{EXTRA}</style></head><body>
<header><div class="wrap">
<h1>하남 봉스튜디오 신랑·신부 헤어·메이크업</h1>
<p class="sub">여기서 직접 찍은 신부들의 블로그 후기 모음 · 2026년 9월 기준 · 사진을 누르면 원래 글로 이동해요</p>
</div></header>
<div class="wrap">

<div class="grid2">
<div class="card"><p class="k">후기에 나온 헤어</p><p class="v">{len(styles)}가지</p><p class="n">드레스를 갈아입을 때마다 바꾸려면 헤어변형을 따로 신청해요</p></div>
<div class="card"><p class="k">헤어변형 선택지</p><p class="v">{len(opts)}가지</p><p class="n">스튜디오 기본, 스튜디오 내부 변형, 외부 출장 업체</p></div>
<div class="card"><p class="k">메이크업 스타일</p><p class="v">{len(looks)}가지</p><p class="n">토탈 패키지에 들어 있고, 2층 헤메샵에서 받아요</p></div>
</div>

<h2><span class="no">1</span>촬영 날 헤메는 이렇게 진행돼요</h2>""")
bullets(makeup["facts"])
if makeup.get("room_photos"):
    w('<div class="strip">' + "".join(blog_photo(p) for p in makeup["room_photos"][:5]) + "</div>")

w('<h2><span class="no">2</span>신부 헤어 스타일</h2>')
w('<p class="lede">후기에서 실제로 한 스타일을 모았어요. 마음에 드는 사진을 캡처해 가서 보여 주면 가장 정확해요.</p><div class="toc">')
for s in styles:
    w(f'<a href="#hair-{esc(s["key"])}">{esc(s["name_ko"])}</a>')
w("</div>")
for s in styles:
    card(s["name_ko"], [("", s.get("look")), ("어울린 드레스·배경", s.get("pairs_with")), ("후기 한마디", s.get("review"))],
         s.get("photos"), f'hair-{s["key"]}', s.get("mention_count"))

w('<h2><span class="no">3</span>헤어변형, 어떻게 할까요</h2>')
w('<p class="lede">기본 헤어는 한 가지로 끝까지 가요. 드레스마다 머리를 바꾸고 싶으면 스튜디오 안에서 추가하거나 외부 출장 업체를 불러요. 가격은 후기에 적힌 때 기준이라 지금은 다를 수 있어요.</p>')
w('<div class="tw"><table class="opt"><thead><tr><th>선택지</th><th>가격</th><th>진행 방식</th><th>좋았던 점</th><th>아쉬운 점</th></tr></thead><tbody>')
for o in opts:
    cite(o.get("sources"))
    w(f'<tr><td>{esc(o["name_ko"])}</td><td>{esc(o.get("price"))}</td><td>{esc(o.get("how"))}</td><td>{esc(o.get("good"))}</td><td>{esc(o.get("bad"))}</td></tr>')
w("</tbody></table></div>")
if hair.get("tips"):
    w('<div class="note"><p><b>헤어 팁</b></p>')
    bullets(hair["tips"])
    w("</div>")

w('<h2><span class="no">4</span>신부 메이크업</h2>')
for s in looks:
    card(s["name_ko"], [("", s.get("look")), ("후기 한마디", s.get("review"))], s.get("photos"), f'mk-{s["key"]}', s.get("mention_count"))
w('<div class="two"><div class="card"><p class="k">좋았다는 점</p>')
bullets(makeup.get("good", []))
w('</div><div class="card"><p class="k">아쉬웠다는 점</p>')
bullets(makeup.get("bad", []))
w("</div></div>")

w('<h2><span class="no">5</span>신랑 헤어·메이크업</h2>')
w('<p class="lede">신랑 헤어·메이크업도 토탈 패키지에 들어 있어요. 헤어 스타일 고르는 법은 <a href="groom_hairstyle_report.html">신랑 헤어스타일 순위 보고서</a>에 더 자세히 있어요.</p>')
w('<h3>헤어 스타일</h3>')
for s in groom["hair"]:
    card(s["name_ko"], [("", s.get("look")), ("후기 한마디", s.get("review"))], s.get("photos"), f'gh-{s["key"]}', s.get("mention_count"))
w('<h3>메이크업</h3>')
bullets(groom.get("makeup", []))
if groom.get("makeup_photos"):
    w('<div class="strip">' + "".join(blog_photo(p) for p in groom["makeup_photos"][:5]) + "</div>")
w('<h3>진행 방식과 준비</h3>')
bullets(groom.get("facts", []) + groom.get("tips", []))
w('<div class="two"><div class="card"><p class="k">좋았다는 점</p>')
bullets(groom.get("good", []))
w('</div><div class="card"><p class="k">아쉬웠다는 점</p>')
bullets(groom.get("bad", []))
w("</div></div>")

w('<h2><span class="no">6</span>참고한 후기</h2>')
w(f'<p class="lede">참고한 블로그 글 {len(used_posts)}편이에요. 사진 저작권은 각 글쓴이에게 있고, 이 페이지는 원래 글의 사진을 링크로 불러와 보여 줄 뿐이에요. 외부 헤어변형 업체 후기 중에는 업체 추천 포인트를 받고 쓴 글도 있어요.</p><ol class="srcs">')
for u, t in sorted(used_posts.items(), key=lambda x: posts.get(x[0], {}).get("date", ""), reverse=True):
    w(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t or u)}</a> <span class="s">({esc(blog_id(u))})</span></li>')
w("""</ol>
<footer>
<p>원자료는 <code>research/blog/out_hair.json</code>, <code>out_makeup.json</code>에 있어요.</p>
<p><a href="../index.html">← 보고서 목록</a></p>
</footer>
</div></body></html>""")

path = os.path.join(PROJ, "report/bong_hair_makeup.html")
open(path, "w", encoding="utf-8").write("\n".join(out))
print("wrote", path, "styles", len(styles), "options", len(opts), "looks", len(looks), "posts", len(used_posts))
