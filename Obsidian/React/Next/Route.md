
> Next에선 Route를 폴더명을 통해 자동으로 해준다

## 1. app 폴더가 Home의 역할
- 사용 불가
	- components 
## 2. 폴더 안의 page가 구현될 페이지
- 반드시 폴더의 페이지 이름을 page로 생성해야한
## 3. 반드시 export default를 해야한다
## 4. 다른 기능을 사용하기 위해 export function ? 를 사용
- get
```ts
export function GET() {
	return Response.json({test:"GET"})
}
```
## 5. Route 숨기기
> 공통으로 사용되는 url (/common/~~ 에서 /common) 상위 폴더명 없이 동작하게 하는 방법

- 공통으로 Route한 폴더명을 ()로 감싸준다
	- ex) (common)

## 6. Route 연결 제외
> Route에 연결되지 않도록 하는 방법

- 폴더명 앞에 `_` 를 붙여준다
