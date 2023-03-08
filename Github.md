# Github
>23.01.11

## Github란
- Git을 사용하는 프로젝트의 협업을 위한 웹호스팅 서비스
- 내 컴퓨터의 로컬 저장소를 다른 사람과 공유
- 포트폴리오를 자랑할 수 있는 공간
- 개발자의 SNS

### 1. Github에서 원격 저장소 생성

1. Github화면 오른쪽 상단 더하기(+) 버튼을 누르고 New repository를 클릭한다.
2. 저장소의 이름, 설명, 공개 여부를 선택하고 Create repository를 클릭한다.

### 2. 로컬 저장소와 원격 저장소 연결

1. 원격 저장소가 잘 생성되었는지 확인 후, 저장소의 HTTPS주소를 복사한다.(SHH의 경우 추후 배울 예정)

2. 작업을 하고싶은 디렉토리의 폴더로 가서 vscode를 연다.

3. git init을 통해 작업하고싶은 디렉토리의 폴더를 로컬 저장소로 만들어준다.
    
    ```bash
    $ git init
    ```


4. git remote
    
    로컬 저장소에 원격 저장소를 `등록, 조회, 삭제`할 수 있는 명령어
    
    1. 등록
        
        `git remote add <이름> <주소>` 형식으로 작성한다.
        
        ```bash
        $ git remote add origin 2)-1.의 주소
        # origin이라는 이름으로 원격저장소와 연결한다.
        # ~~~.git으로 끝나도록 작성한다.
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

### 3. 원격 저장소에 업로드

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

3. vscode 자격 증명

    1. Sign in with your browser 클릭
    2. Authorize GitCredentialManager 클릭

### 4. 원격 저장소에서 정상 업로드 확인

설정한 원격 저장소에서 업로드 된 것을 확인한다.

### 5. 원격 저장소 가져오기

> 지금까지는 로컬 저장소의 내용을 원격 저장소에 업로드하는 것을 학습했다.
이번에는 반대로, 원격 저장소의 내용을 로컬 저장소로 가져오는 것을 학습한한다.

#### 1) git clone

- 원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어
- clone은 `"복제"`라는 뜻으로, `git clone` 명령어를 사용하면 원격 저장소를 통째로 복제해서 내 컴퓨터에 옮길 수 있다.
- `git clone <원격 저장소 주소>`의 형태로 작성한다.
    
    ```bash
    $ git clone 불러올 원격 저장소 주소
                      #주소는 .git으로 끝나야 한다.  
    ```

    
- git clone을 통해 생성된 로컬 저장소는 `git init`과 `git remote add`가 이미 수행되어 있다.
    - git init을 한번 더 하면 안된다.

#### 2) git pull

- 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트하는 명령어
    - 이미 clone한 저장소에서 사용한다.
- 로컬 저장소와 원격 저장소의 내용이 완전 일치하면 git pull을 해도 변화가 일어나지 않는다.
- `git pull <저장소 이름> <브랜치 이름>`의 형태로 작성한다.
    
    ```bash
    $ git pull origin master
    [풀이]
    git 명령어를 사용할건데, origin이라는 원격 저장소의 master 브랜치의 내용을 가져온다(pull).
    ```

### 6. 내 컴퓨터 ↔ Github(원격 저장소) ↔ 강의장 컴퓨터 (예시)

> 두 개 이상의 로컬 저장소에서 하나의 원격 저장소에 접근하면 어떻게 될까?
집과 강의장을 오가면서 `clone, push, pull` 하는 과정을 가정해본다.
> 

#### 1) 규칙

- 수업 때는 두 개의 폴더를 `"내 컴퓨터"`와 `"강의장 컴퓨터"` 라고 가정한다.
- 내 컴퓨터에 있는 로컬 저장소의 이름은 `TIL-home` 이다.
- 강의장 컴퓨터에 있는 로컬 저장소의 이름은 `TIL-class` 이다.
- Github에 있는 원격 저장소의 이름은 `TIL-remote` 이다.

#### 2) 사전 세팅

- 홈 디렉토리 안에 `TIL-home` 폴더를 생성한다.
- Github에서 `TIL-remote` 라는 이름의 원격 저장소를 생성한다.
- `TIL-home` 폴더에서 vscode를 연다.
- 아래와 같은 절차를 진행한다.
    
    ```bash
    # TIL-home
    
    $ git init
    $ touch day1.md
    $ git add .
    $ git commit -m "집에서 Day1 작성"
    $ git remote add origin https://github.com/edukyle/TIL-remote.git
    $ git push origin master
    ```
    
    `TIL-home` 로컬 저장소의 내용이 `TIL-remote` 원격 저장소에 그대로 반영되었습니다.

#### 3) git clone

> 다시 강의장에 왔을 때 강의장에는 `TIL-home`폴더가 없다.
> 
- Github에 있는 `TIL-remote`에서 `git clone`을 통해 내려 받는다.
    
    ```bash
    # TIL-class
    
    $ git clone https://github.com/edukyle/TIL-remote.git TIL-class
    ```
    
    **원격 저장소는 `TIL-remote` 이지만, 위와 같이 작성하면 강의장 컴퓨터에는 `TIL-class`라는 이름으로 로컬 저장소가 생성된다.**

#### 4) git push

> 강의장 컴퓨터 → 원격 저장소
> 
- 강의장에서 새로운 파일을 만들고 원격 저장소에 업로드 한다.
    
    ```bash
    # TIL-class
    
    $ touch day2.md
    $ git add .
    $ git commit -m "강의장에서 Day2 작성"
    $ git push origin master
    ```

#### 5) git pull

> 원격 저장소 → 내 컴퓨터
> 
- 강의장 컴퓨터에서 day2.md를 만들어서 원격 저장소에 push 했기 때문에 내 컴퓨터에는 day2.md가 없다. 따라서 원격 저장소에서 day2.md에 대한 내역을 가져와야 한다.
    
    ```bash
    # TIL-home
    
    $ git pull origin master
    ```
이제 내 컴퓨터, Github, 강의장 컴퓨터의 내용은 모두 같다.

error: failed to push some refs to 'https://github.com/edukyle/TIL-remote.git'


❗ **만약 TIL-home에서 pull이 아니라 commit을 먼저한 후 pull을 하면 어떻게 될까?
다음 세 가지의 경우가 있을 수 있다.**

1. 내 컴퓨터와 강의장 컴퓨터에서 **서로 다른 파일을 수정**한 경우
→ 정상적으로 git pull이 된다.

2. 내 컴퓨터와 강의장 컴퓨터에서 **같은 파일을 수정했지만, 수정한 라인이 다른** 경우
→ 정상적으로 git pull이 된다.

3. 내 컴퓨터와 강의장 컴퓨터에서 **같은 파일의 같은 라인**을 수정한 경우
→ **충돌(conflict)**이 발생한다. 어느 내용을 반영할지 직접 선택해야 한다.


❗ **만약 TIL-home에서 pull이 아니라 commit을 먼저한 후 바로 push 하면 어떻게 될까?**
**아래와 같은 에러 메시지가 나타나면서 push가 실패한다.**

To https://github.com/edukyle/TIL-remote.git

! [rejected]        master -> master (non-fast-forward)

error: failed to push some refs to 'https://github.com/edukyle/TIL-remote.git'

원격 저장소의 내용을 먼저 받아오지 않고, 로컬 저장소에서 새로운 커밋을 생성했기 때문에 서로의 커밋 내역이 달라져서 그렇다.

만약 로컬 저장소와 원격 저장소의 내용이 다르다면 일단 git pull을 통해 동기화를 시키고 새로운 커밋을 쌓아 나가야 한다.

### 7. .gitignore

> 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 것
> 

#### 1) .gitignore에 작성하는 목록

- 민감한 개인 정보가 담긴 파일 (전화번호, 계좌번호, 각종 비밀번호, API KEY 등)
- OS(운영체제)에서 활용되는 파일
- IDE(통합 개발 환경 - pycharm) 혹은 Text editor(vscode) 등에서 활용되는 파일
    - 예) pycharm -> .idea/
- 개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일
    - 가상 환경 : `venv/`
    - `__pycache__/`

#### 2) .gitignore 작성 시 주의 사항

- 반드시 이름을 `.gitignore`로 작성한다. 앞의 점(.)은 숨김 파일이라는 뜻이다.
- `.gitignore` 파일은 `.git` 폴더와 동일한 위치에 생성한다.
- **제외 하고 싶은 파일은 반드시 `git add` 전에 `.gitignore`에 작성한다.**
    
   
    ❗ **왜 git add 전에 .gitignore에 작성해야 할까?**
    
    `git add a.txt` 라고 작성하면, 이제 Git은 `a.txt`를 버전 관리의 대상으로 여긴다.
    한 번 버전 관리의 대상이 된 `a.txt`는 이후에 .gitignore에 작성하더라도
    무시되지 않고 계속 버전 관리의 대상으로 인식된다.
    
    따라서 제외 하고 싶은 파일은 반드시 git add 전에 .gitignore에 작성해야 한다!
    
#### 3) .gitignore 쉽게 작성하기

> .gitignore의 내용을 쉽게 작성할 수 있도록 도와주는 두 개의 사이트이다.
자신의 개발 환경에 맞는 것을 찾아서 `전체 복사, 붙여넣기`를 하면 된다.
> 
1. **웹사이트**

[gitignore.io](https://gitignore.io/)

1. **gitignore 저장소**

[https://github.com/github/gitignore](https://github.com/github/gitignore)

1. **Python에 대한 .gitignore 예시**
    
    [https://gitignore.io/](https://gitignore.io/)

    
### 8. .gitignore 심화

> .gitignore에 대한 추가 정보
> 

#### 1) .gitignore 패턴 규칙

1. 아무것도 없는 라인이나, `#`로 시작하는 라인은 무시한다.
2. `슬래시(/)`로 시작하면 하위 디렉터리에 재귀적으로 적용되지 않는다.
3. 디렉터리는 `슬래시(/)`를 끝에 사용하는 것으로 표현한다.
4. `느낌표(!)`로 시작하는 패턴의 파일은 ignore(무시)하지 않는다.
5. **표준 Glob 패턴을 사용한다.**
    - `*(asterisk)`는 문자가 하나도 없거나 하나 이상을 의미한다.
    - `[abc]`는 중괄호 안에 있는 문자 중 하나를 의미한다.
    - `물음표(?)`는 문자 하나를 의미한다.
    - `[0-9]`처럼 중괄호 안에 하이픈(-)이 있는 경우 0에서 9사이의 문자 중 하나를 의미한다.
    - `**(2개의 asterisk)`는 디렉터리 내부의 디렉터리까지 지정할 수 있다.
    (`a/**/z`라고 작성하면 `a/z`, `a/b/z`, `a/b/c/z` 까지 모두 영향을 끼친다.)

#### 2) 패턴 예시

```bash
# .gitignore

# 확장자가 txt인 파일 무시
*.txt

# 현재 확장자가 txt인 파일이 무시되지만, 느낌표를 사용하여 test.txt는 무시하지 않음
!test.txt

# 현재 디렉터리에 있는 TODO 파일은 무시하고, folder/TODO 처럼 하위 디렉터리에 있는 파일은 무시하지 않음
/TODO

# build/ 디렉터리에 있는 모든 파일은 무시
build/

# folder/notes.txt 파일은 무시하고 folder/child/arch.txt 파일은 무시하지 않음
folder/*.txt

# folder 디렉터리 아래의 모든 .pdf 파일을 무시
folder/**/*.pdf
```
