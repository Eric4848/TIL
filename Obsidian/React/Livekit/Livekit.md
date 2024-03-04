> 무료 실시간 영상, 음성 공유API

## 1. Generate
1. livekit.io 접속
2. sign-in
3. create-project
4. Settings-key에서 Key 설정
```.env
LIVEKIT_API_URL=[Analytics 상단의 주소]
LIVEKIT_API_KEY=[Settings-key의 KEY]
LIVEKIT_API_SECRET=[Settings-key의 Secrety-KEY]
NEXT_PUBLIC_LIVEKIT_WS_URL=[Settings-key의 WEBHOOK]
```

## 2. install
```cmd
npm i @livekit/components-react
npm i livekit-client
npm i livekit-server-sdk
```