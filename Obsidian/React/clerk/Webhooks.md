## 1. 개념
> 즉각적인 정보전달 -> 데이터 변경을 실시간으로 전달
### 1. ngrok에서 URL 연결
### 2. 연결된 URL을 Clerk홈페이지의 Webhooks에 등록
- 등록 시 주소 + /api/webhooks/clerk추가
### 3. Message Filtering에서 user모두 체크
### 4. create
### 5. .env파일에 Signing Secret 등록
```
CLERK_WEBHOOK_SECRET=<Signing Secret>
```
### 6. middleware.ts에 추가
```ts
export default authMiddleware({
  publicRoutes: ["/api/webhooks(.*)"],
});
```