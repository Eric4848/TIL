### 1. ngrok.com/download 에서 설치
### 2. ngrok config add-authtoken [token]로 계정과 연결
### 3. sidebar의 Domains에서 Domain 생성
### 4. 생성된 Domain주소로 local host를 이어준다

## 사용자 관리
### 1. user-create
```ts
const eventType = evt.type;
  
  if (eventType === "user.created") {
    await db.user.create({
      data: {
        externalUserId: payload.data.id,
        username: payload.data.username,
        imageUrl: payload.data.image_url,
      },
    });
  }
```
### 2. user-update
```ts
const eventType = evt.type;

  if (eventType === "user.updated") {
    const currentUser = await db.user.findUnique({
      where: {
        externalUserId: payload.data.id,
      },
    });
  
    if (!currentUser) {
      return new Response("User not fount", { status: 404 });
    }
  
    await db.user.update({
      where: {
        externalUserId: payload.data.id,
      },
      data: {
        username: payload.data.username,
        imageUrl: payload.data.image_url,
      },
    });
  }
```
### 3. user-delete
```ts
const eventType = evt.type;

  if (eventType === "user.deleted") {
    await db.user.delete({
      where: {
        externalUserId: payload.data.id,
      },
    });
  }
```