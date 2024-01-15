> github에서 제공하는 무료 배포기능

## 1. 문법
```
gh-pages -d "forder-name"   %% 폴더에 있는 구현한 웹페이지를 배포한다 %%
"homepage": "https://"UserName".github.io/"RepoName"
```

1. npm의 경우
 - package.json파일에서
```
{
  "name": "first-react-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "gh-pages": "^6.1.1",
    "prop-types": "^15.8.1",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.2",
    "react-scripts": "^5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "deploy": "gh-pages -d build",   %% 배포하는 명령어 %%
    "predeploy": "npm run build"   %% deploy실행 시 먼저 실행 %%
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "homepage": "https://Eric4848.github.io/TIL"   %% gh-pages로 만들 주 %%
}
```