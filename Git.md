# Git
>23.01.11

## git이란 
- 분산 버전 관리 프로그램
- 백업, 복구, 협업을 위해 사용
- [Git 공식문서](https://git-scm.com/book/ko/v2)

![Git로고](https://user-images.githubusercontent.com/49775540/168756716-68f9aebb-380f-4897-8141-78d8403f6113.png)

### git 초기설정
1. bash 커맨드창을 이용하여 커밋을 남기는 사람을 저장한다.
```bash
$ git config --global user.name "유저 이름"
$ git config --global user.email "유저 메일 주소"
```
2. 올바르게 저장되었는지 확인한다.
```bash
$ git config --global -l
$ git config --global -list
```
### 명령어

#### 1) git init

- 현재 작업중인 디렉토리를 git으로 관리한다는 명령어
- Repository인 숨김폴더 `.git`을 생성하고 터미널에는 `(master)`라고 표기된다.
- mac os의경우 `(master)`가 표시되지 않는데, 터미널 업그레이드로 표시할 수 있다.
- 주의사항
    - 상위폴더에서 작업하지 않는다.
        - home에서 생성하지 않는다.
        - 작업 폴더를 항상 확인해야한다.
    - git init은 한번만 실행한다

```bash
$ git init
```

#### 2) git status

- Working Directory와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어
- 어떤 작업을 시행하기 전에 수시로 status를 확인하는게 좋다.
- 상태
    1. `Untracked` : Git이 관리하지 않는 파일 (한번도 Staging Area에 올라간 적 없는 파일)
    2. `Tracked` : Git이 관리하는 파일
        1. `Unmodified` : 최신 상태
        2. `Modified` : 수정되었지만 아직 Staging Area에는 반영하지 않은 상태
        3. `Staged` : Staging Area에 올라간 상태
```bash
$ git status
```

#### 3) git add

- Working Directory에 있는 파일을 Staging Area로 올리는 명령어
- Git이 해당 파일을 추적(관리)할 수 있도록 만든다.
- `Untracked, Modified → Staged` 로 상태를 변경한다.

```bash
# 특정 파일
$ git add a.txt

# 특정 폴더
$ git add my_folder/

# 현재 디렉토리에 속한 파일/폴더 전부
$ git add .
```

#### 4) git commit

- Staging Area에 올라온 파일의 변경 사항을 하나의 버전(커밋)으로 저장하는 명령어
- `커밋 메세지`는 현재 변경 사항들을 잘 나타낼 수 있도록 `의미` 있게 작성해야한다.
- 각각의 커밋은 `SHA-1` 알고리즘에 의해 반환 된 고유의 해시 값을 ID로 가진다.
- `(root-commit)` 은 해당 커밋이 최초의 커밋 일 때만 표시됩니다. 이후 커밋부터는 사라진다.

```bash
$ git commit -m "커밋 메세지"
                #알아보기 쉽게 커밋 메세지 작성
```

#### 5) git log

- 커밋의 내역(`ID, 작성자, 시간, 메세지 등`)을 조회할 수 있는 명령어
- 옵션
    - `--oneline` : 한 줄로 축약해서 보여준다.
    - `--graph` : 브랜치와 머지 내역을 그래프로 보여준다.
    - `--all` : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여준다.
    - `--reverse` : 커밋 내역의 순서를 반대로 보여준다. (최신이 가장 아래)
    - `-p` : 파일의 변경 내용도 같이 보여준다.
    - `-2` : 원하는 갯수 만큼의 내역을 보여준다. (2 말고 임의의 숫자 사용 가능)

```bash
$ git log #(--one line --graph ...)
```

#옵션과 인자   
- 옵션   
명령어 동작의 부가적인 기능 사용 -> 없어도 작동    
ex) git log **--oneline**
- 인자   
명령어 동작의 대상 지정 -> 없으면 오류발생    
ex) git add **. or README.md**

#### 4) git flow
![git_flow](https://www.notion.so/4-Git-db2f2e87d7594724b6308d13b51daff8#d5aefe3792f849b499b40fb0af7b66dd)