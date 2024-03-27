> element를 현재 상태에서 새로운 상태로 변경시킬때 사용

## 1. 문법
```jsx
gsap.to("#blue-box", {   // 대상 지정
      x: 250,   // 도착 위치
      // y: 500,
      repeat: -1,   // 반복 횟수
      yoyo: true,   // 반대방향으로 실행 여부
      rotation: 360,   // 회전
      duration: 5,   // 소요 시간
      ease: "elastic",   // 효과
    }
```