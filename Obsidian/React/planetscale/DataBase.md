## 1. 사용
### 1. sign-up
### 2. create-database
### 3. select framework(Prisma)
### 4. save Username and PW
### 5. install prisma
```cmd
npm i -D prisma
```

```cmd
npm i @prisma/client
```

### 6. setup
```cmd
npx prisma init
```
### 7. set DATABASE_URL
```
%% .env %%
DATABASE_URL = {생성한 DB의 URL}로 변경
```
### 8. prisma/schema.prisma파일 수정
```prisma
datasource db {
  provider     = "mysql"
  url          = env("DATABASE_URL")
  relationMode = "prisma"
}

generator client {
  provider = "prisma-client-js"
}

```
### 9. db push
```cmd
npx prisma db push
```