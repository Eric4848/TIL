# CSS
1. 선택자 : 네이버에서 수많은 div태그를 사용중인데 이중 특정한 태그를 찾아쓴다
2. 스타일(꾸미는 것) : 색상이나 모양 등을 지정한다 -> w3school.com에서 확인 가능

## 스타일과 스타일 시트

### 브라우저 기본 스타일
- 브라우저에서 기본으로 적용하는 스타일
- 웹 문서에서 아무 스타일도 적용하지 않고 HTML만 사용해도 그 기능에 따라 크기에 맞게 보여줌

### 인라인 스타일  
- 스타일 시트를 사용하지 않고 스타일을 적용할 대상에 직접 표시
- 스타일을 적용하고 싶은 태그에 style 속성을 사용해 style=“속성: 속성 값;” 형태로 스타일 적용

### 내부 스타일 시트
- 웹 문서 안에서 사용할 스타일을 문서 안에 정리한 것
- 모든 스타일 정보는 `<head>` 태그와 `</head>` 태그 안에서 정의
- `<style>` 태그와 `</style>` 태그 사이에 작성

### 외부 스타일 시트
- 여러 웹 문서에서 사용할 스타일을 별도 파일로 저장해 놓고 필요할때마다 파일에서 가져와 사용
- `<style>` 태그 없이 `<link>` 태그만 사용해 미리 만들어 놓은 외부 스타일 시트 파일 연결

## 스타일 형식

### 전체 선택자
- 페이지에 있는 모든 요소를 대상으로 스타일을 적용할 때 사용
- 별표(*)로 지정
- 웹 브라우저의 기본 스타일을 초기화할 때 자주 사용

### 태그 선택자 
- 특정 태그를 사용한 모든 요소에 스타일이 적용됨

### 클래스 선택자
- 요소의 특정 부분에만 스타일 적용됨
- 마침표(.) 다음에 클래스 이름 지정
- 문서 안에서 여러 번 반복할 스타일이라면 클래스 선택자로 정의

### 아이디 선택자  
- 요소의 특정 부분에만 스타일 적용
- 파운드(#) 다음에 id 이름 지정
- 문서 안에서 한번만 사용한다면 id 선택자로 정의

### 자식 선택자
- 한 칸 밑의 자식 요소에만 스타일 적용
- 꺽새표(>) 다음에 이름 지정

### 하위(자손) 선택자
- 밑의 모든 하위 요소에 스타일 적용
- 공백( )으로 이름 지정

### 형제 선택자
- 형제 요소들에 스타일 적용
- 물결표 (~)로 이름 지정

### 인접 형제 선택자 
- 같은 부모를 가진 형제 요소 중 첫 번째 형제 요소에만 스타일 적용
- 더하기 (+)로 이름 지정

### 속성 선택자 (attribute selector)
- HTML 태그를 작성할 때 여러 가지 속성을 함께 사용함
- 그 속성값에 따라 원하는 요소를 선택할 수 있음