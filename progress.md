# progress.md

## Current Status

- Date: 2026-03-23
- Phase: bitcoin_essentials_bookshelf_live
- Current top unblocked task: `BITCOIN-ESSENTIALS-001` — 6번 `비트코인 낙관론` books 스캐폴드 + 챕터 추출 시작
- Blockers: 없음
- Recommended next role: `executor`

---

## Execution Log

- 2026-03-20 09:14 KST | executor | started | 프로젝트 목표 확인 및 `The Big Print.epub` 테스트 방향 파악 시작
- 2026-03-20 09:18 KST | executor | completed | `SOUL.md` 작성: 전자책을 HTML 학습 콘텐츠로 바꾸는 프로젝트 정체성과 원칙 정리
- 2026-03-20 09:21 KST | executor | completed | `SOUL.md` 업데이트: 멀티 에이전트 협업 시 `plan.md`/`progress.md`를 읽고 갱신하도록 규칙 추가
- 2026-03-20 09:25 KST | executor | started | agent / command / skill 구조 조사 후 프로젝트 셋업 파일과 기본 디렉토리 생성 시작
- 2026-03-20 09:25 KST | executor | completed | 조사 결과 반영: prompt 역할(`explore`, `planner`, `executor`, `verifier` 등), OMX 명령(`omx explore`, `omx team`, `omx ralph` 등), relevant skills(`$plan`, `$team`, `$ralph`, `$ultrawork`)를 `plan.md`에 정리
- 2026-03-20 09:25 KST | executor | completed | 생성 완료: `USER.md`, `plan.md`, `progress.md`, `books/`, `books/the-big-print/`, `scripts/`, `templates/`, `memory/`, `pdf/`
- 2026-03-20 09:26 KST | executor | completed | 요구사항 업데이트: 챕터별 영어 Markdown + 한국어 Markdown 두 버전 관리 규칙을 문서에 반영
- 2026-03-20 09:27 KST | executor | completed | 분리 기준 업데이트: 서문/추천사 등 front matter는 기본 제외, 저자 기준 챕터 단위 우선, PDF도 챕터 구분이 명확하면 유사 파이프라인으로 설계

---

## Files Created / Updated This Session

- `SOUL.md`
- `USER.md`
- `plan.md`
- `progress.md`
- `books/README.md`
- `books/the-big-print/README.md`
- `books/the-big-print/source/README.md`
- `books/the-big-print/content/README.md`
- `books/the-big-print/quiz/README.md`
- `books/the-big-print/site/README.md`
- `scripts/README.md`
- `templates/README.md`
- `pdf/README.md`
- `memory/2026-03-20.md`

---

## Handoff

### What is ready

- 멀티 에이전트가 읽을 핵심 문서 구조가 준비되었다.
- 루트 기준 협업 파일(`plan.md`, `progress.md`)이 생겼다.
- 테스트 책 `The Big Print`용 작업 디렉토리 스캐폴드가 준비되었다.

### Exact next action

1. `EPUB-001`을 시작한다.
2. `progress.md`에 시작 로그를 남긴다.
3. `The Big Print.epub`의 내부 구조를 기준으로:
   - 목차 저장 파일
   - 챕터 원문 저장 위치
   - 요약 대상 파일 구조
   를 확정한다.
4. 확정 내용을 `books/the-big-print/source/` 또는 `books/the-big-print/content/`의 문서에 반영한다.
5. 영어/한국어 두 버전의 챕터 저장 규칙도 함께 확정한다.
6. cover / foreword / dedication / appendix 등 제외 또는 보조처리 목록을 함께 정한다.

### Suggested command path

- 조사: `omx explore --prompt "Inspect epub/The Big Print.epub structure and recommend file layout for extracted toc and chapter text"`
- 구현: 필요 시 `python3` 기반 추출 스크립트 초안 작성

- 2026-03-20 09:28 KST | executor | started | EPUB-001 시작: The Big Print의 front matter 제외 목록과 저자 기준 챕터 맵 확정 작업 시작

- 2026-03-20 09:30 KST | executor | completed | EPUB-001 완료: The Big Print의 제외 목록, 챕터 맵, 경로 규칙을 source 문서와 JSON 파일로 확정
- 2026-03-20 09:30 KST | executor | started | EPUB-002 시작: 확정된 챕터 맵 기준으로 EPUB 추출 스크립트 초안 준비

- 2026-03-20 09:32 KST | executor | started | 번역 용어/관점 가이드 추가 작업 시작: 오스트리안 경제학/비트코이너 관점 반영 규칙을 skills에 문서화

- 2026-03-20 09:34 KST | executor | completed | repo-local skill 추가: `.codex/skills/bitcoin-translation-style/`에 오스트리안 경제학/비트코이너 번역 규칙과 용어집 문서화

- 2026-03-20 09:36 KST | executor | started | summary style skill 업데이트 시작: 단순 bullet 요약이 아니라 책을 읽는 느낌의 chapter summary 규칙을 repo-local skills에 추가

