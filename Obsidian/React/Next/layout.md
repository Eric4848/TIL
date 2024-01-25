> 페이지를 감싸는 부분 - 공통적으로 유지되는 부분에 사용

## 1. layout 생성
- 공통으로 사용할 폴더에 layout이름으로 생성
- export default
- property에 children을 반드시 추가해야 한다
```tsx
const AuthLayout = ({children}:{children: React.ReactNode}) => {
  return (
    <div>
      {children}
    </div>
  )
}

export default AuthLayout
```