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

> 크기의 html 크기의 변화를 관찰하여

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
