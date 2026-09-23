# prompt.md — 이번 오케스트레이션에서 실제로 내린 명령 전문

하남 봉스튜디오 웨딩 콘셉트 리서치를 t1~t4로 나눠 실행했을 때 사용한 요청·스펙·CLI 명령을 그대로 모아둔 기록이다.
t2/t3/t4 스펙은 Orca에 등록된 원문(`task-list --json` 의 `spec` 필드)을 그대로 옮긴 것이라 재실행하면 동일하게 재현된다.

- Run: `run_a49004dcd4fc`
- 실행일: 2026-09-20
- 작업 폴더: `C:/Users/taehoonlee/orca/projects/뜔희와 튤훈의 웨딩촬영♥️`
- 규칙 근거 파일: `agent.md`(조사 범위·분류 체계·산출물 형식), `hook.md`(하남 봉스튜디오 출처 검증 훅)

---

## 0. 사용자 원본 요청

`/orchestration` 으로 전달된 원문:

```text
각 AI들이 쉬지않고 일을 할 수 있도록 ai들이 쉬고 있는지 일을 하고 있는지 5분에 한번씩 감시하고 명령
을 내려줘.(t1)
2개의 Claude Code가 각각 세부 업무를 수행해줘.
1번 Claude는 agent.md의 봉스튜디오 정보를 수집해줘.(t2)
2번 Claude는 agent.md의 캐주얼 사진 정보를 수집해줘.(t3)

마지막으로 t4는 t2,t3가 수집한 정보를 hook 규칙에 기반해서 검증하고 오류가 없다면 html 문서로 보고
해줘.(t4)
```

턴 중간 추가 지시:

```text
한국어로 말해라
```

---

## 1. 작업 구조 (DAG)

```text
t2 (봉스튜디오 수집) ─┐
                      ├─→ t4 (hook 검증 → HTML 보고)
t3 (캐주얼 수집) ─────┘

t1 (코디네이터) = 위 셋을 5분 주기로 감시하며 명령
```

| 태스크 | Task ID | 의존성 | 담당 |
| --- | --- | --- | --- |
| t1 | (코디네이터 자신) | — | 감시·정산 |
| t2 | `task_ee8146fa9299` | 없음 | Claude 워커 1 |
| t3 | `task_5beeda31594b` | 없음 | Claude 워커 2 |
| t4 | `task_927612e0a4fa` | t2, t3 | Claude 워커 (t2 터미널 재사용) |

---

## 2. t1 — 코디네이터(감시) 명령

t1은 워커에게 보내는 프롬프트가 아니라 코디네이터가 직접 도는 루프다.

### 2-1. Run 생성

```bash
orca orchestration run-create   --objective "하남 봉스튜디오 웨딩 콘셉트 리서치 및 검증 보고서(한글 인코딩 테스트)" --json
```

### 2-2. 5분 주기 감시 루프 (총 8회 순회)

```bash
# (1) 5분간 워커 이벤트 대기
orca orchestration check --wait   --types "worker_done,escalation,question" --timeout-ms 300000 --json

# (2) 빈 결과(타임아웃)이면 '쉬고 있는지 일하고 있는지'를 직접 확인
orca orchestration worker-list --run run_a49004dcd4fc --include-remote --json
orca orchestration worker-show --dispatch <dispatch_id> --json          # 하트비트/상태
orca orchestration worker-read  --dispatch <dispatch_id> --source terminal --limit 15 --json
ls -l research/ report/                                                  # 산출물 증가 확인

# (3) 메시지를 받았으면 처리 후 ack 하면서 다음 대기로 이어감
orca orchestration check --ack <delivery_id> --wait   --types "worker_done,escalation,question" --timeout-ms 300000 --json
```

판정 기준으로 삼은 것:

- `projection.liveness.verdict` 가 `live` 인지
- `projection.attention.requiresAction` 과 `projection.nextAction`
- 터미널 출력이 실제로 갱신되는지, 결과 파일 크기가 늘어나는지
- **유휴(빈 `❯` 프롬프트 + worker_done 없음)일 때만 독촉 명령을 보낸다.** 이번 실행에서는 8회 모두 워커가 작업 중이어서 독촉을 보내지 않았다.
- 응답이 없다는 사실(absence)만으로는 중단·재시도·릴리스를 하지 않는다. 종료는 양성 증거가 있을 때만.