- 2026-03-20 09:40 KST | executor | completed | summary skill 추가: `.codex/skills/book-reading-summary-style/`에 읽는 느낌의 챕터 요약 규칙과 템플릿 문서화
- 2026-03-20 09:41 KST | executor | completed | EPUB-002 진행: `scripts/extract_epub.py` 작성 및 `The Big Print.epub`에서 24개 source chapter markdown 추출
- 2026-03-20 09:42 KST | executor | completed | Big Print 샘플 작성: 1장 `AMERICA IS BROKEN` 영어 digest 및 한국어 번역 digest 생성

- 2026-03-20 09:45 KST | executor | started | summary style 수정: 독후감/독자 반응형이 아니라 저자 논지 중심 요약 규칙으로 스킬과 샘플 갱신

- 2026-03-20 09:48 KST | executor | completed | summary style 수정 완료: 독자 반응형 표현을 제거하고 저자 논지 중심 요약 규칙으로 skill과 1장 샘플 갱신

- 2026-03-20 09:50 KST | executor | started | author-voice summary correction: 해설형 문장을 줄이고 저자 논지를 직접 압축 서술하는 스타일로 skill과 1장 샘플 재수정

- 2026-03-20 10:00 KST | executor | completed | The Big Print 전체 24개 챕터 영어 digest 초안 작성 완료
- 2026-03-20 10:00 KST | executor | completed | The Big Print 전체 24개 챕터 한국어 digest 초안 작성 완료
- 2026-03-20 10:00 KST | executor | completed | 상태 갱신: EPUB-002, SCHEMA-001, I18N-001을 done으로 반영

- 2026-03-20 10:03 KST | executor | completed | 한국어 챕터 요약 후처리: 남아 있던 영문 개념 표현 일부를 한국어 중심 용어로 정리

- 2026-03-20 10:08 KST | executor | started | QUIZ-001/SITE-001/배포 단계 시작: 퀴즈 1개씩 생성, HTML 템플릿 작성, 커밋/푸시/Vercel 배포 준비

- 2026-03-20 10:18 KST | executor | completed | QUIZ-001 완료: 24개 챕터에 대해 장당 1개 퀴즈 JSON 생성 및 schema.json 작성
- 2026-03-20 10:18 KST | executor | completed | SITE-001 완료: HTML 템플릿/스타일/build script 작성 및 24개 챕터 페이지 + index 생성
- 2026-03-20 10:18 KST | executor | completed | VERIFY-001(로컬 선행 검증) 진행: 파일 수, HTML 생성, 샘플 페이지 구조 확인

- 2026-03-20 10:22 KST | executor | completed | Git Lore commit 생성 완료: 1cc1ea4

- 2026-03-20 10:29 KST | executor | started | GitHub 원격 생성 가능 여부 확인: gh 설치/인증 상태 점검

- 2026-03-20 10:31 KST | executor | completed | bit_book 독립 git 저장소 초기화 및 스테이징 완료

- 2026-03-20 10:36 KST | executor | completed | bit_book 독립 저장소 GitHub 생성 및 push 완료: https://github.com/youngjaeshin/bit-book
- 2026-03-20 10:36 KST | executor | completed | Vercel 배포 URL 확보: https://site-ochre-omega.vercel.app

- 2026-03-20 10:40 KST | executor | started | 한국어 heading 정리: `요약`을 전체에서 `요약`으로 통일

- 2026-03-20 10:44 KST | executor | completed | 한국어 heading 통일 완료: `읽는 느낌의 요약` → `요약`, HTML 재빌드 반영

- 2026-03-20 10:49 KST | executor | completed | 퀴즈 언어 분리 반영: 영어/한국어 퀴즈를 각 언어 패널에 맞춰 분리하고 사이트 재빌드

- 2026-03-20 11:00 KST | executor | started | Big Print production 배포 시작 후 Ammous 책 다음 타깃 셋업 진행

- 2026-03-20 11:03 KST | executor | completed | Big Print production 배포 완료: https://site-ochre-omega.vercel.app
- 2026-03-20 11:03 KST | executor | completed | 다음 책 초기화: `Principles of Economics - Ammous, Saifedean_9883.epub` 메타데이터/TOC 추출 및 books/principles-of-economics 스캐폴드 생성
- 2026-03-20 11:03 KST | executor | completed | plan/progress 갱신: 다음 우선 작업을 EPUB-003 (Principles of Economics 분리 전략)으로 변경

- 2026-03-20 11:08 KST | executor | started | EPUB-003 시작: Principles of Economics의 제외 목록과 chapter-level 분리 기준 확정 작업 시작

- 2026-03-20 11:12 KST | executor | completed | EPUB-003 완료: Principles of Economics의 front matter 제외 목록, chapter-level 포함 기준, subsection anchor 병합 기준 확정

