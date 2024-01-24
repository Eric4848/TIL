> HTML과 비슷한 형태로 React를 작성할 수 있도록 돕는다
# 1. 사용
> 사용하기 위해 JSX를 변환해줄 Babel을 사용해야 한다

- 헤더에 추가 할 내용
```javascript
<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
<script type="text/babel">
  // 내용
</script>
```
## 2. HTML과 다르게 써야 할 점
1. label의 for을 htmlFor로 사용해야 한다
```js
<label htmlFor="targetId">Label<label/>
```
2. class를 className으로 사용해야 한다
```js
<h1 className="class">Class<h1/>
```
3.  return할 때 하나의 tag만 사용해야 한다
```js
function Main() {
	return(
		<div>
			<tag></tag>
			<tag></tag>
		</div>
	)
}
```
