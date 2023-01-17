# 파이썬과 MariaDB 연동

## 01. 환경 설정

### 연동 라이브러리 pymysql 설치
- CMD 창 명령프롬프트에서 “pip install pymysql” 수행

## 02. 입력 프로그램

### 파이썬 코딩 순서
1. MariaDB 연결
    - 연결자 = pymysql.connect( 연결옵션 )
2. 커서 생성
    - 커서명 = 연결자.cursor()
3. 데이터 입력
    - 커서명.execute(“INSERT 문장”)
4. 입력 데이터 저장
    - 연결자.commit()
5. MariaDB 연결 종료
    - 연결자.close()

### 파이썬 예제
```python
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='sqldb')
cur = conn.cursor()    
sql = "INSERT INTO userTBL(userID, name, birthYear, addr) VALUES('KIM', '김씨', 1991, '서울');"
cur.execute(sql)
conn.commit()
conn.close()
```

## 03. 조회 프로그램

### 파이썬 코딩 순서
1. MariaDB 연결
    - 연결자 = pymysql.connect( 연결옵션 )
2. 커서 생성
    - 커서명 = 연결자.cursor()
3. 데이터 조회
    - 커서명.execute(“SELECT 문장”)
4. 조회 데이터 출력 -> 반복
    - 커서명.fetchone()
5. MariaDB 연결 종료
    - 연결자.close()    

### 파이썬 예제
```python
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='sqldb')
cur = conn.cursor()
sql = "SELECT userid, name FROM userTBL;"
cur.execute(sql)
while True:
	row = cur.fetchone()
	if row == None: break;
print(row[0], row[1])
conn.close()
```