

## 1. react-router-dom 설치
> npm install react-router-dom

## 2. 문법

```js
{ BrowserRouter as Router, HashRouter, Routes, Route } from "react-router-dom"

function Main() {
  return (
    <Router>
      <Routes>
        <Route
          path='/'
          element={<Home />}
        ></Route>
        <Route
          path='/movie'
          element={<Detail />}
        />
      </Routes>
    </Router>
  );
}
```
### 1. BrowserRouter
> /로 이어지는 위치로 이동시켜준다

### 2. HashRouter
> /#/로 이어지는  위치로 이동시켜준다

### 3. Routes
> 이동 시킬 Routes들을 담는다

### 4. Route
> 위치의 이름과 실행할 element를 설정한다

### 5. useParams
> url로 받은 parameter의 이름과 값을 받아온다