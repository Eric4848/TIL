> element를 새로운 상태에서 현재 상태로 돌아오도록 하데 사용

## 1. 문법
```jsx
gsap.from("#green-box", {   // 대상 지정
      x: 250,   // 시작 위치
      // y: 500,
      repeat: -1,   // 반복 횟수
      yoyo: true,   // 반대방향으로 실행 여부
      rotation: 360,   // 회전
      duration: 5,   // 소요 시간
      ease: "power1.inOut",   // 효과
    }
```