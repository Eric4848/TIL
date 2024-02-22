> 화면에 메세지를 띄워줌

## 1. Install
```cmd
npm i sonner
```

## 2. 문법
### 1. 위치 선정
``` tsx
import { Toaster } from 'sonner'

<Toaster />   // 메세지를 띄울 위치 설정
```

### 2. 메세지 조건설정
```tsx
someFunction()
  .then(() => toast.success("message for succes"))
  .catch(() => toast.error("message for failed"))
```