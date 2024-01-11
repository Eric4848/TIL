> re-render되지 않도록 하는 방법(API를 불러오는 경우 render마다 반복되는 것은 좋지 않다)

## 1. 형태
useEffect(function, deps)

## 2. 문법
```js
const func_name = () => {
  // function you want to use
}
useEffect(func_name, array)

// or

  useEffect(() => {
    // function you want to use
  }, [])
```

## 3. Deps
- render를 일으킬 요소 설정
```js
useEffect(() => {
	// function you want to use
}, [triggers-to-make-render])
```
- 비우면 첫 render만 진행된다