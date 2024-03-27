> elements의 상태를 여러 번 변경시킬 때 사용

## 1. 문법
```jsx
// timeline 정의
const timeline = gsap.timeline({
    repeat: -1,   // 반복 횟수
    repeatDelay: 1,   // 다음 행동 사이의 시간
    yoyo: true,   // 반대로 돌아오기
  });

  useGSAP(() => {
	// 첫번째 행동
    timeline.to("#yellow-box", {
      x: 250,
      rotation: 360,
      borderRadius: "100%",
      duration: 2,
      ease: "back.inOut",
    });
    
    // 두번쨰 행동
    timeline.to("#yellow-box", {
      y: 250,
      scale: 2,   // 크기 비율
      rotation: 360,
      borderRadius: "28px",
      duration: 2,
      ease: "back.inOut",
    });

	// 세번째 행동
    timeline.to("#yellow-box", {
      x: 500,
      scale: 1,
      rotation: 360,
      borderRadius: "8px",
      duration: 2,
      ease: "back.inOut",
    });
  }, []);
`````

```jsx
timeline.paused()  // timeline이 정지 상태인지 확인

timeline.play()   // 정지상태를 실행상태로 변경

timeline.pause()   // 실행상태를 정지상태로 변
```