### 2-3. 완료 정산

```bash
orca orchestration worker-release --dispatch <dispatch_id> --json
orca orchestration worker-list --run run_a49004dcd4fc --terminal-state reclaimable --json  # 0이 될 때까지
```

---

## 3. t2 — 1번 Claude에게 내린 명령 (봉스튜디오 정보 수집)

### 등록·기동 명령

```bash
orca orchestration task-create --run run_a49004dcd4fc   --task-title "t2 봉스튜디오 콘셉트 수집" --display-name "t2 봉스튜디오"   --spec "<아래 스펙 전문>" --json

orca orchestration worker-start --run run_a49004dcd4fc   --task task_ee8146fa9299 --worktree current --agent claude --json
```

### 스펙 전문

```text
[t2] 하남 봉스튜디오 웨딩촬영 콘셉트 사례 수집

TARGET(대상): 작업 폴더 'C:/Users/taehoonlee/orca/projects/뜔희와 튤훈의 웨딩촬영♥️'. 먼저 agent.md(특히 '조사 범위 > 1. 봉스튜디오 콘셉트', '분류 체계', '수집 및 많이 촬영됨 판단 방법')와 hook.md 전문을 읽고 그 규칙을 그대로 따른다.

CHANGE(산출): 웹 리서치로 하남 미사리 봉스튜디오(@bongstudio_, 경기도 하남시 미사동 203-7)의 실제 웨딩촬영 사례를 수집하고, 항목마다 hook.md의 3가지 강제 검증 규칙을 '수집 표에 추가하기 직전' 적용해 PASS/HOLD/EXCLUDE를 판정한 뒤, 결과를 'research/t2_bongstudio.md' 한 파일에 한국어 마크다운으로 기록한다. 파일 구성: (1)조사 요약(조사 기간, 실제 확인 사례 수, 접근 실패 건수), (2)사례별 상세 표 — 컬럼: 사례ID/카테고리/세트·배경/구도/의상/계절/원본링크/하남 식별 근거/출처 유형(공식·제휴·실제후기)/판정, (3)agent.md 분류 체계 6개 카테고리별 '서로 다른 촬영 사례 수' 집계표를 내림차순 정렬, (4)카테고리별 참고 후보 3~5건 선별.

CONSTRAINTS(제약): URL을 절대 지어내지 말 것 — 본인이 실제로 열어보았거나 검색 결과에서 직접 확인한 링크만 기록한다. 인스타그램이 로그인 월(login wall)로 막혀 원문 확인이 불가하면 그 사례는 HOLD로 남기고 PASS로 올리지 않는다. 하남 식별 근거가 없으면 EXCLUDE이며 동명 해외 'Bong Studio'나 국내 유사 상호 혼입을 반드시 배제한다. 목표 표본은 30건 이상이지만, 검증 가능한 건수가 부족하면 행을 채워 넣지 말고 실제 확보 건수를 요약에 정직하게 명시한다. 사실과 추정을 구분해 표기한다. 타 스튜디오 캐주얼 레퍼런스는 t3 담당이므로 절대 수집하지 않는다. git commit/push 금지.

OWNERSHIP(소유권): 'research/t2_bongstudio.md' 파일만 생성·편집한다. agent.md, hook.md, research/t3_casual.md, report/ 이하 파일은 읽기만 하고 수정 금지.

ACCEPTANCE(완료 증거): research/t2_bongstudio.md가 존재하고, 모든 사례 행에 원본링크·하남 식별 근거·출처 유형·판정 4개 값이 채워져 있으며, 카테고리별 사례 수 집계표와 실제 표본 수·조사 기간이 요약에 적혀 있을 것. worker_done 시 --files-modified 에 해당 경로를, 요약 3문장에 'PASS 건수/HOLD 건수/EXCLUDE 건수'를 반드시 포함한다.

질문이 생기면 프리앰블의 ask 명령으로 코디네이터에게 물어라(로컬 질문 TUI 사용 금지). 웹 접근 권한이 거부되면 즉시 ask 또는 escalation 으로 알려라.
```

---

