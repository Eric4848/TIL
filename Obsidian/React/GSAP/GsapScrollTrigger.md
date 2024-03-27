> page의 scroll 위치에 의해 변경시킬 때 사용

## 1. 문법
- scrollTrigger 사용을 위해 추가
```jsx
import gsap from "gsap";
import { ScrollTrigger } from "gsap/all";
  
gsap.registerPlugin(ScrollTrigger);
```

```jsx
const scrollRef = useRef();   // ref설정
  useGSAP(() => {
    const boxes = gsap.utils.toArray(scrollRef.current.children);   // elements를 배열로 묶는다
  
    boxes.forEach((box) => {
      gsap.to(box, {
        x: 150,
        rotation: 360,
        borderRadius: "100%",
        scale: 2,
        scrollTrigger: {   // Trigger 설정
          trigger: box,   // 대상
          start: "bottom, bottom",   // 시작 지점
          end: "top 20%",   // 종료 지점
          scrub: true,   // 부드럽게 동작하도록 가가
        },
        ease: "power1.inOut",
      });
    });
  }, []);
```