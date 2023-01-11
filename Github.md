# Github
>23.01.11

## Github란
- Git을 사용하는 프로젝트의 협업을 위한 웹호스팅 서비스
- 내 컴퓨터의 로컬 저장소를 다른 사람과 공유
- 포트폴리오를 자랑할 수 있는 공간
- 개발자의 SNS

### 1) Github에서 원격 저장소 생성

1. Github화면 오른쪽 상단 더하기(+) 버튼을 누르고 New repository를 클릭한다.
2. 저장소의 이름, 설명, 공개 여부를 선택하고 Create repository를 클릭한다.

### 2) 로컬 저장소와 원격 저장소 연결

1. 원격 저장소가 잘 생성되었는지 확인 후, 저장소의 HTTPS주소를 복사한다.(SHH의 경우 추후 배울 예정)

2. 작업을 하고싶은 디렉토리의 폴더로 가서 vscode를 연다.

3. git init을 통해 작업하고싶은 디렉토리의 폴더를 로컬 저장소로 만들어준다.
    
    ```bash
    $ git init
    ```

1. git remote
    
    로컬 저장소에 원격 저장소를 `등록, 조회, 삭제`할 수 있는 명령어
    
    1. 등록
        
        `git remote add <이름> <주소>` 형식으로 작성한다.
        
        ```bash
        $ git remote add origin 2)-1.의 주소
        # origin이라는 이름으로 원격저장소와 연결한다.
        ```
        
    2. 조회
        
        `git remote -v` 로 작성합니다.
        
        ```bash
        $ git remote -v
        origin 2)-1.의 주소 (fetch)
        origin 2)-1.의 주소 (push)
        
        # add를 이용해 추가했던 원격 저장소의 이름과 주소가 출력된다.
        ```
        
    3. 삭제
        
        `git remote rm <이름>` 혹은 `git remote remove <이름>` 으로 작성한다.
        
        > 로컬과 원격 저장소의 연결을 끊는 것이지, 원격 저장소 자체를 삭제하는 게 아니다.
        
        ```bash
        $ git remote rm origin
        $ git remote remove origin
        
        # origin이라는 이름의 원격저장소의 연결을 끊는다.

### 3) 원격 저장소에 업로드

1. 로컬 저장소에 커밋 생성
```bash
# 현재 상태 확인
$ git status
```

```bash
$ git add 커밋할 파일이나 폴더
```

```bash
$ git commit -m "커밋 메세지"
```

```bash
# 커밋 확인
$ git log --oneline
```

2. 원격 저장소에 올리기   

git push
- 로컬 저장소의 커밋을 원격 저장소에 업로드하는 명령어
- `git push <저장소 이름> <브랜치 이름>` 형식으로 작성한다.
- `-u` 옵션을 사용하면, 두 번째 커밋부터는 `저장소 이름, 브랜치 이름`을 생략 가능하다.

```bash
$ git push origin master
# 이 방식으론 매 push마다 이렇게 작성
------------------------------------------------
$ git push -u origin master
# 이 방식으론 처음만 이렇게 하고 다음부턴 
# $ git push로 작성
```

### 3) vscode 자격 증명

1. Sign in with your browser 클릭
2. Authorize GitCredentialManager 클릭

### 4) 원격 저장소에서 정상 업로드 확인