- 2026-03-20 11:16 KST | executor | completed | EPUB-004 완료: Principles of Economics chapter-map 기준 source chapter 18개 추출

- 2026-03-20 11:24 KST | executor | started | Principles of Economics digest 단계 시작: 18개 chapter 영어/한국어 digest 생성 작업 시작

- 2026-03-20 11:28 KST | executor | completed | Principles of Economics 영어 digest 18개 초안 작성 완료
- 2026-03-20 11:28 KST | executor | completed | Principles of Economics 한국어 digest 18개 초안 작성 완료

- 2026-03-20 11:36 KST | executor | started | Principles of Economics 퀴즈/HTML/배포 단계 시작: 장당 퀴즈 생성, 사이트 빌드, Vercel preview 배포

- 2026-03-20 11:40 KST | executor | completed | Principles of Economics 장당 1개 퀴즈 18개 생성 완료
- 2026-03-20 11:40 KST | executor | completed | Principles of Economics HTML 사이트 빌드 완료 (18개 chapter page + index)

- 2026-03-20 11:43 KST | executor | completed | Principles of Economics 퀴즈/HTML 결과 GitHub push 완료
- 2026-03-20 11:43 KST | executor | started | Principles of Economics 전용 Vercel project link 및 preview 배포 시작

- 2026-03-20 11:46 KST | executor | completed | Principles of Economics Vercel 배포 완료: https://principles-of-economics-site.vercel.app

- 2026-03-20 12:00 KST | executor | started | 멀티북 통합 사이트 작업 시작: 홈에서 여러 책을 고르는 구조로 통합 빌드/배포

- 2026-03-20 11:50 KST | executor | completed | 멀티북 통합 사이트 빌드 완료: 홈에서 책 선택 후 책별 페이지로 이동하는 구조 생성

- 2026-03-20 11:55 KST | executor | completed | 통합 라이브러리 사이트 GitHub push 완료
- 2026-03-20 11:55 KST | executor | started | 통합 라이브러리 Vercel project link 및 preview 배포 시작

- 2026-03-20 12:04 KST | executor | completed | 통합 라이브러리 Vercel 배포 완료: https://bit-book-library.vercel.app
- 2026-03-20 12:04 KST | executor | completed | Principles of Economics 검토 링크는 통합 라이브러리 안의 책 페이지로 이동하도록 대체

- 2026-03-20 12:12 KST | executor | started | 통합 사이트 홈 디자인 개편 시작

- 2026-03-20 12:16 KST | executor | completed | 통합 사이트 홈 디자인 개편 반영 및 라이브러리 재빌드 완료

- 2026-03-20 12:20 KST | executor | completed | 통합 사이트 홈 디자인 개편 커밋/푸시 및 production 재배포 시작

- 2026-03-20 12:24 KST | executor | completed | 홈 단순화 반영: hero 설명/통계/가이드 섹션 제거, 바로 라이브러리 목록이 보이도록 재빌드

- 2026-03-20 12:34 KST | executor | started | 홈 밀도 조정 및 카드/목록 보기 전환 기능 추가 작업 시작

- 2026-03-20 12:38 KST | executor | completed | 카드 축소 및 카드형/목록형 전환 기능 반영, 통합 사이트 재빌드 완료

- 2026-03-20 12:40 KST | executor | completed | 목록형 보기 밀도 개선: 게시판처럼 한 줄씩 많이 보이도록 list mode 스타일 조정 및 재빌드

- 2026-03-20 12:48 KST | executor | started | 통합 챕터 페이지 상대경로 수정 시작: CSS/Library 링크 깨짐 수정

- 2026-03-20 12:49 KST | executor | completed | 통합 챕터 페이지 상대경로 수정 및 라이브러리 재빌드 완료

- 2026-03-20 12:54 KST | executor | completed | 퀴즈 섹션 제목 언어 분리 반영: 영어 탭은 Quiz, 한국어 탭은 퀴즈

- 2026-03-20 13:00 KST | executor | started | 새 스킬 설계 시작: 내부용 영어 EPUB → 한국어 EPUB 변환 워크플로우 설계

- 2026-03-20 13:04 KST | executor | completed | 새 스킬 설계 완료: `.codex/skills/epub-translate-ko/`에 영어 EPUB → 한국어 EPUB 변환 워크플로우, 파이프라인, 재조립 품질 기준 문서화

- 2026-03-20 13:10 KST | executor | completed | epub-translate-ko 기본 스크립트 구현 및 샘플 round-trip 검증(unpack/export/repack/validate) 완료

- 2026-03-20 13:18 KST | executor | started | The Big Print 한국어 EPUB 생성 시작: unpack/export/번역/재조립 workflow 실행

- 2026-03-20 13:24 KST | executor | completed | The Big Print 번역 번들 적용, 한국어 TOC 반영, `.ko.epub` 생성 및 구조 검증 완료