## 4. t3 — 2번 Claude에게 내린 명령 (캐주얼 사진 정보 수집)

### 등록·기동 명령

```bash
orca orchestration task-create --run run_a49004dcd4fc   --task-title "t3 캐주얼 사진 레퍼런스 수집" --display-name "t3 캐주얼"   --spec "<아래 스펙 전문>" --json

orca orchestration worker-start --run run_a49004dcd4fc   --task task_5beeda31594b --worktree current --agent claude --json
```

### 스펙 전문

```text
[t3] 캐주얼·라이프스타일 웨딩촬영 레퍼런스 수집 (타 스튜디오 허용)

TARGET(대상): 작업 폴더 'C:/Users/taehoonlee/orca/projects/뜔희와 튤훈의 웨딩촬영♥️'. 먼저 agent.md(특히 '조사 범위 > 2. 타 스튜디오 캐주얼 콘셉트', 분류 체계의 '캐주얼·라이프스타일' 행, '품질 기준' 마지막 항목)와 hook.md 전문을 읽는다.

CHANGE(산출): 캐주얼·라이프스타일 무드의 웨딩/커플 촬영 레퍼런스를 수집해 'research/t3_casual.md' 한 파일에 한국어 마크다운으로 기록한다. 파일 구성: (1)조사 요약(조사 기간, 확보 레퍼런스 수, 무드 분포), (2)레퍼런스 상세 표 — 컬럼: 사례ID/스튜디오 또는 촬영 장소/무드 분류/의상/포즈·상호작용/계절·시간대/원본링크/출처 유형(공식·제휴·실제후기)/봉스튜디오 재현 가능 여부, (3)무드별 요약. 최소 10개 이상, 서로 다른 무드(도시 산책, 데이트, 홈·카페, 스포츠·취미 등)를 고르게 포함한다.

CONSTRAINTS(제약): 이 카테고리만은 촬영 장소를 봉스튜디오로 제한하지 않는다. 다만 각 사례에 스튜디오/촬영 장소를 반드시 분명히 표시하고, '봉스튜디오 재현 가능 여부'는 확인 전까지 예외 없이 '확인 필요'로 적는다. 수집한 사례를 봉스튜디오 촬영 사례로 표기하거나 봉스튜디오 인기 순위 집계에 넣지 않는다. 패션 화보·상업 광고·AI 생성 이미지는 제외한다. 웨딩 전문 스튜디오 또는 신뢰 가능한 실제 촬영 후기 출처만 사용한다. URL을 절대 지어내지 말 것 — 실제로 열어보았거나 검색 결과에서 직접 확인한 링크만 기록하고, 확인 불가한 항목은 표에서 빼거나 '확인 불가'로 명시한다. 10개를 못 채우면 억지로 채우지 말고 실제 확보 수를 요약에 정직히 밝힌다. 봉스튜디오 자체 콘셉트 수집은 t2 담당이므로 하지 않는다. git commit/push 금지.

OWNERSHIP(소유권): 'research/t3_casual.md' 파일만 생성·편집한다. agent.md, hook.md, research/t2_bongstudio.md, report/ 이하 파일은 읽기만 하고 수정 금지.

ACCEPTANCE(완료 증거): research/t3_casual.md가 존재하고, 모든 레퍼런스 행에 스튜디오·장소, 무드, 원본링크, 출처 유형, 재현 가능 여부('확인 필요') 값이 채워져 있으며, 서로 다른 무드가 4종 이상 포함되어 있을 것. worker_done 시 --files-modified 에 해당 경로를, 요약 3문장에 '확보 레퍼런스 수'와 '포함된 무드 종류'를 반드시 포함한다.

질문이 생기면 프리앰블의 ask 명령으로 코디네이터에게 물어라(로컬 질문 TUI 사용 금지). 웹 접근 권한이 거부되면 즉시 ask 또는 escalation 으로 알려라.
```

---

## 5. t4 — 검증 및 HTML 보고 명령

### 등록·기동 명령

```bash
orca orchestration task-create --run run_a49004dcd4fc   --task-title "t4 hook 검증 및 HTML 보고서" --display-name "t4 검증·보고"   --deps '["task_ee8146fa9299","task_5beeda31594b"]'   --spec "<아래 스펙 전문>" --json

# t2/t3 완료 후, t2가 쓰던 검증된 터미널을 재사용해 기동
orca orchestration worker-start --run run_a49004dcd4fc   --task task_927612e0a4fa --worktree current   --terminal term_6234f977-e853-4cb8-aba7-d4801cc1db14 --json
```

