# Java Script

## 다른 태그의 height 가져오기

> 다른 태그의 요소들을 가져와서 원하는 요소에 추가해준다

```javascript
function div2Resize() {
  var ul1 = document.getElementById("ul1");
  var div2 = document.getElementById("content");
  div2.style.height = ul1.clientHeight + "px";
  console.log(ul1.clientHeight);
}
window.onload = function () {
  div2Resize();

  // 브라우저 크기가 변할 시 동적으로 사이즈를 조절해야 하는경우
  window.addEventListener("resize", div2Resize);
};
```

## 크기변화 관찰하기

> 크기의 html 크기의 변화를 관찰하여 동작시킨다

```javascript
function resize() {
  const $target = document.querySelector("#ul1");
  const observer = new ResizeObserver((entries) => {
    entries.forEach((entry) => {
      var ul1 = document.getElementById("ul1");
      var div2 = document.getElementById("content");
      div2.style.height = ul1.scrollHeight + 32 + "px";
    });
  });

  observer.observe($target);
}
```

## 슬라이드 기능(slick)

> 상하, 좌우 슬라이드 기능을 slick을 활용하여 구현할 수 있다
```HTML
CSS
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>
JS
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>

```

```javascript
$(function(){
    $('.slider-wrap').slick({
      slide: 'div',        //슬라이드될 태그
      infinite : true,     //무한 반복 옵션     
      slidesToShow : 2,        // 한 화면에 보여질 컨텐츠 개수
      slidesToScroll : 1,        //스크롤 한번에 움직일 컨텐츠 개수
      speed : 500,     // 다음 버튼 누르고 다음 화면 뜨는데까지 걸리는 시간(ms)
      arrows : true,         // 옆으로 이동하는 화살표 표시 여부
      dots : true,         // 스크롤바 아래 점으로 페이지네이션 여부
      autoplay : true,            // 자동 스크롤 사용 여부
      autoplaySpeed : 2000,         // 자동 스크롤 시 다음으로 넘어가는데 걸리는 시간 (ms)
      pauseOnHover : true,        // 슬라이드 이동   시 마우스 호버하면 슬라이더 정지
      vertical : false,        // 세로 방향 슬라이드 옵션
      prevArrow : "<button type='button' class='slick-prev'>Previous</button>",
      nextArrow : "<button type='button' class='slick-next'>Next</button>",
      draggable : true,     //드래그 가능 여부 
      responsive: [ // 반응형 웹 구현
        {  
          breakpoint: 960, //화면 사이즈
          settings: {
            slidesToShow: 4
          } 
        },
        { 
          breakpoint: 768, //화면 사이즈
          settings: {    
            slidesToShow: 5
          } 
        }
      ]

    });
})
```