# Work Flow
>현업에서 Github가 어떻게 사용되는지 실습을 통해 알아본다.

💡 **Branch를 이용해 협업을 하는 두 가지 방법**에 대해 알아본다.
1. 원격 저장소 소유권이 있는 경우 (Shared repository model)
2. 원격 저장소 소유권이 없는 경우 (Fork & Pull model)

## 원격 저장소 소유권이 있는 경우 (Shared repository model)

### 1. 개념

- 원격 저장소가 자신의 소유이거나 collaborator로 등록되어 있는 경우에 가능다.
- master에 직접 개발하는 것이 아니라, `기능별로 브랜치`를 따로 만들어서 개발한다.
- `Pull Request`를 같이 사용하여 팀원 간 변경 내용에 대한 소통을 진행한다.

### 2. 작업 흐름

1. 소유권이 있는 원격 저장소를 로컬 저장소로 `clone` 받는다.

    ```bash
    $ git clone 원격 저장소 주소
    ```

2. 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성`하고, 그 안에서 `기능을 구현`한다.
    
    ```bash
    $ git switch -c feature/login
    ```
    
3. 기능 구현이 완료되면, 원격 저장소에 해당 브랜치를 `push` 한다.
    
    ```bash
    $ git push origin feature/login
    ```
    
4. 원격 저장소에는 master와 각 기능의 브랜치가 반영된다.

5. Pull Request를 통해 브랜치를 master에 반영해달라는 요청을 보낸다.
(팀원들과 코드 리뷰를 통해 소통할 수 있다.)
    
6. 병합이 완료되면 원격 저장소에서 병합이 완료된 브랜치는 불필요하므로 삭제한다.    

7. master에 브랜치가 병합되면, 각 사용자는 로컬의 master 브랜치로 이동한다.

    ```bash
    $ git switch master
    ```
    
8. 병합으로 인해 변경된 원격 저장소의 master 내용을 로컬에 받아온다.

    ```bash
    $ git pull origin master
    ```
    
9. 병합이 완료된 master의 내용을 받았으므로, 기존 로컬 브랜치는 삭제한다. (한 사이클 종료)
    
    ```bash
    $ git branch -d feature/login
    ```
    
10. 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복한다.
    
    ```bash
    $ git switch -c feature/pay
    ```
    

##  원격 저장소 소유권이 없는 경우 (Fork & Pull model)

### 1. 개념

- 오픈 소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우 사용한다.
- 원본 원격 저장소를 그대로 내 원격 저장소에 `복제`한다. (이 행위를 `fork`라고 한다.)
- 기능 완성 후 `Push는 복제한 내 원격 저장소에 진행`한다.
- 이후 `Pull Request`를 통해 원본 원격 저장소에 반영될 수 있도록 요청한다.

### 2. 작업 흐름

1. 소유권이 없는 원격 저장소를 `fork`를 통해 내 원격 저장소로 `복제`한다.

     `Fork` 버튼을 누르면 자동으로 내 원격 저장소에 복제된다.
    
2. `fork` 후, 복제된 내 원격 저장소를 로컬 저장소에 `clone` 받는다.
    
    ```bash
    $ git clone 내 원격 저장소 주소
    ```

3. 이후에 로컬 저장소와 원본 원격 저장소를 동기화 하기 위해서 연결한다.
    
    ```bash
    # 원본 원격 저장소에 대한 이름은 upstream으로 붙이는 것이 일종의 관례
    
    $ git remote add upstream 원본 원격 저장소 주소
    ```
    
4. 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성`하고, 그 안에서 `기능을 구현`한다.

    ```bash
    $ git switch -c feature/login
    ```
    
5. 기능 구현이 완료되면, `복제 원격 저장소(origin)`에 해당 브랜치를 `push` 한다.
    
    ```bash
    $ git push origin feature/login
    ```
    
6. `복제 원격 저장소(origin)`에는 master와 브랜치가 반영된다.

7. `Pull Request`를 통해 `복제 원격 저장소(origin)의 브랜치`를 `원본 원격 저장소(upstream)의 master`에 반영해달라는 요청을 보낸다. 
(원본 원격 저장소의 관리자가 코드 리뷰를 진행하여 반영 여부를 결정한다.)

8. `원본 원격 저장소(upstream)`의 master에 브랜치가 병합되면 `복제 원격 저장소(origin)`의 브랜치는 삭제한다. 그리고 사용자는 로컬에서 master 브랜치로 이동한다.
    
    ```bash
    $ git switch master
    ```
    

