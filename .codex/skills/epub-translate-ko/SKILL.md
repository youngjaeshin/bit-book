---
name: epub-translate-ko
description: Use when converting an English EPUB in this repo into a Korean EPUB for private/internal use. The workflow should preserve the original EPUB structure as much as possible, translate chapter XHTML content into Korean, apply Austrian-economics and Bitcoiner terminology consistently, and rebuild a readable .ko.epub with working TOC, links, and basic styling.
---

# EPUB Translate KO

이 스킬은 이 저장소에서 **영어 EPUB을 한국어 EPUB으로 변환**할 때 사용한다.

목표는 단순 번역문 추출이 아니라:

- 원본 EPUB 구조를 최대한 유지하고
- 챕터별 XHTML 본문을 한국어로 바꾸고
- 목차/링크/스타일이 살아 있는
- **내부 개인용 `.ko.epub` 파일**을 만드는 것이다.

## Scope

- **개인/내부 보관용 EPUB 번역본** 생성
- 공개 배포용 번역 출판 workflow는 아님
- 번역은 기존 repo-local 스킬과 함께 사용한다.
  - `bitcoin-translation-style`
  - `book-reading-summary-style` (요약이 아니라 스타일 참고가 필요할 때만)

## Core principle

새 EPUB을 처음부터 다시 쓰기보다,
**원본 EPUB의 골격을 재사용하고 텍스트만 안전하게 교체**하는 방식을 기본 전략으로 삼는다.

즉:

1. 원본 EPUB unzip
2. OPF/nav/ncx/stylesheet 구조 보존
3. chapter XHTML별로 번역문 반영
4. metadata/manifest/spine/toc 유효성 유지
5. `.ko.epub`로 재패키징

## Translation policy

한국어 번역은 다음 원칙을 따른다.

- 오스트리안 경제학 용어 유지
- 비트코이너 친화적 표현 유지
- 저자 논지의 방향을 약화시키지 않기
- 필요할 때 첫 등장에 영어 원어 병기

용어는 반드시 아래 스킬/레퍼런스를 우선 참조한다.

- `../bitcoin-translation-style/SKILL.md`
- `../bitcoin-translation-style/references/glossary-ko.md`

## Recommended workflow

### Phase 1. Intake

1. 원본 EPUB 경로 확인
2. `source/metadata.json`, `toc.json`, `chapter-map.json` 존재 여부 확인
3. 번역 단위를 chapter-level로 확정
4. 출력 경로 결정
   - 예: `books/<slug>/translated_epub/`

### Phase 2. Unpack + map

1. EPUB unzip
2. `META-INF/container.xml` 확인
3. `content.opf`, nav, ncx, stylesheet 위치 확인
4. chapter-map 기준으로 어떤 XHTML을 번역할지 결정

### Phase 3. Translate XHTML content

1. XHTML에서 본문 노드만 추출
2. 제목, 문단, 리스트, 인용문 단위로 번역
3. 각주 링크, anchor id, href는 유지
4. 이미지/캡션/figure 구조는 최대한 유지
5. 번역 결과를 XHTML에 다시 삽입

### Phase 4. Reassemble

1. 수정된 XHTML 저장
2. nav/ncx 제목도 필요 시 한국어화
3. manifest/spine 유효성 점검
4. `mimetype` 첫 항목 무압축 규칙 유지
5. `.ko.epub`로 zip 패키징

### Phase 5. Verify

최소한 아래를 확인한다.

- EPUB 파일이 열리는가
- 목차가 동작하는가
- chapter 이동이 되는가
- 한글이 깨지지 않는가
- 링크/각주/이미지가 크게 깨지지 않는가

## Reassembly quality bar

좋은 결과물은 아래를 만족해야 한다.

1. **TOC integrity**
   - nav/ncx 링크 정상
   - 장 이동 정상

2. **Structure integrity**
   - 제목/소제목 계층 유지
   - 문단 흐름 유지
   - chapter 순서 유지

3. **Text integrity**
   - 한글 인코딩 문제 없음
   - 번역 누락 최소화
   - anchor/link 깨짐 최소화

4. **Reading integrity**
   - EPUB 리더에서 자연스럽게 읽힘
   - 스타일이 완전히 붕괴하지 않음

## Output conventions

권장 출력:

- `books/<slug>/translated_epub/work/` — 중간 unpack 작업 디렉토리
- `books/<slug>/translated_epub/xhtml/` — 번역된 XHTML 샘플/보관
- `books/<slug>/translated_epub/<slug>.ko.epub` — 최종 산출물

## Suggested future scripts

이 스킬은 설계 단계이며, 실제 구현은 보통 아래 스크립트로 이어진다.

- `scripts/unpack_epub.py`
- `scripts/translate_epub_xhtml.py`
- `scripts/repack_epub.py`
- `scripts/validate_epub.py`

## Reference

- `references/pipeline.md` — 세부 파이프라인 설계
- `references/reassembly-quality.md` — 재조립 품질 체크리스트
