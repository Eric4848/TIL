>  하나로 묶은 element들을 일정 지연으로 변경시킬 때 사용

## 1. 문법
```jsx
  useGSAP(() => {
    gsap.to(".stagger-box", {
      y: 250,
      rotation: 360,
      borderRadius: "100$",
      repeat: -1,
      yoyo: true,
      duration: 3,
      // stagger: 0.5,   왼쪽부터 시간 차로 진행
      stagger: {
        amount: 1.5,   // 시간차
        grid: [2, 1],   // grid대사이면 설정하여 그에 따라 동작
        axis: "y",   // grid를 그린 경우 우선순위
        ease: "circ.inOut",
        from: "center",   // 시작 치
      },
    });
  });
```