### 스펙 전문

```text
[t4] t2·t3 수집물의 hook 규칙 검증 및 최종 HTML 보고서 작성

TARGET(대상): 작업 폴더 'C:/Users/taehoonlee/orca/projects/뜔희와 튤훈의 웨딩촬영♥️'. 입력 파일은 'research/t2_bongstudio.md'(봉스튜디오 수집물)와 'research/t3_casual.md'(캐주얼 레퍼런스). 규칙 근거는 hook.md 전문과 agent.md의 '최종 산출물 형식' 및 '품질 기준'.

CHANGE(산출): 1단계 검증 — 두 입력 파일의 모든 항목을 hook.md 기준으로 재검증하고 검증 로그를 'research/t4_validation.md'에 남긴다. 2단계 보고 — 검증에서 구조적 오류가 없을 때만 최종 보고서를 'report/wedding_concept_report.html' 에 한국어 HTML로 작성한다.

검증 기준(중요, 두 입력의 기준이 다르다):
(A) t2(봉스튜디오) 항목 — hook.md의 3가지 강제 검증 규칙을 그대로 적용한다. 하남 식별자(경기도 하남시 미사동 203-7 / 하남 미사리 촬영장 / 공식 인스타 @bongstudio_ / 하남 촬영장 명시 공식·제휴 페이지) 중 최소 1개 확인, 동명 해외 'Bong Studio' 및 국내 유사 상호 배제, 원본 링크와 하남 식별 근거 동시 기록 — 3개 모두 충족 PASS, 하나라도 미충족 EXCLUDE, 근거 불충분하나 확인 가능성 있으면 HOLD. PASS 항목의 링크가 실제로 열리는지 재확인하고, 끊긴 링크와 출처 불명 항목은 최종 후보에서 뺀다.
(B) t3(캐주얼) 항목 — hook.md의 하남 식별자 규칙은 봉스튜디오 전용이므로 t3 항목에는 적용하지 않는다. t3 항목이 하남 식별 근거가 없는 것은 정상이며 이를 이유로 EXCLUDE 하지 말 것. t3에 적용할 검증은 다음 4가지다: 각 항목에 봉스튜디오가 아닌 스튜디오·장소가 분명히 표시되었는가, 봉스튜디오 재현 가능 여부가 '확인 필요'로 표기되었는가, t3 항목이 봉스튜디오 사례 집계·순위표에 단 하나도 섞이지 않았는가, 패션 화보·상업 광고·AI 생성 이미지가 아닌가.

HTML 보고서는 agent.md '최종 산출물 형식'의 6개 절 순서를 그대로 따른다: 1)요약(조사 기간·표본 수·핵심 결론·주의사항) 2)봉스튜디오 인기 콘셉트 순위표 3)카테고리별 사진 보드(한 줄 설명·출처 링크·재현 시 체크할 점) 4)별도 섹션 타 스튜디오 캐주얼 레퍼런스(봉스튜디오 사례와 섞지 말 것) 5)촬영 전 봉스튜디오에 확인할 질문 6)최종 쇼트리스트 3~5개. 모든 인용 사진에 원본 링크를 바로 붙이고, 사실과 추정을 시각적으로 구분한다. 단일 HTML 파일로 자체 완결되게 CSS를 인라인 작성하고 모바일 폭에서도 표가 깨지지 않게 한다.

CONSTRAINTS(제약): 입력 파일에 없는 사례·링크를 새로 지어내지 않는다. 표본 수가 agent.md 목표(봉스 30건, 캐주얼 10건)에 못 미치면 숫자를 부풀리지 말고 요약에 실제 수치와 한계를 명시한다. EXCLUDE·HOLD 항목은 순위 집계에서 제외한다. 검증 결과 구조적 오류(예: t3 항목이 봉스 순위에 혼입, PASS 항목에 하남 근거 누락, 링크 다수 파손)가 남아 있으면 HTML을 쓰지 말고 worker_done --outcome failed 로 오류 목록을 보고한다 — 이것이 '오류가 없다면 보고'라는 게이트다. git commit/push 금지.

OWNERSHIP(소유권): 'research/t4_validation.md' 와 'report/wedding_concept_report.html' 두 파일만 생성·편집한다. agent.md, hook.md, research/t2_bongstudio.md, research/t3_casual.md 는 읽기 전용이며 절대 수정하지 않는다.

ACCEPTANCE(완료 증거): research/t4_validation.md 에 항목별 판정표(원본 링크/하남 식별 근거/출처 유형/판정)와 t3용 4가지 검증 결과가 기록되어 있고, 오류가 없을 경우 report/wedding_concept_report.html 이 6개 절을 모두 갖춘 상태로 존재할 것. worker_done 시 --files-modified 와 --report-path 를 채우고, 요약 3문장에 'PASS/HOLD/EXCLUDE 최종 건수'와 'HTML 생성 여부'를 반드시 포함한다.

질문이 생기면 프리앰블의 ask 명령으로 코디네이터에게 물어라(로컬 질문 TUI 사용 금지).
```

