> 이론용으로 일반적으로 사용되지 않는다
## 1. 사용
- React에선 HTML을 직접 작성하지 않으므로 tag들을 따로 생성해야한다.
## 2. 문법
```javascript
const root = document.getElementById("root");   // body의 위치를 찾아줄 태
const name = React.createElement("span");   // 이름으로 인자로 준 tag를 생성해 저장한다
										   // 인자로는 (tag, property, content)
ReactDOM.render(name, root)   // Element를 HTML에 만들어주는 함수 (Element, 위치)
```