9. 병합으로 인해 변경된 `원본 원격 저장소(upstream)의 master` 내용을 로컬에 받아온다. 
그리고 기존 로컬 브랜치는 삭제한다. (한 사이클 종료)

    ```bash
    $ git pull upstream master
    $ git branch -d feature/login
    ```
    
10. 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복한다.

    ```bash
    $ git switch -c feature/pay
    ```

##  Pull Request (PR) 자세히 알아보기
> Github 화면을 통해 Pull Request 과정을 자세히 알아본다.
> 

1. 브랜치를 Push 하면 `Compare & pull request` 라는 알림 버튼이 나타나는데, 이를 누르면 된다.
 
2. 혹은 원격 저장소 상단 바에서 `Pull requests → New pull request`을 통해서도 가능하다.
   
3. `base`는 병합될 대상이다. `master를 base로` 두면 된다.
`compare`는 병합할 대상이다. 우리가 만든 `feature/login 브랜치를 compare로` 두면 된다.
그리고 아래쪽에서 비교 내용을 확인하고 `Create pull request`를 클릭한다.

4. Pull Request에 대한 제목과 내용, 각종 담당자를 지정하는 페이지가 나온다.
모두 작성했다면 `Create pull request`를 눌러서 PR을 생성한다.
    
    `Reviewers` : 현재 PR에 대해 코드 리뷰를 진행해 줄 담당자
    
    `Assignees` : 현재 PR에 대한 작업을 맡고 있는 담당자
    
5. PR이 생성되면 다음과 같은 화면이 나타난다. 왼쪽 상단에 checks를 뺀 세 부분을 살펴보자.
    
6. `Conversation` : 아래 Write 부분에서 comment를 별도로 작성할 수도 있다. 그리고 `Merge pull request` 버튼을 누르면 병합이 시작된다. (충돌(conflict) 상황에서는 충돌을 해결하라고 나온다.)
    
7. `Commits` : PR을 통해 반영될 커밋들을 볼 수 있다.
    
8. `Files changed` : 파일의 변화 내역들을 볼 수 있다.
    
9. 코드리뷰를 원하는 라인에서 `+` 를 눌러서 해당 라인에 리뷰를 남길 수 있다.
    
    빨간 사각형으로 표시된 작은 아이콘을 클릭하면, 
    **`suggestion 기능`(코드를 이렇게 바꾸라고 추천하는 기능)**을 넣을 수도 있다.
    
10. 코드 리뷰를 끝내려면 `Finish your review` 버튼을 누르면 된다. 
그리고 옵션을 선택하고 `Submit review`를 클릭한다.
    
    - `Comment`: 추가적인 comment를 작성할 경우 선택
    - `Approve`: merge를 승인하는 경우 선택
    - `Request change` : 수정해야 하는 사항이 있을 경우 선택   

11. 다시 conversation으로 가보면 진행했던 리뷰가 나타난 것을 확인할 수 있다.

12. 병합을 했을 때 좌측 상단에 보라색으로 병합이 완료되었다고 나오면 성공이다.
    
    `Delete branch` 버튼을 통해 병합된 `feature/login` 브랜치를 지울 수 있다. 
    (원격 저장소에서만 지워진다.)
    
13. `master`를 확인해보면 `feature/login`의 내용이 master에 병합된 것을 확인할 수 있다.

14. 이후 로컬 저장소의 master 브랜치에서 `git pull`을 이용해 로컬과 원격을 동기화 한다.

## Pull Request 실습 - N행시 짓기

> 소유권이 없는 상태에서의 협업하는 방법(fork 와 pull request)에 대해 익혀 보자.
> 
1. 강사의 깃허브에 있는 `acrostic-poem` repository를 fork한다.
2. 교육생은 fork 한 자신의 repository를 `clone`하여 자신의 local에 복제한다.
3. `교육생 이름`으로 된 브랜치를 생성하고, 주어진 명제에 따라 N행시를 작성한다.
4. 작성을 완료한 결과물에 대해 커밋 후 `push` 한다.
    - master 브랜치가 아닌, 자신 이름으로 된 브랜치로 push 해야 한다.
    - 강사의 repository가 아닌, fork 한 자신의 repository로 push 해야 한다.
5. 깃허브에서 강사의 repository에 `Pull Request` 를 보내 본다.
    
6. 이후 아래처럼 강사의 repository의 Pull Request 목록에서 자신의 요청을 찾아본다.

📌 **요약**

`fork`→`clone`→브랜치 생성→ `add` → `commit` → 브랜치 `push` → `pull request` 보내기