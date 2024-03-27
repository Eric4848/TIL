> element를 지정한 상태1에서 지정한 상태2로 변경시킬때 사용

## 1. 문법
```jsx
useGSAP(() => {
    gsap.fromTo(
      "#red-box",   // 대상 지정
      {   // from 
        x: 0,   // 위치
        rotation: 0,   // 회전
        borderRadius: "0%",   // 모서리 각도
      },
      {   // to
        x: 250,   // 위치
        repeat: -1,   // 반복 횟수
        yoyo: true,   // 반대방향으로 실행 여부
        borderRadius: "100%",   // 모서리 각도
        rotation: 360,   // 회전
        duration: 5,   // 소요 시간
        ease: "bounce.out",   // 효
      }
    );
  }, []);
```