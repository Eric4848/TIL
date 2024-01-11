## 1. style.css
> css파일을 만들어 사용

1. src에 style.css 파일을 생성
2. css파일에서 style 설정
3. App.js에서 import "./style.css"를 작성해 입력

## 2. style prop
> property로 style 작성

## 3. Style.module.css
> object로 만들어 일부에만 적용

1. src에 style.module.css파일 생성
2. css파일에 .name_i_set으로 style 설정
3. 적용할 component에 해당 style.module.css를 styleName으로 import
4. 적용할 component에 className={styleName.name_i_set}