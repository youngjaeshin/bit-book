# source/

이 디렉토리에는 원본 EPUB에서 직접 추출한 자료를 둔다.

예상 파일 예시:

- `metadata.json`
- `toc.json`
- `chapter-map.json`
- `excluded-sections.json`
- `chapters/01-introduction.md`
- `chapters/02-opening-scene.md`

원칙:

- 원문 추출 단계의 결과를 보존한다.
- 후속 요약/퀴즈 생성은 이 디렉토리의 결과를 기준으로 한다.
- cover, dedication, foreword 같은 제외 대상은 별도 목록으로 남긴다.
- 실제 챕터 파일은 가능하면 저자 목차 기준으로 맞춘다.
