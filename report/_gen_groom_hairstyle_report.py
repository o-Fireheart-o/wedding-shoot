# -*- coding: utf-8 -*-
import re, os

PROJ = r"C:/Users/taehoonlee/orca/projects/뜔희와 튤훈의 웨딩촬영♥️"
src = open(os.path.join(PROJ, "report/wedding_concept_report.html"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", src, re.S).group(1)

EXTRA = """
.rank{font-weight:700;color:var(--acc);font-variant-numeric:tabular-nums;font-size:1.05rem}
.bar{display:inline-block;height:9px;border-radius:5px;background:var(--acc);vertical-align:middle;margin-right:7px}
figure img.tall{height:300px;object-fit:cover;object-position:center 15%}
.tag{display:inline-block;font-size:.7rem;padding:1px 6px;border-radius:5px;background:#f1eae6;color:var(--mut);border:1px solid var(--line)}
.noimg{height:300px;display:flex;align-items:center;justify-content:center;background:repeating-linear-gradient(45deg,#f4efec,#f4efec 9px,#efe8e4 9px,#efe8e4 18px);color:var(--mut);font-size:.82rem;text-align:center;padding:0 18px}
"""

IMG = {
 "az1": "https://contents.glity.link/beauty-magazine/336_1_img_1080.jpg",
 "azc1": "https://t1.daumcdn.net/news/202310/23/style_ade/20231023165011762tdkj.png",
 "azc2": "https://t1.daumcdn.net/news/202310/23/style_ade/20231023165012392uesl.jpg",
 "garma": "https://contents.glity.link/beauty-magazine/336_18_img_375x375.jpg",
 "gail": "https://t1.daumcdn.net/news/202310/23/style_ade/20231023165015950qxny.png",
 "poma": "https://t1.daumcdn.net/news/202310/23/style_ade/20231023165010251fgew.png",
 "shadow1": "https://contents.glity.link/beauty-magazine/336_33_img_375x375.jpg",
 "shadow2": "https://contents.glity.link/beauty-magazine/336_40_img_375x375.jpg",
 "bong1": "https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b607d82c5bda7f740787_%EB%98%A5%EA%B0%95%EC%95%84%EC%A7%801R1A4735-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif",
 "bong2": "https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b64b14903fb4e4164830_%ED%81%B4%EC%97%85L1190665-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif",
}
BONGSRC = "https://www.directwedding.co.kr/studio/bong"

S = {
 "ade": "https://v.daum.net/v/1E7ogzC2dg",
 "avodo": "https://avodoliving.com/79",
 "choice": "https://choicehalls.com/blog/2022/11/01/%ec%96%bc%ea%b5%b4%ed%98%95-%eb%b3%84-%ec%98%88%eb%b9%84%ec%8b%a0%eb%9e%91-%ed%97%a4%ec%96%b4%ec%8a%a4%ed%83%80%ec%9d%bc-%ec%b6%94%ec%b2%9c-4%ea%b0%80%ec%a7%80/",
 "mame": "https://mamedene.com/magazines/336",
 "ohman": "https://ohmanbeauty.imweb.me/Blog/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=169252423&t=board",
 "wheal": "https://weddingheal.com/men-wedding-hair-style/",
 "threads": "https://www.threads.com/@commab91/post/DQ6g4iAk-D7/",
 "micol": "https://micolwife.com/%EC%8B%A0%EB%9E%91-%EC%9B%A8%EB%94%A9-%ED%97%A4%EC%96%B4%EC%8A%A4%ED%83%80%EC%9D%BC-%EC%B6%94%EC%B2%9C%EA%B3%BC-%EC%96%BC%EA%B5%B4%ED%98%95%EB%B3%84-%EA%B0%80%EC%9D%B4%EB%93%9C/",
 "visio": "https://visioai.app/ko/blog/namja-peom-jongryu/",
 "vsalon": "https://visualsalon.co.kr/hair-beauty-contents/?bmode=view&idx=170190451",
}

def a(k, t):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (S[k], t)

RANK = [
 (1, "애즈펌", "시스루 애즈펌 · 내추럴 애즈", 7, "촬영·본식 공통",
  "이마를 살짝만 덮으며 앞으로 흐르는 자연스러운 컬. 가장 많은 출처가 신랑 헤어로 첫손에 꼽았다."),
 (2, "가르마펌", "애즈 가르마펌 · 가르마 레이어컷", 6, "촬영·본식 공통",
  "가르마를 확실히 열어 이마가 절반쯤 보인다. 애즈펌보다 또렷하고 지적인 인상."),
 (3, "가일컷", "가일펌 · 반까꿍 · 세미포마드", 5, "촬영 현장 최다",
  "한쪽은 넘기고 한쪽은 내린다. 포마드의 부담을 덜면서 이목구비를 드러내는 절충안."),
 (4, "포마드", "올백 · 슬릭백", 4, "본식 선호",
  "이마를 완전히 드러내 카리스마와 격식을 준다. 어두운 홀·호텔 웨딩과 궁합."),
 (4, "리젠트", "리젠트컷 · 업스타일 컷", 4, "본식 선호",
  "옆은 짧게, 앞머리는 위로 올린다. 도시적이고 단정한 인상."),
 (6, "댄디컷", "레이어 댄디 · 내추럴 다운", 3, "촬영 선호",
  "펌 없이 레이어와 질감으로 정리. 2026 트렌드 기사들이 공통으로 짚은 방향."),
 (6, "쉐도우펌", "S컬 웨이브 펌", 3, "촬영 선호",
  "전체에 S컬을 넣어 인상을 부드럽게. 길이가 충분해야 예쁘게 나온다."),
 (8, "사이드 파트", "6:3 · 7:3 가르마 컷", 2, "본식 선호",
  "펌 없이 커트와 드라이만으로 내는 단정한 가르마. 가르마펌의 무(無)펌 버전."),
]

rows = []
for r, name, alias, n, tag, desc in RANK:
    w = int(n / 7.0 * 118)
    rows.append(
        '<tr><td class="num"><span class="rank">%d</span></td>\n'
        '<td><strong>%s</strong><br><span class="lede" style="font-size:.79rem">%s</span></td>\n'
        '<td class="num"><span class="bar" style="width:%dpx"></span>%d</td>\n'
        '<td><span class="tag">%s</span></td><td>%s</td></tr>' % (r, name, alias, w, n, tag, desc))
TABLE = "\n".join(rows)

def fig(img, cap, desc, chk, src_html, cls="tall"):
    if img:
        media = '<img class="%s" src="%s" alt="%s" loading="lazy">' % (cls, img, cap)
    else:
        media = '<div class="noimg">검증된 공개 이미지를 찾지 못해<br>사진을 싣지 않았습니다</div>'
    return ('<figure>%s<figcaption>\n<span class="set">%s</span>\n'
            '<span class="desc">%s</span>\n<span class="chk">촬영 체크 · %s</span>\n'
            '<span class="src">%s</span>\n</figcaption></figure>') % (media, cap, desc, chk, src_html)

FACT = '<span class="chip c-fact">사실</span>'
EST = '<span class="chip c-est">추정</span>'
WARN = '<span class="chip c-warn">연예인 화보</span>'
HOLD = '<span class="chip c-hold">이미지 미확보</span>'

BOARD1 = "\n".join([
 fig(IMG["az1"], "애즈펌 — 미용실 시술 예시",
     "앞머리가 앞으로 흐르고 이마는 살짝만 보인다. 컬이 자연스러워 손질 부담이 적다.",
     "정면보다 45° 측면에서 컬 방향이 살아난다",
     "출처 " + a("mame", "마메드네 스타일북") + " " + FACT),
 fig(IMG["azc1"], "애즈펌 — 매체가 제시한 연예인 예시",
     "밝은 모발톤에서도 이마 라인이 자연스럽게 남는다.",
     "염색이 밝으면 조명에서 더 떠 보인다",
     "출처 " + a("ade", "스타일에이드") + " " + WARN),
 fig(IMG["azc2"], "애즈펌 — 매체가 제시한 연예인 예시",
     "어두운 모발에서 볼륨과 컬이 또렷하게 읽힌다.",
     "야외 바람에 컬이 풀리면 인상이 달라진다",
     "출처 " + a("ade", "스타일에이드") + " " + WARN),
 fig(IMG["garma"], "가르마펌 — 미용실 시술 예시",
     "가르마를 열어 이마가 절반쯤 보인다. 애즈펌보다 또렷한 인상.",
     "이마가 넓으면 노출 비율을 줄여달라고 요청",
     "출처 " + a("mame", "마메드네 스타일북") + " " + FACT),
])

BOARD2 = "\n".join([
 fig(IMG["gail"], "가일컷 — 매체가 제시한 연예인 예시",
     "한쪽 헤어라인만 올리고 반대쪽은 내려 부드러움을 남긴다.",
     "M자·넓은 이마면 올리는 쪽이 부각된다",
     "출처 " + a("ade", "스타일에이드") + " " + WARN),
 fig(IMG["poma"], "포마드 — 매체가 제시한 연예인 예시",
     "이마를 완전히 드러내 이목구비가 또렷해진다.",
     "광택 과하면 조명에서 기름져 보인다 · 세미매트로 요청",
     "출처 " + a("ade", "스타일에이드") + " " + WARN),
 fig(None, "리젠트 — 사진 없음",
     "옆은 짧게, 앞머리는 위로 세운다. 목이 굵거나 둥근 얼굴형에 볼륨으로 시선을 분산.",
     "윗볼륨이 무너지면 전혀 다른 스타일이 된다",
     "근거 " + a("wheal", "WeddingHeal") + " · " + a("choice", "초이스홀") + " " + HOLD),
 fig(None, "댄디컷 — 사진 없음",
     "펌 없이 레이어와 질감만으로 정리하는 방향. 펌이 부담스러운 신랑의 대안.",
     "드라이 없이도 형태가 남는지 미리 확인",
     "근거 " + a("vsalon", "비주얼살롱 2026 트렌드") + " " + HOLD),
 fig(IMG["shadow1"], "쉐도우펌 — 미용실 시술 예시",
     "전체에 S컬이 들어가 인상이 부드러워진다.",
     "길이가 짧으면 컬이 뭉쳐 보인다",
     "출처 " + a("mame", "마메드네 스타일북") + " " + FACT),
 fig(IMG["shadow2"], "쉐도우펌 — 강한 컬 예시",
     "컬을 세게 넣으면 인상이 크게 바뀐다. 웨딩에선 과할 수 있다.",
     "뽀글해지지 않도록 컬 강도를 낮춰 요청",
     "출처 " + a("mame", "마메드네 스타일북") + " " + FACT),
])

bsrc = '출처 <a href="%s" target="_blank" rel="noopener">다이렉트웨딩 봉스튜디오 포트폴리오</a> %s' % (BONGSRC, FACT)
BONG = "\n".join([
 fig(IMG["bong1"], "봉스튜디오 야외 컷 — 애즈펌 계열",
     "이마를 덮는 내추럴한 앞머리. 야외광에서 컬이 부드럽게 풀린다.",
     "같은 스타일도 야외 바람에서 형태가 달라진다", bsrc),
 fig(IMG["bong2"], "봉스튜디오 클로즈업 컷 — 애즈펌 계열",
     "클로즈업에서도 이마를 거의 덮는 동일 계열 스타일.",
     "클로즈업은 헤어라인·눈썹이 그대로 드러난다", bsrc),
])

HTML = """<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<title>웨딩촬영 신랑 헤어스타일 순위 보고서</title>
<style>%(css)s%(extra)s</style></head><body>
<header><div class="wrap">
<h1>웨딩촬영 신랑 헤어스타일 인기 순위</h1>
<p class="sub">조사일 2026-09-21 · 공개 자료 10개 출처 기반 · <span class="chip c-fact">사실</span> 출처가 직접 말한 것 &nbsp;<span class="chip c-est">추정</span> 종합해 해석한 것 &nbsp;<span class="chip c-warn">연예인 화보</span> 형태 예시일 뿐 실제 신랑 시술 아님</p>
</div></header>
<div class="wrap">

<h2 id="s1"><span class="no">1</span>요약</h2>
<p class="lede">웨딩 매체·헤어 매거진·남성 헤어 컨설팅 등 서로 다른 10개 공개 출처가 신랑 헤어로 추천한 스타일을 모아, <strong>몇 개의 출처가 그 스타일을 꼽았는지</strong>로 순위를 매겼다.</p>
<div class="grid2">
<div class="card"><p class="k">조사일</p><p class="v">2026-09-21</p><p class="n">하루 조사</p></div>
<div class="card"><p class="k">서로 다른 출처</p><p class="v">10곳</p><p class="n">전부 본문 직접 확인</p></div>
<div class="card"><p class="k">순위에 오른 스타일</p><p class="v">8종</p><p class="n">별칭은 대표 이름으로 통합</p></div>
<div class="card"><p class="k">실린 사진</p><p class="v">10장</p><p class="n">전부 실제 열림 확인</p></div>
</div>

<h3>핵심 결론</h3>
<ul>
<li><strong>출처 수로는 애즈펌이 1위</strong>다. 10곳 중 7곳이 신랑 헤어로 꼽았고, 웨딩 매체의 트렌드 TOP3에서도 1번으로 나온다. %(fact)s</li>
<li><strong>촬영 현장에서 실제로 가장 많이 시술되는 것은 가일컷</strong>일 가능성이 높다. 남성 헤어 컨설팅 업체는 "웨딩촬영 헤어·메이크업 샵을 가면 10명 중 8명은 가일컷을 합니다"라고 적었다. %(ohman)s %(fact)s</li>
<li>애즈펌과 가르마펌은 <strong>사실상 한 가족</strong>이다. 차이는 이마 노출 정도뿐이며, 헤어 매거진조차 "애즈펌을 하러가도 가르마 머리가 나오는 경우가 있어요"라고 쓴다. %(mame)s %(fact)s</li>
<li>포마드·리젠트는 <strong>본식 쪽에서 더 많이 추천</strong>되고, 촬영에서는 애즈·가일 계열이 우세하다. %(est)s</li>
</ul>

<div class="note w">
<p><strong>이 순위가 말하지 않는 것</strong></p>
<p>공개 자료로는 실제 예약·시술 건수를 알 수 없다. 여기 순위는 <strong>"몇 개의 출처가 추천했는가"</strong>이지 <strong>"몇 명이 실제로 했는가"</strong>가 아니다. 두 값은 어긋날 수 있고, 실제로 어긋난다 — 출처 수 1위는 애즈펌이지만, 촬영 현장을 직접 관찰해 적은 유일한 출처는 가일컷이 8할이라고 말한다.</p>
<p>표본도 10곳뿐이라 한 곳이 늘고 줄면 4위와 6위는 쉽게 자리가 바뀐다. <strong>1~3위와 그 아래의 간격</strong>만 유의미하게 보는 편이 안전하다.</p>
</div>

<h2 id="s2"><span class="no">2</span>인기 순위표</h2>
<p class="lede">막대와 숫자는 그 스타일을 신랑 헤어로 꼽은 <strong>서로 다른 출처의 수</strong>(최대 10).</p>
<div class="note">
<p><strong>집계 규칙</strong> — §10의 10개 출처를 하나씩 열어, <strong>그 글이 신랑·웨딩 헤어로 그 스타일을 이름을 들어 언급했으면 1</strong>로 셌다. 본문이든 얼굴형 표든 위치는 가리지 않았고, 같은 글에서 여러 번 나와도 1로만 셌다. 별칭(가일펌=가일컷, 애즈=에즈, 올백=포마드 등)은 대표 이름으로 합쳤다. 직접 세어 확인할 수 있도록 출처 링크를 §10에 전부 실었다.</p>
</div>
<div class="tw"><table>
<thead><tr><th>순위</th><th>스타일</th><th>출처 수</th><th>주 무대</th><th>한 줄 설명</th></tr></thead>
<tbody>
%(table)s
</tbody></table></div>
<p class="lede">※ 1위 애즈펌과 2위 가르마펌은 계열이 겹친다. 둘을 한 가족으로 묶으면 10곳 중 9곳이 이 계열을 추천한 셈이 된다. %(est)s</p>

<h2 id="s3"><span class="no">3</span>사진 보드 — 상위권</h2>
<p class="lede">사진마다 원본 링크를 함께 싣고, <strong>연예인 화보인지 미용실 시술 사례인지</strong> 구분해 표기했다.</p>
<div class="board">
%(board1)s
</div>

<h2 id="s4"><span class="no">4</span>사진 보드 — 중·하위권</h2>
<div class="board">
%(board2)s
</div>

<h2 id="s5"><span class="no">5</span>실제 웨딩 촬영 컷에서는 어떻게 보이는가</h2>
<p class="lede">앞선 사진들은 미용실 시술컷이거나 연예인 화보다. 실제 웨딩 촬영에서 같은 계열이 어떻게 찍히는지 보려고, 앞서 검증했던 봉스튜디오 공개 포트폴리오에서 신랑이 또렷하게 나온 컷을 가져왔다.</p>
<div class="board">
%(bong)s
</div>
<div class="note">
<p><strong>봉스튜디오 공개 샘플 95컷 가운데 30컷을 고르게 뽑아 직접 확인한 결과</strong> — 30컷 모두 신랑 헤어가 <strong>애즈펌 계열 한 종류</strong>였다. 이마를 살짝 덮는 내추럴한 앞머리가 야외·실내·캐주얼 세트를 가리지 않고 반복된다. %(fact)s</p>
<p>다만 확인한 30컷은 <strong>거의 같은 남성 모델의 샘플 촬영</strong>이었다. 실제 신랑이 아니라 모델 한 명의 스타일링이 반복된 것이므로, 이 자료는 <strong>스튜디오의 샘플 스타일링 방향</strong>은 말해주지만 <strong>신랑들이 실제로 무엇을 많이 고르는지는 말해주지 않는다</strong>. 그래서 인기 순위의 근거로는 쓰지 않았다. <span class="chip c-warn">주의</span></p>
</div>

<h2 id="s6"><span class="no">6</span>조건별 선택 가이드</h2>
<p class="lede">얼굴형·이마·모량별 추천은 출처마다 조금씩 다르다. <strong>둘 이상의 출처가 겹치게 말한 것</strong>만 옮겼다.</p>
<div class="tw"><table>
<thead><tr><th>이런 경우</th><th>추천</th><th>피하거나 조심</th><th>이유</th></tr></thead>
<tbody>
<tr><td>이마가 넓다</td><td>애즈펌, 시스루 앞머리</td><td>포마드, 가일컷</td><td>가일컷은 한쪽 헤어라인을 통째로 올려 넓은 이마가 부각된다</td></tr>
<tr><td>M자 헤어라인</td><td>애즈펌, 앞머리 내린 펌</td><td>가일컷, 올백</td><td>올리는 쪽 라인이 그대로 드러난다</td></tr>
<tr><td>얼굴이 둥글다</td><td>포마드, 가일컷, 리젠트</td><td>옆볼륨 큰 펌</td><td>윗볼륨을 살려 세로로 길어 보이게</td></tr>
<tr><td>얼굴이 길다</td><td>가르마펌, 애즈펌</td><td>5:5 가르마, 강한 리젠트</td><td>옆볼륨을 주고 이마를 살짝 가려 길이를 보완</td></tr>
<tr><td>턱·광대가 각졌다</td><td>쉐도우펌, 내추럴 가르마, 댄디펌</td><td>직선감 강한 가일컷</td><td>웨이브로 윤곽을 부드럽게 흘린다</td></tr>
<tr><td>이마가 좁다</td><td>포마드</td><td>앞머리 완전히 내리기</td><td>올리면 훤칠해 보이는 효과</td></tr>
<tr><td>모량이 적다</td><td>애즈펌·가일펌 + 윗머리 펌</td><td>완전 올백</td><td>펌으로 볼륨을 만들어 풍성해 보이게</td></tr>
<tr><td>안경을 쓴다</td><td>앞머리를 살짝 올린 스타일</td><td>앞머리 완전히 내리기</td><td>안경테가 시선을 뺏어 헤어는 군더더기 없는 편이 낫다</td></tr>
</tbody></table></div>
<p class="lede">근거: %(avodo)s · %(choice)s · %(ohman)s · %(threads)s · %(mame)s</p>

<h2 id="s7"><span class="no">7</span>촬영 전 준비 타이밍</h2>
<div class="tw"><table>
<thead><tr><th>항목</th><th>권장</th><th>출처가 말한 이유</th></tr></thead>
<tbody>
<tr><td>커트 시기 (촬영)</td><td>촬영 2~3주 전</td><td>자른 티가 빠지고 형태가 자리잡는다 · %(wheal)s</td></tr>
<tr><td>커트 시기 (본식)</td><td>본식 3~5일 전</td><td>당일은 너무 짧아지고, 일주일 넘으면 구레나룻 라인이 지저분해진다 · %(avodo)s</td></tr>
<tr><td>다운펌</td><td>커트할 때 함께</td><td>옆머리가 뜨면 얼굴이 커 보인다</td></tr>
<tr><td>염색</td><td>다크 · 초콜릿 브라운</td><td>밝은 노란기는 조명 아래서 싸구려로 보인다</td></tr>
<tr><td>왁스</td><td>세미매트</td><td>광택이 과하면 사진에서 떡져 보인다</td></tr>
<tr><td>눈썹 정리</td><td>필수</td><td>이마를 드러내는 스타일일수록 눈썹이 흐리면 얼굴이 밋밋해진다 · %(ohman)s</td></tr>
<tr><td>신랑 메이크업</td><td>받기를 권장</td><td>신부만 풀메이크업이면 사진에서 톤 차이가 난다</td></tr>
</tbody></table></div>

<h2 id="s8"><span class="no">8</span>헤어샵·스튜디오에 확인할 질문</h2>
<ol class="q">
<li>촬영 당일 <strong>헤어 변형이 몇 회</strong> 포함되는지, 신랑도 해당되는지</li>
<li>가일컷처럼 <strong>커트가 필요한 스타일</strong>을 당일에 할 수 있는지, 미리 잘라 가야 하는지</li>
<li>내 헤어라인·이마에 <strong>가일컷을 권하는지</strong>, 권한다면 이유가 "잘 어울려서"인지 "무난해서"인지</li>
<li>야외 세트에서 <strong>바람에 컬이 풀렸을 때</strong> 현장 수정이 가능한지</li>
<li>펌을 한다면 <strong>촬영 며칠 전</strong>이 컬이 가장 예쁜 시점인지</li>
<li>신랑 <strong>메이크업·눈썹 정리</strong>가 패키지 포함인지, 추가 비용인지</li>
<li>레퍼런스 사진을 보여줬을 때 <strong>내 모발로 재현 가능한지</strong></li>
</ol>

<h2 id="s9"><span class="no">9</span>추천 3안</h2>
<div class="sl">
<h3>안 A — 실패 확률이 가장 낮은 선택</h3>
<p class="meta">애즈펌 · 출처 수 1위 · 촬영·본식 공통</p>
<p>평소 모습에서 크게 벗어나지 않으면서 볼륨과 정돈감만 더한다. 이마 노출이 부담스럽거나 헤어라인이 신경 쓰이는 경우에 특히 안전하다.</p>
<p class="ref">봉스튜디오 공개 샘플에서 확인한 30컷의 신랑 헤어가 전부 이 계열이었다 — 스튜디오 세트와 톤이 이미 이 스타일에 맞춰져 있다는 뜻으로 읽을 수 있다. %(est)s</p>
</div>
<div class="sl">
<h3>안 B — 또렷하게 나오고 싶다면</h3>
<p class="meta">가일컷 · 촬영 현장 최다 · 정장·실내 세트와 궁합</p>
<p>이마를 절반만 열어 이목구비를 살리면서 포마드만큼 부담스럽지 않다. 다만 넓은 이마·M자 헤어라인·흐린 눈썹이면 단점이 그대로 드러나니 눈썹 정리를 먼저 하는 편이 좋다.</p>
<p class="ref">"신랑에게 제일 잘 어울려서가 아니라 그냥 무난하기 때문에 추천한다"는 지적이 함께 있다. 촬영 사진 10장 중 8장이 이 머리라는 말은 곧 <strong>개성은 약하다</strong>는 뜻이기도 하다. · %(ohman)s</p>
</div>
<div class="sl">
<h3>안 C — 무드를 확실히 나누고 싶다면</h3>
<p class="meta">애즈펌 + 포마드 · 세트별로 바꾸기</p>
<p>야외·캐주얼 세트는 애즈펌으로 부드럽게, 클래식·엔틱 세트나 턱시도 컷은 포마드로 넘겨 대비를 준다. 한 번의 촬영에서 두 가지 인상을 남길 수 있다.</p>
<p class="ref">헤어 변형이 신랑에게도 적용되는지 먼저 확인해야 한다 (§8 1번 질문).</p>
</div>

<h2 id="s10"><span class="no">10</span>출처 목록</h2>
<div class="tw"><table>
<thead><tr><th>#</th><th>출처</th><th>유형</th><th>다룬 범위</th><th>이 보고서에서 쓴 것</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td>%(s_ade)s</td><td>웨딩·스타일 매체</td><td>촬영·본식</td><td>트렌드 TOP3, 연예인 예시 사진 4장</td></tr>
<tr><td class="num">2</td><td>%(s_ohman)s</td><td>남성 헤어 컨설팅</td><td>촬영 특화</td><td>가일컷 8/10 현장 관찰, 장단점·피해야 할 유형</td></tr>
<tr><td class="num">3</td><td>%(s_avodo)s</td><td>결혼 준비 블로그</td><td>본식</td><td>가장 많이 하는 3가지, 얼굴형표, 커트 타이밍</td></tr>
<tr><td class="num">4</td><td>%(s_mame)s</td><td>헤어 매거진</td><td>일반</td><td>스타일 판별 기준, 시술 예시 사진 4장</td></tr>
<tr><td class="num">5</td><td>%(s_choice)s</td><td>웨딩 정보</td><td>촬영·본식</td><td>포마드·가일펌·가르마/애즈·리젠트</td></tr>
<tr><td class="num">6</td><td>%(s_wheal)s</td><td>웨딩 정보</td><td>촬영·본식</td><td>포마드·사이드파트·애즈펌·리젠트, 커트 2~3주 전</td></tr>
<tr><td class="num">7</td><td>%(s_vsalon)s</td><td>미용실 콘텐츠</td><td>일반·트렌드</td><td>댄디컷·리젠트+가일·가르마 레이어컷</td></tr>
<tr><td class="num">8</td><td>%(s_visio)s</td><td>헤어 정보</td><td>일반</td><td>가르마·애즈·쉐도우·댄디 분류</td></tr>
<tr><td class="num">9</td><td>%(s_threads)s</td><td>SNS 정리글</td><td>일반</td><td>얼굴형 5종별 매칭</td></tr>
<tr><td class="num">10</td><td>%(s_micol)s</td><td>웨딩 블로그</td><td>촬영·본식</td><td>사이드파트·투블럭·내추럴펌</td></tr>
</tbody></table></div>

<div class="note">
<p><strong>수집 한계</strong></p>
<p>① 아이웨딩 기사 등 일부 웨딩 매체 페이지는 본문이 JavaScript로만 렌더링돼 확인하지 못했다 — 순위 집계에서 제외했다.<br>
② 네이버 블로그는 크롤러 차단이라 실제 신랑 후기를 표본에 넣지 못했다. 이 순위는 <strong>추천 글 기준</strong>이지 <strong>후기 기준</strong>이 아니다.<br>
③ 리젠트·댄디컷은 본문 근거는 있으나 실제로 열리는 예시 사진을 확보하지 못해 사진 없이 실었다.<br>
④ 연예인 화보 사진은 스타일의 형태를 보여주기 위한 예시이며 실제 신랑의 시술 결과가 아니다.</p>
</div>

<div class="note w">
<p><strong>hook.md 적용 여부</strong> — hook.md의 검증 규칙은 "하남 봉스튜디오에서 촬영된 사진인지"를 가리는 규칙이다. 이 보고서의 헤어 예시 사진은 봉스튜디오 촬영분이라고 주장하지 않으므로 적용 대상이 아니다. 다만 §5에 실은 2컷은 봉스튜디오 포트폴리오 컷이며, 앞선 검증에서 PASS 판정을 받은 항목이다.</p>
</div>

<footer>
<p>조사·작성 2026-09-21 · 서로 다른 10개 공개 출처의 본문을 직접 열어 확인했고, 실린 사진 10장은 전부 referer 없이 실제로 열리는 것을 확인했다.</p>
<p>순위는 추천 출처 수 기준이며 실제 예약·시술 건수가 아니다. 사진의 저작권은 각 원본 출처에 있다.</p>
</footer>
</div></body></html>""" % {
 "css": CSS, "extra": EXTRA, "table": TABLE,
 "board1": BOARD1, "board2": BOARD2, "bong": BONG,
 "fact": FACT, "est": EST,
 "ohman": a("ohman", "오맨뷰티"), "mame": a("mame", "마메드네"),
 "avodo": a("avodo", "아보의 결혼생활"), "choice": a("choice", "초이스홀"),
 "threads": a("threads", "얼굴형별 정리"), "wheal": a("wheal", "WeddingHeal"),
 "s_ade": a("ade", "스타일에이드 — 신랑 웨딩헤어 트렌드 TOP3"),
 "s_ohman": a("ohman", "오맨뷰티 — 남자웨딩촬영헤어"),
 "s_avodo": a("avodo", "아보의 결혼생활 — 신랑 본식 헤어스타일"),
 "s_mame": a("mame", "마메드네 — 애즈펌·가르마펌·쉐도우펌 차이"),
 "s_choice": a("choice", "초이스홀 — 얼굴형별 예비신랑 헤어 4가지"),
 "s_wheal": a("wheal", "WeddingHeal — 남자 웨딩 헤어스타일"),
 "s_vsalon": a("vsalon", "비주얼살롱 — 2026 남자 헤어컷 트렌드"),
 "s_visio": a("visio", "Visio — 남자 펌 종류 비교"),
 "s_threads": a("threads", "얼굴형별 어울리는 헤어스타일 정리"),
 "s_micol": a("micol", "최다영 — 신랑 웨딩 헤어 얼굴형별 가이드"),
}

out = os.path.join(PROJ, "report/groom_hairstyle_report.html")
open(out, "w", encoding="utf-8").write(HTML)
print("written:", out)
print("bytes:", len(HTML.encode("utf-8")))