- 2026-03-20 13:30 KST | executor | completed | The Big Print 한국어 EPUB 생성 성공: 번역 적용 버그 수정 후 `.ko.epub` 재생성 및 검증 통과

- 2026-03-20 13:36 KST | executor | started | Big Print 완전 번역판 확장: excluded/front/back matter 번역 bundle 생성 완료

- 2026-03-20 13:42 KST | executor | started | 사용자 피드백 대응: 생성 EPUB 내부 실제 한글 반영 여부 재점검 및 완전 번역판 재생성 준비

- 2026-03-20 13:48 KST | executor | completed | Big Print 완전 번역판 재생성 완료: 제목 메타데이터는 영어 유지, front/back matter 포함 `.full.ko.epub` 생성 및 검증 통과

- 2026-03-20 13:56 KST | executor | completed | Books 호환성 보정판 생성: 영어 제목 유지, ko 언어 메타데이터, 고유 identifier, TOC placeholder 제거를 반영한 `.full.ko.safe.epub` 생성

- 2026-03-20 14:02 KST | executor | started | 완전 번역판 정리 단계 시작: translated_text 내부에 남은 영어 문장 잔재 탐지 및 정제 작업 시작

- 2026-03-20 14:09 KST | executor | completed | 영어 잔재 탐지 스크립트 추가 및 The Big Print 번역 산출물에 대한 residue report 생성 완료

- 2026-03-20 14:14 KST | executor | started | 영어 잔재 2차 정리 패스 시작: 보고서 경로 점검 후 재번역 대상 선별

- 2026-03-20 14:18 KST | executor | started | refresh 실패 원인 점검: 원본/작업본 XHTML 파싱 상태 확인

- 2026-03-20 14:30 KST | executor | started | 사용자 제보 영어 잔재 직접 수정 패스 시작: 실제 예시 문장 기준으로 잔재 위치 추적 및 정리

