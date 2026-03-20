# plan.md

## Coordination Contract

새 에이전트는 작업 전에 반드시 아래 순서로 읽는다.

1. `SOUL.md`
2. `USER.md`
3. `memory/YYYY-MM-DD.md` (오늘 + 어제)
4. `plan.md`
5. `progress.md`

작업을 시작할 때는 `progress.md`에 시작 로그를 먼저 남긴다.

---

## Agent / Command / Skill Registry

### Prompt-based agent roles

조사 결과, 현재 로컬 prompt catalog에는 아래 역할이 있다.

- `explore` — 코드베이스/파일/패턴 조사 전용
- `planner` — 계획 수립 전용
- `executor` — 실제 구현/셋업 전용
- `verifier` — 완료 검증 전용
- `writer` — 문서/설명/정리 전용
- `architect`, `debugger`, `test-engineer`, `security-reviewer` — 필요 시 보조 역할

### Recommended OMX commands

조사 결과, 현재 이 환경에서 직접 활용 가능한 대표 명령은 아래와 같다.

- `omx explore` — 읽기 전용 조사
- `omx team` — tmux 기반 멀티 에이전트 실행
- `omx ralph` — 지속 실행 + 검증 루프
- `omx sparkshell` — 요약형 쉘 실행/검증
- `omx status`, `omx cancel`, `omx trace` — 상태 확인/정리

### Relevant skills for this repo

- `$plan` — 구조화된 계획 수립
- `$team` — 여러 에이전트 협업
- `$ralph` — 끝까지 실행/검증
- `$ultrawork` — 병렬 작업
- `$note` — 메모 저장
- `$trace` — 실행 흐름 확인
- `$pdf` — PDF 처리 시 활용
- `bitcoin-translation-style` — repo-local 번역 스킬 (`.codex/skills/bitcoin-translation-style/SKILL.md`)
- `book-reading-summary-style` — repo-local 읽는 느낌의 챕터 요약 스킬 (`.codex/skills/book-reading-summary-style/SKILL.md`)

### Project execution policy

- 조사 성격의 작업은 `explore` 또는 `omx explore`
- 실제 파일 생성/수정은 `executor`
- 큰 구조 변경 전 계획 정리는 `planner` 또는 `$plan`
- 완료 판정 전에는 `verifier` 또는 명시적 검증 로그 확보

---

## Task Board

| ID | Priority | Status | Owner | Surface | Depends on | Task | Definition of Done |
|---|---|---|---|---|---|---|---|
| BOOT-001 | P0 | done | executor | direct | - | 프로젝트 기본 문서(`SOUL.md`, `USER.md`, `plan.md`, `progress.md`) 정리 | 핵심 문서가 존재하고 협업 규칙이 명시됨 |
| BOOT-002 | P0 | done | executor | direct | BOOT-001 | 기본 디렉토리 구조 생성 | `books/`, `scripts/`, `templates/`, `memory/`, `pdf/`와 테스트 책 하위 구조가 존재함 |
| EPUB-001 | P1 | done | explore -> executor | `omx explore`, direct | BOOT-002 | `The Big Print.epub` 메타데이터/목차/본문 분리 전략 확정 | 추출 경로, 파일명 규칙, front matter 제외 규칙, 저자 기준 챕터 분리 기준이 문서화됨 |
| EPUB-002 | P1 | done | executor | direct | EPUB-001 | EPUB 추출 스크립트 초안 작성 | `scripts/`에 재사용 가능한 추출 스크립트가 생기고 테스트 책에 1회 실행 가능 |
| SCHEMA-001 | P1 | done | writer -> executor | direct | EPUB-001 | 챕터 영어 Markdown 포맷 정의 | 챕터별 영문 Markdown 템플릿과 필수 필드가 정해짐 |
| I18N-001 | P1 | done | writer -> executor | direct | SCHEMA-001 | 챕터 한국어 번역 Markdown 포맷 정의 | 영문판과 대응되는 한글 Markdown 경로/필드/번역 규칙이 정해짐 |
| QUIZ-001 | P1 | done | writer -> executor | direct | EPUB-001 | 퀴즈 JSON 스키마 정의 | 질문/선택지/정답/해설 구조가 문서화됨 |
| PDF-001 | P2 | todo | explore -> executor | direct | EPUB-001 | PDF 챕터 분리 파이프라인 설계 | 텍스트 PDF 전제에서 챕터 탐지, 제외 규칙, 저장 형식이 문서화됨 |
| SITE-001 | P2 | done | executor | direct | SCHEMA-001, I18N-001, QUIZ-001 | 정적 HTML 템플릿 초안 생성 | 영어/한국어 전환과 요약/퀴즈를 렌더링하는 기본 템플릿이 생성됨 |
| VERIFY-001 | P2 | todo | verifier | direct | EPUB-002, SITE-001 | 첫 책 MVP 검증 | 텍스트/퀴즈/HTML이 최소 1개 챕터에서 동작 확인됨 |

---

## Working Rules for Multi-Agent Sessions

- 각 작업은 반드시 위 Task Board의 ID를 기준으로 움직인다.
- `Owner`는 권장 역할이며, 실제 에이전트 이름보다 **역할 기반**으로 이어받는다.
- `Surface`는 권장 실행 표면이다.
  - `direct` = 현재 세션에서 직접 수행
  - `omx explore` = 조사 우선
  - `$plan`, `$team`, `$ralph` = 워크플로우 모드 사용
- 새 에이전트는 가장 높은 우선순위의 `todo` 또는 `in_progress` 중 **unblocked**인 작업을 선택한다.
- 상태 변경 시 `plan.md`와 `progress.md`를 함께 갱신한다.

---

## Immediate Next Recommended Task

현재 가장 먼저 진행할 작업은 `VERIFY-001`이다.

### 목표

- 생성된 퀴즈와 HTML 결과물을 검증하고
  - 구조 누락이 없는지 확인
  - 로컬 확인 증거를 남기고
  - 커밋/배포 가능한 상태로 정리한다.

### 권장 시작 방식

1. 퀴즈 파일 수와 챕터 수가 일치하는지 확인한다.
2. 생성된 HTML 페이지와 인덱스가 존재하는지 확인한다.
3. 커밋/배포 전에 결과 구조를 최종 점검한다.
