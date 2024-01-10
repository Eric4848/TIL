> 부모 레벨의 데이터를 자식 레벨로 보내는 방법 (상속과 유사)

## 1. 형태
function Props(props) {}

## 2. 사용
- 반복되어 사용되는 Component의 경우 상속할 원본을 만들어 그 안에 properties를 넘겨 사용
- 인자의 object로 입력되는 데이터를 해당 함수 내에서 사용
- 중괄호를 사용하여 풀면 바로 사용 가능
	- function Props({property}){} => {property}로 바로 사용 가능

## 3. [[Memo]](Memorize)
- 인자가 바뀌지 않는 경우 render하지 않도록 한다