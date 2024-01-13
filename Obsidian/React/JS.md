## 1. 리스트에 이름 부여하기
> 리스트의 위치를 인덱스로 부를 수도 있지만 이름을 지정할 수도 있다

1. 문법
```js
const food = ["Pizza", "Hamburger"]
const [myFavFood, mySecondFavFood] = food
```
 ==
```js
const food = ["Pizza", "Hamburger"]
const myFavFood = food[0]
const mySecoundFavFood = food[1]
```
## 2. HTML에서 JS 사용하기
> HTML에서 JS를 바로 작성하는 방법

1. 문법
```html
<div>
  How to use JS in HTML   // 문자가 그대로 출력된다
  {write JavaScript}   // html에서 중괄호를 사용하면 JS를 바로 사용할 수 있다
</div>
```

### 3. Array의 값 가져오기
> Array의 값들을 그대로 이어갈 때 사용

1. 문법
```js
// array에서 6을 추가해 새로운 array를 만들 때
const array = [1, 2, 3, 4, 5]
const newArray = [...array, 6]   // ...을 사용하면 그 안의 값들을 그대로 가져온
```

## 4. fetch
> api(데이터) 가져오기

1. 문법
```js
fetch("urls_want_to_use")
```