# scripts/

재사용 가능한 추출/변환/빌드 스크립트를 둔다.

권장 스크립트 후보:

- `extract_epub.py` — EPUB 메타데이터/목차/본문 추출
- `extract_pdf.py` — PDF 텍스트 추출 (후순위)
- `build_site.py` — content/quiz 데이터를 HTML로 렌더링

원칙:

- 한 권 전용 임시 스크립트보다 재사용 가능한 입력/출력 인터페이스를 우선한다.
- 출력 경로는 되도록 `books/<slug>/...` 아래로 통일한다.