---

## 6. 사고 복구 시 추가로 내린 명령

최초 기동한 t2·t3 워커에 스펙이 전달되지 않았다. Orca "새 에이전트 탭" 실행 설정에 들어 있던
`'--dangerously-skip-permissions'` 가 따옴표째 Claude의 첫 프롬프트로 소비되면서, 주입된 스펙이 유실된 것이다.
Orca 리시트는 `input_accepted` / `turnStart: observed` 로 정상처럼 보였지만 **엉뚱한 턴을 관측한 값**이었다.

```bash
# 1) 터미널을 죽이지 않고 디스패치만 펜싱 (worker-stop 이 아니라 abandon)
orca orchestration worker-abandon --dispatch ctx_21027d43da68 --json   # t2 최초
orca orchestration worker-abandon --dispatch ctx_2b3d2bbe7d47 --json   # t3 최초

# 2) 살아 있는 같은 터미널에 --retry-of 로 재투입 (신규 기동을 피해 버그 재발 방지)
orca orchestration worker-start --run run_a49004dcd4fc --task task_ee8146fa9299   --retry-of ctx_21027d43da68 --worktree current   --terminal term_6234f977-e853-4cb8-aba7-d4801cc1db14 --json

orca orchestration worker-start --run run_a49004dcd4fc --task task_5beeda31594b   --retry-of ctx_2b3d2bbe7d47 --worktree current   --terminal term_7859153a-8036-4f9b-9bd3-65c97eba861c --json

# 3) 리시트를 믿지 말고 터미널에 스펙 본문이 실제로 찍혔는지 눈으로 확인
orca orchestration worker-read --dispatch <new_dispatch_id> --source terminal --limit 40 --json
```

---

## 7. 처음부터 재현하는 순서

```bash
orca status --json
orca orchestration run-create --objective "<목표>" --json
orca orchestration task-create ... --spec "<t2 스펙>" --json
orca orchestration task-create ... --spec "<t3 스펙>" --json
orca orchestration task-create ... --deps '["<t2>","<t3>"]' --spec "<t4 스펙>" --json
orca orchestration worker-start --task <t2> --worktree current --agent claude --json
orca orchestration worker-start --task <t3> --worktree current --agent claude --json
# → 각 기동 직후 worker-read 로 스펙 주입 검증 (6장 참고)
# → 5분 주기 check --wait 루프 (2장)
# → t2/t3 완료 후 worker-start --task <t4> --terminal <정착된 핸들>
# → worker-release 후 reclaimable 0 확인
```

## 8. 산출물

| 파일 | 내용 |
| --- | --- |
| `research/t2_bongstudio.md` | t2 수집물 — PASS 107 / HOLD 7 / EXCLUDE 10, 세션 46건 |
| `research/t3_casual.md` | t3 수집물 — 레퍼런스 18건 / 무드 7종 |
| `research/t4_validation.md` | t4 검증 로그 — 항목별 판정표, 게이트 결론 |
| `report/wedding_concept_report.html` | 최종 보고서 — agent.md 6개 절 |
| `research/_orchestration_state.md` | 코디네이터 진행 기록 |
