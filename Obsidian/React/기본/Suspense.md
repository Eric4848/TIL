> await중 다른 것들은 먼저 render될 수 있게 한다

## 1. 문법
```tsx
      <Suspense fallback={<h1>Loading movie info</h1>}>
        <MovieInfo id = {id} />
      </Suspense>
```
- fallback -> await중 띄워줄 부분
- Loading에 영향을 주지 않는