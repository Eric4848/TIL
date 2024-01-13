> 데이터가 저장되는 곳

# 1. 형태
### React.useState(인자);
- [변수, 함수]의 형태로 저장된다
- 인자: 변수의 초기 값

## 2. 기능
- 함수를 사용하면 변수 update하고 render를 진행해준다
	- render를 직접 하지 않아도 된다

## 3. value
- input을 입력받는 경우 인자의 target의 value로 접근할 수 있다
```js
const func = (typed) => {
	console.log(typed.target.value)   // input value에 접근
}
```
## 4. funcion
- 생성한 변수를 조작하는 함수를 작성할 수 있다
- 변수를 직접 변경하는 것 보다 현재 상태를 변경하는 것이 좋다
```js
funcName((current) => (current * something))   // 변수가 다른 곳에서 변한 것도 반영
```

## 5. array
