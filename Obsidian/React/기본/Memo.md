> Memorize기능 => property가 바뀌지 않는 경우 render하지 않도록 설정

## 1. 사용
- property가 변경되지 않은 component의 re-render를 막는다
	- component가 매우 많아지면 성능 저하의 원인이 될 수 있기 때문

## 2. 문법
```js
function Btn({prop});
const MemorizedBtn = React.memo(Btn);
```