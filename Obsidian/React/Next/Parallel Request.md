> 여러 데이터를 fetch할 시 기본적으로 하나씩 하는데 동시에 하는 방법

## 1. Promise
### 1. 문법
```tsx
const [movie, video] = await Promise.all([getMovie(id), getVideo(id)])
```

### 2. 특징
- 안의 모든 함수가 완료되기 전까지 미리 완료된 것 사용 X
