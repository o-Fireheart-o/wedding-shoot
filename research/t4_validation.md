# [t4] t2·t3 수집물 hook 규칙 재검증 로그

- **검증일**: 2026-09-20
- **입력**: `research/t2_bongstudio.md` (봉스튜디오), `research/t3_casual.md` (타 스튜디오 캐주얼)
- **기준**: `hook.md` 전문 / `agent.md` 최종 산출물 형식·품질 기준
- **입력 파일은 읽기 전용으로만 다뤘다.** 수정하지 않았다.

## 0. 게이트 결론

| 구조적 오류 항목 | 결과 |
| --- | --- |
| t3 항목이 봉스튜디오 사례 집계·순위표에 혼입 | **없음** — t2 전문에서 `C01~C18` 사례ID 0건, t3 스튜디오명 15종 전부 0건 매칭 |
| PASS 항목에 하남 식별 근거 누락 | **없음** — PASS 107행 전부 근거·링크 동시 기재 |
| 링크 다수 파손 | **없음** — 스킴 정정 후 유효 링크 107/107. 공식 갤러리 13행만 `https` 표기로는 406이고 `http`로는 200 → **표기 정정 후 전부 열림** |
| t3에 봉스튜디오 사례 혼입 | **없음** — t3 표 18행 중 봉스튜디오 촬영 0건 |

→ **구조적 오류 없음. HTML 보고서 작성 게이트 통과.** `report/wedding_concept_report.html` 생성함.

## 1. 최종 판정 건수

| 판정 | 건수 | 내용 |
| --- | --- | --- |
| **PASS** | **107** | 제휴 포트폴리오 컷 94행 + 공식 갤러리 시리즈 13행 (이 중 13행은 링크 표기 정정 조건부) |
| **HOLD** | **7** | 공식 인스타 1 + 웨딩크라우드 후기 6 — 순위 집계 제외 |
| **EXCLUDE** | **10** | 범위 외 공식 갤러리 4(제주 3·가족 1) + 유사·동명 상호 6 — 순위 집계 제외 |

t3는 hook.md 하남 식별자 규칙 적용 대상이 아니므로 위 건수에 포함하지 않는다. t3 18건은 §3의 4가지 기준으로 별도 검증했고 **18건 전부 통과**다.

## 2. t2 (봉스튜디오) 항목별 판정표 — hook.md 3규칙

규칙 ① 하남 식별자 최소 1개 확인 / ② 동명 해외 `Bong Studio`·국내 유사 상호 배제 / ③ 원본 링크와 하남 식별 근거 동시 기록.

### 2.1 링크 재확인 방법

- **개방 여부**: 129개 고유 URL 전부에 HEAD→GET 실제 요청. 브라우저 User-Agent·Accept 헤더 사용.
- **동일성 확인**: 제휴 포트폴리오 이미지 95개를 **다시 내려받아 t2 수집 시점 사본과 MD5 바이트 비교** → **95/95 전부 일치**. 링크가 열리기만 하는 것이 아니라 t2가 분류한 그 사진을 여전히 가리킨다는 뜻이다.
- **정정 1건**: 공식 갤러리 13행의 `https://studiobong.com/galleries/...`는 HTTP 406을 돌려준다. 같은 경로를 `http://`로 요청하면 200 + 본문 정상이다. t2 부록 C가 "HTTPS self-signed 인증서 오류 → HTTP로 우회 접속 성공"을 이미 기록해 두었으므로, 최종 보고서에서는 **`http://` 표기를 사용**한다. 새 링크를 만든 것이 아니라 스킴만 정정했다.

### 2.2 판정표 (118행)

