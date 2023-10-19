- 헤더파일 = 클래스 선언, 변수와 함수의 원형 
- 소스파일 = 함수의 내용 저
## 1. 클래스 생성
- Tools > New C++ class
- 클래스 생성 시 상속받을 클래스 선택, 다양한 부모 클래스들이 있다
- Content Browser에 C++ Classes에서 확인할 수 있다
- 클래스 생성 시 헤더파일(.h)과 소스파일(.cpp)가 생성된다
## 2. 함수
1. 클래스 이름의 함수 - 객체가 생성될 때 실행, 주로 액터의 기본값을 설정
2. BeginPlay - 배치된 월드에서 게임 시작, 스폰되었을 때 호출, 게임 플레이 로직 초기화
3. Tick - 프레임마다 호출, 매개변수 DeltaTime을 이용해 함수 호출간 시간 계산, 주로 게임의 로직 계산, 함수 제거로 성능 향상 가능
	*함수 제거를 위해 함수들을 제거하고 소스파일에서 "PrimaryActorTick.bCanEverTick = True(매초마다 Tick함수 호출하는 코드);"를 제거한다*
## 3. 컴파일
- cmd에서 LiveCoding.Compile 입력
- Ctrl + Alt + F11
- Unreal Editor 종료 > VS 상단 Build > Rebuild Solution > 다시 시작
