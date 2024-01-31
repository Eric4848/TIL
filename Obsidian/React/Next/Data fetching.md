## 1. 차이
### 1. React
1. React app
2. API
3. API's DataBase

### 2. Next.js
1. Next app
2. API's DataBase

## 2.  사용
```tsx
const URL = "URL to fetch"
  
async function getData() {
  const response = await fetch(URL)
  const json = await response.json();
  return json;
}
  
export default async function Main() {
  const data = await getData()
  return (
    <div>
      <div>{JSON.stringify(data)}</div>
    </div>
  );
}
```

## 특징
- server단에서 fetch
- 한번 받아오면 다시 받지 않는다
- 받아질 때 까지 페이지가 나오지 않는다
	- loading을 사용하여 우선 구현 가능