| 사례ID | 원본링크 | 하남 식별 근거 | 출처 유형 | ① | ② | ③ | 링크 개방 | 링크 동일성 | t2 판정 | **t4 최종 판정** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BS-P001 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6086838f90719091c2c_%EA%B0%9C%EC%84%A0%EB%AC%B8%201R1A9948-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P002 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6086ee3926fa22e0212_%EA%B0%A4%EB%9F%AC%EB%A6%AC1R1A2013-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P003 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b60709da12b736bebbc7_%EA%B0%A4%EB%9F%AC%EB%A6%ACL1210186-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P004 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b607d00fe7fbfba27fab_%EA%B3%84%EB%8B%A81R1A5285-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P005 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b607bbab85878b21cf1e_%EA%B3%84%EB%8B%A8JUN_3416-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P006 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b60790d9616048a503b5_%EA%B3%84%EB%8B%A8KWON4746-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P007 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b607473c90eed2f76fd9_%EB%82%AE%EB%B3%B5%EB%8F%841R1A9406%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P008 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b607868e92e4b3d6e9f1_%EB%82%AE%EB%B3%B5%EB%8F%84HO__6246%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P009 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b60714903fb4e41625c4_%EB%91%90%EA%B1%B41R1A4647-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P010 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6087007257f1a50f526_%EB%91%90%EA%B1%B4JUN_7517-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P011 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b607d82c5bda7f740787_%EB%98%A5%EA%B0%95%EC%95%84%EC%A7%801R1A4735-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P012 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b60790d9616048a503a6_%EB%AC%B8%EC%95%9E1R1A7136-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P013 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6074cb6ed54014bbf24_%EB%AF%B8%EB%8B%88%EA%B2%B0%ED%98%BC1R1A5860-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P014 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6071520f307ea93f6ce_%EB%AF%B8%EB%8B%88%EA%B2%B0%ED%98%BC1R1A5966-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P015 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6076838f90719091c1a_%EB%AF%B8%EB%8B%88%EA%B2%B0%ED%98%BCJUN_2180-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P016 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6071520f307ea93f6d5_%EB%AF%B8%EB%8B%88%EA%B2%B0%ED%98%BCL1190370-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P017 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b60793b224e5d85e666b_%EB%B0%98%EB%B0%981R1A8218-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P018 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b607473c90eed2f76fd2_%EB%B2%A0%EC%9D%BC1R1A3345-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P019 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6072a3722b8a204e07e_%EB%B2%A0%EC%9D%BC1R1A3569-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P020 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6087007257f1a50f529_%EB%B2%A0%EC%9D%BCJUN_6620-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P021 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b607007bd4aca99b9efa_%EB%B2%A4%EC%B9%98JUN_1991-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P022 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b60e868e92e4b3d6ee1d_%EB%B2%A4%EC%B9%98L1190222-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P023 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b615868e92e4b3d6f426_%EB%B3%B5%EB%8F%841R1A8998-1-2%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P024 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b61570408da64b82c4b9_%EB%B3%B5%EB%8F%841R1A9315-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P025 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6151520f307ea93fc77_%EB%B3%B5%EB%8F%846099-1-2%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P026 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b61514903fb4e4162a37_%EB%B8%94%EB%9E%99L1200631-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P027 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6156838f90719092342_%EB%B8%94%EB%9E%99L1200697-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P028 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b61514903fb4e4162a24_%EB%B8%94%EB%9E%99L1200824-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P029 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b61570408da64b82c4d7_%EC%84%B1%EB%B2%BD1R1A9017-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P030 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6156838f9071909235a_%EC%84%B1%EB%B2%BDL1200316-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P031 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6177007257f1a5100a7_%EC%84%B1%EB%B2%BDL1200335-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P032 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b61570408da64b82c511_%EC%84%BC%ED%84%B0%ED%94%BC%EC%8A%A41R1A6299-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P033 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6252a3722b8a204e939_%EC%84%BC%ED%84%B0%ED%94%BC%EC%8A%A4L1190522-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P034 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b625abe712ac1a43e196_%EC%95%BC%EA%B0%841R1A0277-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P035 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6259f86442f7afd383d_%EC%95%BC%EA%B0%841R1A0366-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P036 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6255a5c728297586ae6_%EC%95%BC%EA%B0%841R1A0447-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P037 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b625a3a7e5367c08b744_%EC%95%BC%EA%B0%84GYU_8385-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P038 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6255a5c728297586ac0_%EC%95%BC%EA%B0%84%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P039 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6255a5c728297586ae3_%EC%9A%B4%EB%8F%99%EC%9E%A51R1A4429-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P040 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6257007257f1a510c5d_%EC%9A%B4%EB%8F%99%EC%9E%A51R1A5208-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P041 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b625868e92e4b3d6fb56_%EC%9A%B4%EB%8F%99%EC%9E%A5JUN_7854-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P042 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b62ed82c5bda7f741874_%EC%9A%B4%EB%8F%99%EC%9E%A5JUN_7877-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P043 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b62d5a5c728297586bb9_%EC%9A%B4%EB%8F%99%EC%9E%A5JUN_7897-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P044 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63521ea4b48b99f7f51_%EC%9A%B4%EB%8F%99%EC%9E%A5L1220252-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P045 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6257c61caa07329c6f7_%EC%9A%B4%EB%8F%99%EC%9E%A5006090210022-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P046 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6355a5c728297586c6b_%EC%9C%A1%EA%B0%81%EC%B0%BD1R1A4066-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P047 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6359f86442f7afd3cc3_%EC%9C%A1%EA%B0%81%EC%B0%BDHO__2995-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P048 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b635abe712ac1a43e49e_%EC%9C%A1%EA%B0%81%EC%B0%BDKWON1183-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P049 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b635a3a7e5367c08bc39_%EC%9E%91%EC%9D%80%EC%B0%BD1R1A3716-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P050 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6352a3722b8a204ed23_%EC%9E%91%EC%9D%80%EC%B0%BDHO__2840-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P051 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63514903fb4e4163feb_%EC%9E%91%EC%9D%80%EC%B0%BDKWON0859-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P052 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63f7007257f1a51236c_%EC%9E%91%EC%9D%80%EC%B0%BDL1180783-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P053 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63f2a3722b8a204ee19_%EC%A0%95%EC%9B%901R1A1726-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P054 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63f14903fb4e41640bc_%EC%A0%95%EC%9B%901R1A2135-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P055 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63fe1d2fef33a0b3d7e_%EC%A0%95%EC%9B%901R1A3051-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P056 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63ea3a7e5367c08bd96_%EC%A0%95%EC%9B%90KWON9295-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P057 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63e5a5c728297586f13_%EC%A0%95%EC%9B%90006090210016-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P058 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63e7007257f1a5122ff_%EC%A3%BC%EA%B0%84%ED%8C%8C%ED%8B%B01R1A8249-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P059 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63fa3a7e5367c08bdb1_%EC%A3%BC%EA%B0%84%ED%8C%8C%ED%8B%B01R1A8338-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P060 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63f67f6bc60a3ef4687_%EC%A3%BC%EA%B0%84%ED%8C%8C%ED%8B%B0HO__7622-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P061 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63e14903fb4e41640ab_%EC%A3%BC%EA%B0%84%ED%8C%8C%ED%8B%B0JUN_3815-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P062 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63f1520f307ea9401bf_%EC%A3%BC%EA%B0%84%ED%8C%8C%ED%8B%B0JUN_3970-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P063 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b63e93b224e5d85e70a1_%EC%A3%BC%EA%B0%84%ED%8C%8C%ED%8B%B0KWON2310-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P064 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b647a3a7e5367c08c133_%ED%81%B4%EC%97%85HO__6623-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P065 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b64b14903fb4e4164830_%ED%81%B4%EC%97%85L1190665-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P066 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b64d93b224e5d85e82b6_%ED%86%B5%EC%B0%BD1R1A2600-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P067 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b653bbab85878b21e3c9_%ED%86%B5%EC%B0%BD1R1A2673-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P068 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6525a5c728297587193_%ED%86%B5%EC%B0%BD1R1A2788-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P069 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b652a3a7e5367c08c7e0_%ED%86%B5%EC%B0%BD21R1A3353-22%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P070 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6525a5c7282975871a7_%ED%86%B5%EC%B0%BD2HO__2654-22%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P071 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b652bbab85878b21e3b7_%ED%86%B5%EC%B0%BD2L1180713-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P072 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6521520f307ea940f26_%ED%8F%AC%EC%8A%A4%ED%84%B0GYU_1754-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P073 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b6525997a71e311be095_%ED%8F%AC%EC%8A%A4%ED%84%B0HO__1335-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P074 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7b1d9ad1d9e304d76fa_%ED%8F%AC%EC%8A%A4%ED%84%B0L1220150-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P075 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7b97c61caa0732a8778_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%84%B01R1A1118-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P076 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c1868e92e4b3d754f5_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%84%B0GYU_0294-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P077 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c121ea4b48b99f926f_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%84%B0GYU_0303-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P078 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c17c61caa0732a898a_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%84%B0GYU_0337-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P079 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c1bbab85878b22664e_%ED%95%98%ED%8A%B8GYU_1344-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P080 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c1d00fe7fbfba2beb2_%ED%95%98%ED%8A%B8GYU_1426-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P081 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c114903fb4e4166a8e_%ED%95%98%ED%8A%B8HO__1070-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P082 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c1b2e7bf8ee2457224_%ED%95%9C%ED%99%941R1A2211-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P083 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c07c61caa0732a894f_%ED%95%9C%ED%99%941R1A2211-2%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P084 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c1d9ad1d9e304d771f_%ED%95%9C%ED%99%941R1A2234-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P085 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c7d9ad1d9e304d775b_%ED%95%9C%ED%99%94L1210373-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P086 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c7b767d015c70dc94a_%ED%95%A9%ED%8C%90%EB%B2%BD1R1A8412-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P087 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c7d9ad1d9e304d776d_%ED%95%A9%ED%8C%90%EB%B2%BDJUN_4144-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P088 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c75997a71e311bfb33_%ED%95%A9%ED%8C%90%EB%B2%BDKWON3454-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P089 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c77007257f1a51ee38_%ED%99%94%EC%9D%B4%ED%8A%B81R1A6070-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P090 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c790d9616048a57f1d_%ED%99%94%EC%9D%B4%ED%8A%B8GYU_7018-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P091 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c7868e92e4b3d756ed_%ED%99%94%EC%9D%B4%ED%8A%B8HO__4264-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P092 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c7dff982c791813b00_%ED%99%94%EC%9D%B4%ED%8A%B8HO__4339-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P093 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c7d00fe7fbfba2bf33_%ED%99%94%EC%9D%B4%ED%8A%B8KWON1625-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-P094 | [열기](https://cdn.prod.website-files.com/66a1eeaa00f1c86c3dbae974/6a44b7c71520f307ea9447a9_%ED%99%94%EC%9D%B4%ED%8A%B8KWON1993-1%5B%EA%BE%B8%EB%AF%B8%EA%B8%B0%5D.avif) | 하남 미사리 세트장 명시(제휴 포트폴리오) + TEL 02-3447-6049·사무실 동일 → wedding21 기사의 `하남시 미사동 203-7`과 동일 업체 | 제휴 | ✔ | ✔ | ✔ | 열림 | 동일(바이트 일치) | PASS | **PASS** |
| BS-G01 | [열기](http://studiobong.com/galleries/2024-comely/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G02 | [열기](http://studiobong.com/galleries/2023-winsome/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G03 | [열기](http://studiobong.com/galleries/2021heshe/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G04 | [열기](http://studiobong.com/galleries/2020-youarelove/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G05 | [열기](http://studiobong.com/galleries/2019-iamlove/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G06 | [열기](http://studiobong.com/galleries/2018loverose/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G07 | [열기](http://studiobong.com/galleries/ylang/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G08 | [열기](http://studiobong.com/galleries/love-blossom/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G09 | [열기](http://studiobong.com/galleries/nature-blooming/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G10 | [열기](http://studiobong.com/galleries/cantabile/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G11 | [열기](http://studiobong.com/galleries/cantata/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G12 | [열기](http://studiobong.com/galleries/la-flora/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-G13 | [열기](http://studiobong.com/galleries/beyond-day/) | 공식 홈 푸터 `경기도 하남시 미사동로40번길 124-27` (하남 촬영장 명시 공식 페이지) | 공식 | ✔ | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | PASS | **PASS(링크 표기 정정)** |
| BS-X01 | [열기](http://studiobong.com/galleries/2015jeju/) | 없음 — 공식 갤러리이나 촬영지가 제주 / 웨딩 아님 | 공식 | ✖ 하남 미사리 세트 아님(제주/가족) | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | EXCLUDE | **EXCLUDE** |
| BS-X02 | [열기](http://studiobong.com/galleries/hello-jeju-vol1/) | 없음 — 공식 갤러리이나 촬영지가 제주 / 웨딩 아님 | 공식 | ✖ 하남 미사리 세트 아님(제주/가족) | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | EXCLUDE | **EXCLUDE** |
| BS-X03 | [열기](http://studiobong.com/galleries/hello-jeju-vol2/) | 없음 — 공식 갤러리이나 촬영지가 제주 / 웨딩 아님 | 공식 | ✖ 하남 미사리 세트 아님(제주/가족) | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | EXCLUDE | **EXCLUDE** |
| BS-X04 | [열기](http://studiobong.com/galleries/family/) | 없음 — 공식 갤러리이나 촬영지가 제주 / 웨딩 아님 | 공식 | ✖ 하남 미사리 세트 아님(제주/가족) | ✔ | ✔ | 열림(http로 정정) | 해당 없음(페이지) | EXCLUDE | **EXCLUDE** |
| BS-H01 | [열기](https://www.instagram.com/bongstudio_/) | 간접 근거만 — 원문(게시물·후기 본문) 확인 불가 | 공식 | △ 간접(기사·업체 페이지 표기) | ✔ | ✖ 원문 미확인 | 열림 | 해당 없음(페이지) | HOLD | **HOLD** |
| BS-H02 | [열기](https://weddingcrowd.kr/store/view.php?idx=281) | 간접 근거만 — 원문(게시물·후기 본문) 확인 불가 | 실제 후기 | △ 간접(기사·업체 페이지 표기) | ✔ | ✖ 원문 미확인 | 열림 | 해당 없음(페이지) | HOLD | **HOLD** |
| BS-H03 | [열기](https://weddingcrowd.kr/store/view.php?idx=281) | 간접 근거만 — 원문(게시물·후기 본문) 확인 불가 | 실제 후기 | △ 간접(기사·업체 페이지 표기) | ✔ | ✖ 원문 미확인 | 열림 | 해당 없음(페이지) | HOLD | **HOLD** |
| BS-H04 | [열기](https://weddingcrowd.kr/store/view.php?idx=281) | 간접 근거만 — 원문(게시물·후기 본문) 확인 불가 | 실제 후기 | △ 간접(기사·업체 페이지 표기) | ✔ | ✖ 원문 미확인 | 열림 | 해당 없음(페이지) | HOLD | **HOLD** |
| BS-H05 | [열기](https://weddingcrowd.kr/store/view.php?idx=281) | 간접 근거만 — 원문(게시물·후기 본문) 확인 불가 | 실제 후기 | △ 간접(기사·업체 페이지 표기) | ✔ | ✖ 원문 미확인 | 열림 | 해당 없음(페이지) | HOLD | **HOLD** |
| BS-H06 | [열기](https://weddingcrowd.kr/store/view.php?idx=281) | 간접 근거만 — 원문(게시물·후기 본문) 확인 불가 | 실제 후기 | △ 간접(기사·업체 페이지 표기) | ✔ | ✖ 원문 미확인 | 열림 | 해당 없음(페이지) | HOLD | **HOLD** |
| BS-H07 | [열기](https://weddingcrowd.kr/store/view.php?idx=281) | 간접 근거만 — 원문(게시물·후기 본문) 확인 불가 | 실제 후기 | △ 간접(기사·업체 페이지 표기) | ✔ | ✖ 원문 미확인 | 열림 | 해당 없음(페이지) | HOLD | **HOLD** |

### 2.3 규칙 ② 동명·유사 상호 배제 재확인 (EXCLUDE 6건)

> 하남 봉스튜디오 식별 근거가 확인되지 않았습니다. 동명·유사 상호 혼입 방지를 위해 이 사례를 제외합니다.

| 대상 | 링크 | 재확인 결과 | 판정 유지 |
| --- | --- | --- | --- |
| `@bong__st` | <https://www.instagram.com/bong__st/> | HTTP 200이나 로그인 월 — 하남 식별자 확인 불가 | EXCLUDE |
| `@bong_studio` | <https://www.instagram.com/bong_studio/> | 동일 | EXCLUDE |
| `@officialstudiobon` (BON/본) | <https://www.instagram.com/officialstudiobon/> | 상호 자체가 다름 | EXCLUDE |
| `@thebongstudioofficial` (The Bong Studio) | <https://www.instagram.com/thebongstudioofficial/> | 해외 동명 가능성, 하남 식별자 없음 | EXCLUDE |
| Studio BONG: 스튜디오봉 (FB) | <https://www.facebook.com/studiobong/> | HTTP 400 — 본문 확인 불가, 하남 식별자 없음 | EXCLUDE |
| Bong Studio, Gangnam District (FB) | <https://www.facebook.com/bongstudiobong/> | HTTP 400 — 동일 | EXCLUDE |

공식 계정은 `@bongstudio_` 단일이며(wedding21·아이웨딩·다이렉트결혼준비 3개 출처 일치), 위 6건은 모두 이와 다르다. **최종 후보에 유사 상호 항목은 한 건도 포함되지 않았다.**

### 2.4 최종 후보에서 뺀 항목

| 항목 | 사유 |
| --- | --- |
| BS-X01·X02·X03 (2015 The Jeju, Hello Jeju Vol1·Vol2) | 봉스튜디오 공식 갤러리이나 촬영지가 제주 — 하남 미사리 세트가 아님 |
| BS-X04 (Family) | 가족사진 갤러리로 웨딩 촬영이 아님 |
| BS-H01 (`@bongstudio_`) | 로그인 월로 게시물·캡션 원문 확인 불가 → HOLD |
| BS-H02~H07 (웨딩크라우드 후기 6건) | 개별 후기 URL이 JS 렌더링으로만 노출되어 본문·사진 확인 불가 → HOLD |
| BS-G04~G13 (2020 이전 공식 시리즈 10건) | 링크는 열리지만 개별 컷을 열람하지 않아 카테고리 미확인 → 사진 보드에서는 제외하고 §3 각주로만 안내 |

## 3. t3 (타 스튜디오 캐주얼) 항목별 4가지 검증

**적용하지 않은 규칙**: hook.md의 하남 식별자 규칙은 봉스튜디오 전용이다. t3 항목에 하남 식별 근거가 없는 것은 정상이며, 이를 이유로 EXCLUDE 하지 않았다.

검증 기준

1. **T1** — 봉스튜디오가 아닌 스튜디오·장소가 분명히 표시되었는가
2. **T2** — 봉스튜디오 재현 가능 여부가 `확인 필요`로 표기되었는가
3. **T3** — 이 항목이 봉스튜디오 사례 집계·순위표에 섞이지 않았는가
4. **T4** — 패션 화보·상업 광고·AI 생성 이미지가 아닌가

| 사례ID | 스튜디오·장소 | 원본링크 | 출처 유형 | T1 | T2 | T3 | T4 | 판정 | 품질 주의 (agent.md 품질 기준) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | 스튜디오 크리미 (서울 송파, 시간당 3만원 대여 스튜디오에서 커플이 직접 셀프 촬영) | [열기](https://brunch.co.kr/@junha04/149) | 실제후기 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C02 | 동해 밤바다 (촬영 작가·업체명 원문 미공개) | [열기](https://brunch.co.kr/@honeysoul/22) | 실제후기(촬영 준비 글) | ✔ | ✔ | ✔ | ✔ | **PASS** | 촬영 결과물이 아닌 **촬영 계획 단계** 서술 (t3 원문이 이미 별도 표기). 무드 참고용으로만 사용. |
| C03 | 차 없는 도로·야외 거리 (구체 스튜디오 없음, 의상은 홍대 빈티지샵) | [열기](https://brunch.co.kr/@threeclover/55) | 실제후기 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C04 | 예천 선몽대 인근 자연공간 · 한옥 숙소 · 집 근처 시골길/기찻길 (동일 커플 2편) | [열기](https://brunch.co.kr/@amymoong/114) | 실제후기 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C05 | 바르셀로나(사그라다 파밀리아·고딕지구) · 포르투(상벤투역·동루이스 다리) — 현지 작가 섭외, 업체명 원문 미공개 | [열기](https://brunch.co.kr/@e741835775f7438/210) | 실제후기 | ✔ | ✔ | ✔ | ✔ | **PASS** | 해외(바르셀로나·포르투) 촬영. 장소 재현 대상이 아니라 '같은 옷·같은 포즈, 배경만 교체' 방법론 참고용. |
| C06 | 은평구 한옥 공간 ("웨딩스러운 공간이 아닌, 다같이 우리 집에 놀러 와" 콘셉트) | [열기](https://brunch.co.kr/@inalee/38) | 실제후기 | ✔ | ✔ | ✔ | ✔ | **PASS** | 웨딩 촬영이 아니라 **한옥 스몰웨딩 행사** 서술 비중이 큼. 놀이형 상호작용 아이디어만 참고. |
| C07 | 구호 스튜디오 (서울 성동구) / 촬영지 서울숲 | [열기](https://www.directwedding.co.kr/blog/outdoor-wedding-snapshots) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C08 | 나라코드 작가(필름커넥트 소속) / 촬영지 난지한강공원(상암, 월드컵대교 배경) | [열기](https://blog.filmconnect.co.kr/%ED%95%84%EB%A6%84%EC%BB%A4%EB%84%A5%ED%8A%B8-%EC%84%9C%EC%9A%B8-%ED%95%9C%EA%B0%95%EA%B3%B5%EC%9B%90-%EC%9B%A8%EB%94%A9%EC%8A%A4%EB%83%85-%ED%9B%84%EA%B8%B0-%EC%9E%91%EA%B0%80%EC%B6%94%EC%B2%9C-%EB%82%98%EB%9D%BC%EC%BD%94%EB%93%9C--107802) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C09 | 김태우스냅(스냅퍼 플랫폼, 서울, 경력 13년) | [열기](https://www.snaaaper.com/shootingGallery/1259) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C10 | 정말제대로하자(크몽) / 궁·공원·스튜디오 등 희망 장소, 서울·경기·제주·해외 출장 | [열기](https://kmong.com/gig/239071) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C11 | 마인드무브(크몽, 프리랜서 4년) / 서울·경기·강원 실내외, 실내는 고객이 대여 스튜디오 섭외 | [열기](https://kmong.com/gig/469930) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C12 | 댕귤스튜디오(크몽) / 제주도, 패키지별 3~5개 장소 이동 | [열기](https://kmong.com/gig/420250) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | — |
| C13 | 하라 사진관 / 제주 애월 중산간·송악산 입구·곽지 과물해수욕장 | [열기](https://mywedding.designhouse.co.kr/in_magazine/sub.html?at=view&info_id=75835) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | MYWEDDING 기사 1건에서 나온 5건 중 하나 (독립 출처 아님). |
| C14 | 강릉 원규앤노블레스 스튜디오(이동진) / 강릉 경포호·안목해변·평창 대관령 삼양목장 | [열기](https://mywedding.designhouse.co.kr/in_magazine/sub.html?at=view&info_id=75835) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | MYWEDDING 기사 1건에서 나온 5건 중 하나 (독립 출처 아님). |
| C15 | 오브센트(김성겸) / 해파랑길 37코스(강릉 염전해변)·등명해수욕장·경포비치호텔 레스토랑 | [열기](https://mywedding.designhouse.co.kr/in_magazine/sub.html?at=view&info_id=75835) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | MYWEDDING 기사 1건에서 나온 5건 중 하나 (독립 출처 아님). |
| C16 | 더써드마인드 부산(장현경) / 송정동 철길 옆 작은 숲·송정 바닷가·철길 옆 골목 | [열기](https://mywedding.designhouse.co.kr/in_magazine/sub.html?at=view&info_id=75835) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | MYWEDDING 기사 1건에서 나온 5건 중 하나 (독립 출처 아님). |
| C17 | 세컨플로우(김백천·허수덕) / 부산 보수동 책방 골목·경주 산림환경연구원·경주 대릉원 | [열기](https://mywedding.designhouse.co.kr/in_magazine/sub.html?at=view&info_id=75835) | 제휴 | ✔ | ✔ | ✔ | ✔ | **PASS** | MYWEDDING 기사 1건에서 나온 5건 중 하나 (독립 출처 아님). |
| C18 | 루브르네프(홍혜전) · 로웰 스튜디오 · 오디너리 독스(염호영) — 매거진 1건에서 3개 스튜디오가 함께 언급됨 | [열기](https://www.noblesse.com/home/news/magazine/detail.php?no=10361) | 제휴(매거진) | ✔ | ✔ | ✔ | ✔ | **PASS** | 매거진 1건이 3개 스튜디오를 함께 소개하고, 예시로 **연예인 촬영**을 든다. 개별 예비부부 촬영 사례가 아니므로 무드 방향만 참고. |

### 3.1 4가지 기준 집계

| 기준 | 통과 | 미통과 | 근거 |
| --- | --- | --- | --- |
| T1 스튜디오·장소 명시 | 18 | 0 | 18행 전부 스튜디오명 또는 구체 촬영지 기재. 작가·업체명이 원문에 없는 C02·C03·C05는 촬영 장소(동해 밤바다 / 차 없는 도로 / 바르셀로나·포르투)로 특정되고 원문 미공개임을 명시 |
| T2 재현 여부 `확인 필요` | 18 | 0 | 18행 전부 `확인 필요`. t3 서두에도 "모든 행이 예외 없이 확인 필요" 고지 |
| T3 봉스 집계 비혼입 | 18 | 0 | t2 전문 grep — `C01~C18` 0건, t3 스튜디오명 15종 0건. t2 §3 순위표 세트명도 전부 봉스튜디오 세트 |
| T4 화보·광고·AI 아님 | 18 | 0 | 출처가 실제후기(브런치 6) 또는 스튜디오 추천 기사·플랫폼 상품 페이지(12). MYWEDDING 기사는 직접 열람해 **추천 기사이며 유료 광고가 아님**을 확인 |

`품질 주의` 열은 agent.md 품질 기준("사실과 추정을 명확히 구분")에 따른 **읽을 때의 주의사항**이며, 위 4가지 기준의 판정을 바꾸는 값이 아니다.

### 3.2 원문 내용 교차 확인 (표본 열람)

링크가 열리는지만 보지 않고, t3가 표에 적은 내용이 원문에 실제로 있는지 표본으로 확인했다.

| 대상 | 확인한 것 | 원문에서 확인된 내용 | 결과 |
| --- | --- | --- | --- |
| C01<br><https://brunch.co.kr/@junha04/149> | 송파 스튜디오 크리미 대여 셀프 촬영, 시간당 3만원, 2024년 7월, 옷 바꿔 입기 여부 | 제목 '100%셀프 스튜디오 촬영으로 우리 다운 웨딩 스냅찍기'(박천희, 2024-07-07). 본문에 "우리는 집에서 가까운 송파 쪽의 '스튜디오 크리미'라는 곳을 대여했다", "1시간에 3만 원", 옷 바꿔 입은 컷 서술 확인. | **t3 기재와 일치** |
| C06<br><https://brunch.co.kr/@inalee/38> | 은평구 한옥, '다같이 우리 집에 놀러 와' 콘셉트, 어머니 제작 한복, 보물찾기·캔버스, 2024-05-05 6시간 | 제목 '셀프웨딩의 끝판왕, 준비과정'(이나, 게시 2024-06-08). 은평구 한옥·콘셉트 문구·한복·보물찾기·캔버스 그리기·5월 5일·6시간 모두 확인. "한옥에서 하는데, 한복도 빠질 수 없다." | **t3 기재와 일치 (t3의 2024-05-05는 행사일, 게시일은 2024-06-08)** |
| C13~C17<br><https://mywedding.designhouse.co.kr/in_magazine/sub.html?at=view&info_id=75835> | 하라 사진관·원규앤노블레스(이동진)·오브센트(김성겸)·더써드마인드 부산(장현경)·세컨플로우(김백천·허수덕) 5곳과 촬영지가 실제로 이 기사에 있는지, 기사가 패션 화보·유료 광고인지 | 제목 'MYWEDDING HOT SPOT 셀프 웨딩 촬영, 이곳이 대세다'. 5곳 전부와 기재된 촬영지가 확인됨. 형식은 **스튜디오 추천 기사**이며 패션 화보·유료 광고가 아님. 같은 기사에 있는 제주 루체·웨드아일랜드는 t3가 '자연·로맨틱 무드'로 정확히 제외했음을 역확인. | **t3 기재와 일치 + t3 제외 판단도 타당** |

나머지 브런치 5건(C02·C03·C04 2편·C05)과 플랫폼·매거진 7건(C07~C12, C18)은 HTTP 요청으로 개방을 확인했다. 브런치 링크는 비브라우저 클라이언트에 대해 카카오 자동로그인 302를 돌려주지만 본문은 공개이며, 표본 2건을 실제로 열어 확인했다.

### 3.3 agent.md 목표 대비 t3 표본

| 항목 | agent.md 목표 | 실제 | 판단 |
| --- | --- | --- | --- |
| 외부 캐주얼 레퍼런스 수 | 최소 10개 | **18건** | 충족 |
| 서로 다른 무드 고르게 포함 | 도시 산책·데이트·홈/카페·스포츠·취미 등 | **7종** (카페·스포츠·취미 미확보) | **부분 충족** — 아래 참고 |
| 공식 출처 | 명시 없음 | **0건** (스튜디오 홈페이지 3곳 HTTP 403) | 한계 명시 |
| 독립 출처 수 | 명시 없음 | 18건 중 5건이 MYWEDDING 기사 1건, 4건이 플랫폼 상품 목록 | **출처 편중 있음** |

**미확보 무드**: 카페, 스포츠·취미. t3가 검색을 수행했으나 검증 가능한 개별 촬영 사례가 나오지 않았고(수집 한계 5번), 억지로 채우지 않았다. 최종 보고서 §4에도 미확보로 명시한다.

## 4. 표본 수 정직 고지

| 대상 | agent.md 목표 | 실제 확보 | 부풀림 없음 |
| --- | --- | --- | --- |
| 봉스튜디오 사진 | 최소 30장(가능하면 50장+) | **컷 94장** (세트 29개 / 추정 세션 46건) | 목표 충족 |
| 봉스튜디오 '사례' | 사진 장수보다 사례 수 우선 | **추정 세션 46건** — 하한 추정치 | 세션 수는 **추정**임을 표기 |
| 외부 캐주얼 레퍼런스 | 최소 10개 | **18건 / 무드 7종** | 목표 충족(무드 2종 미확보) |
| 실제 후기(봉스튜디오) | 명시 없음 | **0건** — 전부 HOLD | 네이버 블로그 차단·인스타 로그인 월 |

## 5. 남은 한계 (보고서 §1 주의사항으로 이관)

1. **봉스튜디오 실제 후기 0건.** 네이버 블로그가 크롤러 차단, 인스타그램 `@bongstudio_`은 로그인 월, 웨딩크라우드 후기 6건은 개별 URL 미노출. 공개된 것은 공식·제휴 포트폴리오뿐이고, 이는 스튜디오가 선별해 올린 자료다.
2. **주소 표기 2종.** 공식 홈 `경기도 하남시 미사동로40번길 124-27` vs wedding21(2024-12) `경기도 하남시 미사동 203-7`. 둘 다 하남시 미사동이지만 현재 촬영장 주소는 직접 확인이 필요하다.
3. **세션 수는 추정.** 카메라 프레임 번호 간격 300 기준 군집이며, 기준을 바꾸면 값이 변한다. 커플 수는 산출하지 않았다.
4. **계절 표기는 추정.** 사진 속 식생·광질에서 읽었고 촬영 일자는 공개되지 않았다.
5. **제휴사 명시 주의 문구**: "앨범의 성격상 날씨나 계절에 따라 촬영의 컨셉이 샘플과 달라질 수 있음."
6. **t3 출처 편중·미확보 무드** (§3.3).
