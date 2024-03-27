> text를 대상으로 to, from, fromto, timeline을 사용

## 1. 문법
```jsx
useGSAP(() => {
    gsap.to("#text", {   // text를 담은 tag 대상
      ease: "power1.inOut",
      opacity: 1,   // 투명도
      y: 0,
    });
  
    gsap.fromTo(
      ".para",
      {
        opacity: 0,
        y: 20,
      },
      {
        opacity: 1,
        y: 0,
        delay: 0.5,
        stagger: 0.1,
      }
    );
  }, []);
```