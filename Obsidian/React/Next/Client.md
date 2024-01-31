## 1. use client(client side render)
> 사용시 page의 일부분만 변경하는 기능도 사용 가능 - useState, useEffect, onClick, frontend behavior
```tsx
"use client"
const ~ = () => {

}
```
- metadata 사용 불가능
## 2. server side render
> page 변경 불가(default)
- Next.js의 default
- JScode를 다운로드 하지 않아 더 빠르다
- client side로 가지 않기 때문에 보안에 좋다