- 2026-03-20 14:36 KST | executor | completed | 사용자 제보 잔재 문장(Opening Scene/Author's Story) 수정 반영 후 Big Print 안전판 EPUB 재생성

- 2026-03-20 14:50 KST | executor | completed | 번역 정책 강화: 인용문/볼드/기울임 등 inline 강조 텍스트도 고유명사가 아니면 한국어로 번역하도록 스킬 규칙 업데이트

- 2026-03-20 15:05 KST | executor | started | 다국어 오염 정리 패스 시작: 영어 잔재뿐 아니라 힌디어/기타 외국 문자 오염도 함께 탐지 및 수정

- 2026-03-20 15:18 KST | executor | completed | 최신 잔재 수정 반영 후 Big Print 안전판 EPUB 재생성 및 residue report-current 갱신

- 2026-03-20 15:30 KST | executor | completed | 남은 기관명/제목류 잔재 정리 반영 후 Big Print 안전판 EPUB 재생성 및 residue report-current 재갱신

- 2026-03-20 15:42 KST | executor | completed | 대규모 잔재 치환 패스 반영 후 Big Print 안전판 EPUB 재생성 및 residue report-current 재갱신

- 2026-03-20 16:05 KST | executor | completed | XML parse 오류 원인 확인 및 수정: part0032의 잘못된 ampersand(S&S&P) 보정, 전체 XHTML 파싱 재점검

- 2026-03-23 09:33 KST | executor | completed | `epub/비트코인 필수/` 소스 묶음 확인: 1~12 책 목록을 EPUB/PDF, EN+KO 쌍 여부 기준으로 분류 완료

- 2026-03-23 09:41 KST | executor | completed | `library-site` 메인 UI를 비트코인 필수 1~12 서가형 홈으로 재설계: 번호 배지, 표지 카드, 책 상세 진입 페이지 구조 반영

- 2026-03-23 09:49 KST | executor | completed | `screenshot/` 직접 촬영 표지를 library cover로 우선 사용하도록 빌드 로직 반영 및 비트코인 필수 12권 상세 placeholder 페이지 생성

- 2026-03-23 10:11 KST | executor | completed | 표지 스크린샷 자동 crop 적용: 12장 전체를 점검해 균일한 외곽 여백을 보수적으로 제거하고 library-site 재빌드 완료

- 2026-03-23 10:18 KST | executor | completed | 상단 브랜드를 `btc-book`으로 변경하고 카테고리 탭(`비트코인 필수`, `자유주의 필수`, `비트코인 일반`) 추가: 현재는 비트코인 필수만 활성화

- 2026-03-23 10:19 KST | executor | completed | 비트코인 필수 서가형 홈을 production 재배포: https://bit-book-library.vercel.app

- 2026-03-23 10:42 KST | executor | completed | 12권 전체 웹 챕터맵 초안 v1 저장: `memory/2026-03-23-web-chapter-map-v1.md` (원서 기준, KO-only 예외, 책별 착수 전 점검 원칙 확정)

- 2026-03-23 11:05 KST | executor | completed | 6번 `비트코인 낙관론` 착수: `books/the-bullish-case-for-bitcoin/` 스캐폴드, 원서 TOC/메타데이터 추출, 8개 웹 단위 chapter-map v1 작성, spine-range 추출로 source chapter markdown 8개 생성

- 2026-03-23 11:32 KST | executor | completed | 6번 `비트코인 낙관론` digest/quiz 단계 완료: EN digest 8개, KO digest 8개, 퀴즈 8개 생성 후 책 사이트 빌드 및 통합 library-site 재빌드(로컬 검증 완료)

- 2026-03-23 11:58 KST | executor | completed | 요약 원칙 보정: 책 전체와 웹 단위 분량에 비례해 digest 길이를 늘리고, 고정된 짧은 분량으로 압축하지 않기로 확정(향후 전 책 공통 적용)

- 2026-03-23 12:14 KST | executor | completed | 6번 `비트코인 낙관론` digest 재작성: 웹 단위 분량에 비례해 EN/KO 요약을 더 길고 촘촘하게 보강하고 챕터 이전/다음 네비게이션까지 반영

- 2026-03-23 12:32 KST | executor | completed | UI/quiz 원칙 보정: 퀴즈 정답 길이 편향 제거, KO가 있으면 한국어를 기본 탭으로 사용, 챕터 목록/이전다음 네비게이션도 한국어 제목을 우선 표시하도록 확정

- 2026-03-23 12:45 KST | executor | started | 로컬 전용 연속 작업 모드 전환: 사용자 검수 대기 없이 1번부터 12번까지 순차 진행, 각 책 완료 후 자체검수 수행

- 2026-03-23 12:55 KST | executor | started | 1번 `모두를 위한 비트코인` 착수: KO 원본 기준 스캐폴드/메타데이터 보정/TOC 정리/12개 웹 단위 chapter-map v1 작성 및 source markdown 12개 추출 완료

- 2026-03-23 18:05 KST | executor | started | Ralph continue: The Big Print 한국어 EPUB 최종 점검 재개 — XML 파싱 오류와 본문 영어 잔재를 다시 전수 점검 후 재조립

- 2026-03-23 13:10 KST | executor | completed | 1번 `모두를 위한 비트코인` digest/quiz 단계 완료: KO 원본 기준 12개 웹 단위에 대해 EN digest 12개, KO digest 12개, 퀴즈 12개 생성 후 책 사이트 및 library-site 로컬 빌드/자체검수 완료

- 2026-03-23 13:12 KST | executor | started | 2번 `왜 그들만 부자가 되는가` 착수: EN 원서 기준으로 TOC/메타데이터/웹 챕터맵 점검 시작

- 2026-03-23 13:25 KST | executor | completed | 2번 `왜 그들만 부자가 되는가` 구조 점검 완료: EN 원서 기준 스캐폴드/메타데이터/TOC 정리, 11개 웹 단위 chapter-map v1 작성 및 source markdown 11개 추출 완료
- 2026-03-23 18:42 KST | executor | completed | The Big Print 한국어 EPUB 정리 패스 진행: 본문/강조문/다수 각주 영어 잔재를 추가 번역하고 `.full.ko.safe.epub` 재패키징 및 XML/EPUB 검증 통과

- 2026-03-23 13:45 KST | executor | completed | 2번 `왜 그들만 부자가 되는가` digest/quiz 단계 완료: EN 원서 기준 11개 웹 단위에 대해 EN digest 11개, KO digest 11개, 퀴즈 11개 생성 후 책 사이트 및 library-site 로컬 빌드/자체검수 완료

- 2026-03-23 13:47 KST | executor | started | 3번 `달러는 왜 비트코인을 싫어하는가` 착수: EN 원서 기준 TOC/웹 단위 분할 상세 설계 시작

- 2026-03-23 14:10 KST | executor | completed | 3번 `달러는 왜 비트코인을 싫어하는가` 구조 점검 완료: EN 원서 기준 스캐폴드/메타데이터/TOC 정리, fragment-aware 분할을 활용한 16개 웹 단위 chapter-map v1 작성 및 source markdown 16개 추출 완료
- 2026-03-23 19:14 KST | executor | completed | The Big Print EPUB 잔재 정리 추가 패스: 설명형 영어 각주 다수 한국어화. 현재 residue report는 표지 영어 제목 + 일부 citation/저자명/책제목 위주로 축소됨.
- 2026-03-23 19:26 KST | executor | completed | The Big Print EPUB 잔재 보고서 축소: 현재 남은 residue는 표지 영어 제목(`What Happened To America...`)과 citation 저자명 위주로 정리됨. `.full.ko.safe.epub` 재패키징/검증 통과.
- 2026-03-23 19:34 KST | executor | completed | The Big Print 한국어 EPUB 최종 정리 완료: `.full.ko.safe.epub` 재패키징/검증 통과, residue report는 표지 영어 제목과 인명/저자명만 남음.
- 2026-03-23 19:38 KST | executor | started | 4번 `21가지 교훈` 착수: 원서 파일 탐색 및 스캐폴드/메타데이터/TOC 점검 시작

- 2026-03-23 14:32 KST | executor | completed | 3번 `달러는 왜 비트코인을 싫어하는가` digest/quiz 단계 완료: EN 원서 기준 16개 웹 단위에 대해 EN digest 16개, KO digest 16개, 퀴즈 16개 생성 후 책 사이트 및 library-site 로컬 빌드/자체검수 완료

- 2026-03-23 14:34 KST | executor | started | 4번 `21가지 교훈` 착수: EN 원서 기준 구조 점검 및 웹 단위 설계 시작
- 2026-03-23 19:42 KST | executor | completed | 4번 `21가지 교훈` 스캐폴드/메타데이터/TOC 추출 완료: `books/21-lessons/` 생성, EN 원서 메타데이터 및 TOC 25개 항목 정리
- 2026-03-23 19:44 KST | executor | completed | 4번 `21가지 교훈` 구조 점검 완료: 8개 웹 단위 chapter-map v1 작성 및 source markdown 8개 추출

- 2026-03-23 14:55 KST | executor | completed | 4번 `21가지 교훈` 구조 점검 완료: EN 원서 기준 스캐폴드/메타데이터/TOC 정리, 8개 웹 단위 chapter-map v1 작성 및 source markdown 8개 추출 완료
- 2026-03-23 19:46 KST | executor | started | 4번 `21가지 교훈` digest/quiz 단계 시작: 8개 웹 단위 EN/KO 요약과 장당 퀴즈 생성
- 2026-03-23 19:52 KST | executor | completed | 4번 `21가지 교훈` digest/quiz 단계 완료: 8개 웹 단위 EN digest 8개, KO digest 8개, 퀴즈 8개 생성
- 2026-03-23 19:53 KST | executor | completed | 4번 `21가지 교훈` 책 사이트 및 library-site 로컬 빌드 완료

- 2026-03-23 15:18 KST | executor | completed | 4번 `21가지 교훈` digest/quiz 단계 완료: EN 원서 기준 8개 웹 단위에 대해 EN digest 8개, KO digest 8개, 퀴즈 8개 생성 후 책 사이트 및 library-site 로컬 빌드/자체검수 완료

- 2026-03-23 15:20 KST | executor | started | 5번 `피아트 스탠다드` 착수: EN 원서 기준 구조 점검 및 대형 파트 분할 설계 시작
- 2026-03-23 20:02 KST | executor | completed | 4번 `21가지 교훈` 최종 정리 완료: chapter-map/source/content/quiz/site를 8개 웹 단위로 통일, library-site 재빌드 완료
- 2026-03-23 20:03 KST | executor | started | 5번 `피아트 스탠다드` 착수: 원서 파일 점검 및 스캐폴드/메타데이터/TOC 추출 시작
- 2026-03-23 20:08 KST | executor | completed | 5번 `피아트 스탠다드` 구조 점검 완료: 15개 웹 단위 chapter-map v1 작성 및 source markdown 15개 추출
- 2026-03-23 20:10 KST | executor | started | 5번 `피아트 스탠다드` digest/quiz 단계 시작: 15개 웹 단위 EN/KO 요약과 장당 퀴즈 생성

- 2026-03-23 15:36 KST | executor | completed | 5번 `피아트 스탠다드` 구조 점검 완료: EN 원서 기준 스캐폴드/메타데이터/TOC 정리, 15개 웹 단위 chapter-map v1 작성 및 source markdown 15개 추출 완료
- 2026-03-23 20:18 KST | executor | completed | 5번 `피아트 스탠다드` digest/quiz 단계 완료: 15개 웹 단위 EN digest 15개, KO digest 15개, 퀴즈 15개 생성
- 2026-03-23 20:19 KST | executor | completed | 5번 `피아트 스탠다드` 책 사이트 및 library-site 로컬 빌드 완료
- 2026-03-23 20:21 KST | executor | started | 7번 `레이어드 머니` 착수: 원서 파일 점검 및 스캐폴드/메타데이터/TOC 추출 시작
- 2026-03-23 20:24 KST | executor | completed | 7번 `레이어드 머니` 스캐폴드/메타데이터/TOC 추출 완료
- 2026-03-23 20:26 KST | executor | completed | 7번 `레이어드 머니` 구조 점검 완료: 10개 웹 단위 chapter-map v1 작성 및 source markdown 10개 추출
- 2026-03-23 20:28 KST | executor | completed | 7번 `레이어드 머니` source 추출 정상화: src 경로 보정 후 10개 웹 단위 source markdown 생성 완료
- 2026-03-23 20:30 KST | executor | started | 7번 `레이어드 머니` digest/quiz 단계 시작: 10개 웹 단위 EN/KO 요약과 장당 퀴즈 생성

- 2026-03-23 16:05 KST | executor | completed | 5번 `피아트 스탠다드` digest/quiz 단계 완료: EN 원서 기준 15개 웹 단위에 대해 EN digest 15개, KO digest 15개, 퀴즈 15개 생성 후 chapter-map/file-name 정리와 로컬 빌드/자체검수 완료

- 2026-03-23 16:07 KST | executor | started | 7번 `레이어드 머니` 착수: EN 원서 기준 구조 점검 및 웹 단위 설계 시작
- 2026-03-23 20:36 KST | executor | completed | 7번 `레이어드 머니` digest/quiz 단계 완료: 10개 웹 단위 EN digest 10개, KO digest 10개, 퀴즈 10개 생성
- 2026-03-23 20:37 KST | executor | completed | 7번 `레이어드 머니` 책 사이트 및 library-site 로컬 빌드 완료
- 2026-03-23 20:40 KST | executor | started | 12번 `비트코인 핸드북` 착수: 원서 파일 점검 및 스캐폴드/메타데이터/TOC 추출 시작
- 2026-03-23 20:42 KST | executor | completed | 12번 `비트코인 핸드북` 스캐폴드/메타데이터/TOC 추출 완료
- 2026-03-23 20:45 KST | executor | completed | 12번 `비트코인 핸드북` 구조 점검 완료: 11개 웹 단위 chapter-map v1 작성 및 source markdown 11개 추출
- 2026-03-23 20:47 KST | executor | started | 12번 `비트코인 핸드북` digest/quiz 단계 시작: 11개 웹 단위 EN/KO 요약과 장당 퀴즈 생성
- 2026-03-23 20:53 KST | executor | completed | 12번 `비트코인 핸드북` digest/quiz 단계 완료: 11개 웹 단위 EN digest 11개, KO digest 11개, 퀴즈 11개 생성
- 2026-03-23 20:54 KST | executor | completed | 12번 `비트코인 핸드북` 책 사이트 및 library-site 로컬 빌드 완료
- 2026-03-23 20:56 KST | executor | started | 11번 `비트코인 블록사이즈 전쟁` 착수: 원서 파일 점검 및 스캐폴드/메타데이터/TOC 추출 시작

- 2026-03-23 16:42 KST | executor | completed | 7번 `레이어드 머니` digest/quiz 단계 완료: EN 원서 기준 10개 웹 단위에 대해 EN digest 10개, KO digest 10개, 퀴즈 10개 생성 후 파일 정리/로컬 빌드/자체검수 완료

- 2026-03-23 16:44 KST | executor | started | 8번 `비트코인 디플로마` 착수: KO 원본 기준 구조 점검 및 웹 단위 설계 시작
- 2026-03-23 20:58 KST | executor | completed | 11번 `비트코인 블록사이즈 전쟁` 스캐폴드/메타데이터/TOC 추출 완료
- 2026-03-23 21:00 KST | executor | completed | 11번 `비트코인 블록사이즈 전쟁` 구조 점검 완료: 12개 웹 단위 chapter-map v1 작성 및 source markdown 12개 추출
- 2026-03-23 21:02 KST | executor | started | 11번 `비트코인 블록사이즈 전쟁` digest/quiz 단계 시작: 12개 웹 단위 EN/KO 요약과 장당 퀴즈 생성

- 2026-03-23 17:05 KST | executor | completed | 8번 `비트코인 디플로마` 구조 점검 완료: KO 원본 기준 스캐폴드/메타데이터 보정/TOC 정리, 8개 웹 단위 chapter-map v1 작성 및 source markdown 8개 추출 완료
- 2026-03-23 21:08 KST | executor | completed | 11번 `비트코인 블록사이즈 전쟁` digest/quiz 단계 완료: 12개 웹 단위 EN digest 12개, KO digest 12개, 퀴즈 12개 생성
- 2026-03-23 21:09 KST | executor | completed | 11번 `비트코인 블록사이즈 전쟁` 책 사이트 및 library-site 로컬 빌드 완료
- 2026-03-23 21:11 KST | executor | started | 9번 `비트코인 백서 해설` 착수: KO 원본 파일 점검 및 스캐폴드/메타데이터/TOC 추출 시작
- 2026-03-23 21:14 KST | executor | completed | 9번 `비트코인 백서 해설` 스캐폴드/메타데이터/TOC 추출 완료

- 2026-03-23 17:28 KST | executor | completed | 8번 `비트코인 디플로마` digest/quiz 단계 완료: KO 원본 기준 8개 웹 단위에 대해 EN digest 8개, KO digest 8개, 퀴즈 8개 생성 후 책 사이트 및 library-site 로컬 빌드/자체검수 완료

- 2026-03-23 17:30 KST | executor | started | 9번 `비트코인 백서 해설` 착수: KO 원본 기준 spine/실제 본문 구조 분석 및 재분할 설계 시작
- 2026-03-23 21:18 KST | executor | completed | 9번 `비트코인 백서 해설` 구조 점검 완료: 단일 XHTML을 10개 웹 단위로 수동 분할한 chapter-map/source markdown 생성
- 2026-03-23 21:20 KST | executor | completed | 9번 `비트코인 백서 해설` source 분할 보정: section marker 기반 10개 웹 단위 source markdown 재생성
- 2026-03-23 21:22 KST | executor | started | 9번 `비트코인 백서 해설` digest/quiz 단계 시작: 10개 웹 단위 EN/KO 요약과 장당 퀴즈 생성
- 2026-03-23 21:28 KST | executor | completed | 9번 `비트코인 백서 해설` digest/quiz 단계 완료: 10개 웹 단위 EN digest 10개, KO digest 10개, 퀴즈 10개 생성
- 2026-03-23 21:29 KST | executor | completed | 9번 `비트코인 백서 해설` 책 사이트 및 library-site 로컬 빌드 완료
- 2026-03-23 21:31 KST | executor | started | 8번 `비트코인 디플로마` 착수: KO 원본 파일 점검 및 스캐폴드/메타데이터/TOC 추출 시작
- 2026-03-23 21:33 KST | executor | started | 10번 `비트코인 사용 가이드(PDF)` 착수: PDF 기반 구조/분할 상태 점검 시작
- 2026-03-23 21:37 KST | executor | completed | 10번 `비트코인 사용 가이드(PDF)` 스캐폴드 초기화: 29개 웹 단위 provisional chapter-map과 메타데이터/분할 규칙 초안 생성
- 2026-03-23 21:40 KST | executor | started | 10번 `비트코인 사용 가이드(PDF)` 실제 추출 단계 시작: PDF 텍스트/목차 구조를 파악해 29개 웹 단위 source를 생성
- 2026-03-23 21:45 KST | executor | completed | 10번 `비트코인 사용 가이드(PDF)` source 생성: page-range 기반 29개 웹 단위 source markdown 생성 완료

- 2026-03-23 17:55 KST | executor | completed | 9번 `비트코인 백서 해설` digest/quiz 단계 완료: KO 원본 기준 10개 웹 단위에 대해 EN digest 10개, KO digest 10개, 퀴즈 10개 생성 후 파일 정리/로컬 빌드/자체검수 완료

- 2026-03-23 17:57 KST | executor | started | 10번 `비트코인 사용 가이드` 착수: KO PDF 원본 기준 파트/세부 단위 분할과 로컬용 처리 계획 수립 시작
- 2026-03-23 21:52 KST | executor | completed | 10번 `비트코인 사용 가이드(PDF)` digest/quiz 단계 완료: 29개 웹 단위 EN/KO 요약 초안과 퀴즈 생성
- 2026-03-23 21:53 KST | executor | completed | 10번 `비트코인 사용 가이드(PDF)` 책 사이트 및 library-site 로컬 빌드 완료
- 2026-03-23 21:56 KST | executor | completed | 비트코인 필수 12권 로컬 자체검수 완료: 12권 모두 source/content/quiz/site 산출물 존재, curated library-site 로컬 빌드 기준 12권 published 확인
- 2026-03-23 21:58 KST | executor | completed | `레이어드 머니` source 정합성 보정: chapter-map 기준 10개 source markdown 재추출 완료
- 2026-03-23 22:00 KST | executor | completed | 비트코인 필수 12권 최종 재검증: 12권 모두 source/content/quiz/site 개수 일치, library-site ready 카드 12개 확인

- 2026-03-23 22:05 KST | executor | completed | 단독 책 사이트 템플릿 정합성 보정: build_book_site를 책장 UI와 맞춰 KO 기본 탭/한국어 제목/이전다음 네비게이션 지원으로 수정
- 2026-03-23 22:07 KST | executor | completed | 비트코인 필수 12권 단독 사이트 전권 재빌드 및 library-site 로컬 재빌드 완료
- 2026-03-23 22:09 KST | executor | completed | 최종 검증: 샘플 3권 기준 단독 챕터 페이지에서 한국어 탭 기본 활성/퀴즈 한국어 기본 활성/이전다음 네비 존재 확인
- 2026-03-23 22:08 KST | executor | completed | 템플릿/네비게이션 반영 후 12권 책 사이트 + library-site 전체 재빌드 완료
- 2026-03-23 22:14 KST | executor | completed | 단독 책 사이트 다크 테마 보정 완료: chapter template에 library-reading-page body class/title 치환을 적용하고 전권 재빌드 후 KO 기본 탭/이전다음 네비를 재검증
- 2026-03-23 22:16 KST | executor | completed | Ralph 로컬 실행 종료: 비트코인 필수 12권 전권 산출물 수량 일치 및 KO 기본 읽기 UI 검증까지 완료, 이후 대기 상태 전환
