# SQL 고급

## 01. DATA TYPE/형변환

### DATA TYPE : 숫자형

|                 DATA TYPE                |      BYTES    |            RANGE          |                                    COMMENT                                  |
|:----------------------------------------:|:-------------:|:-------------------------:|:---------------------------------------------------------------------------:|
|                  SMALLINT                |        2      |      -32,768 ~ 32,768     |                                     정수                                    |
|              INT     INTEGER             |        4      |       약 -21억 ~ 21억     |                                     정수                                    |
|                   BIGINT                 |        8      |      약 -900경 ~ 900경    |                                     정수                                    |
|                   FLOAT                  |        4      |     -1.7e+38 ~ 1.7e+38    |              실수 : 부동 소숫점     (소수점 아래 7자리까지 표현)            |
|              DOUBLE     REAL             |        8      |          거의 무한        |            실수 : 부동   소숫점    (소수점 아래 15자리까지 표현)           |
|     DECIMAL(m,[d])     NUMERIC(m,[d])    |     5 ~ 17    |     -10e38+1 ~ 10e38-1    |     실수 : 고정 소숫점     (m : 전체 자릿수,     d : 소수점 이하 자릿수)    |

### DATA TYPE : 문자형

|      DATA TYPE    |      BYTES     |                           COMMENT                          |                                    COMMENT                                  |
|:-----------------:|:--------------:|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
|       CHAR(n)     |      1~255     |               고정길이 문자형     (Character)              |                                     정수                                    |
|     VARCHAR(n)    |     1~65535    |           가변길이 문자형     (Variabel Character)         |                                     정수                                    |
|        TEXT       |     1~65535    |                       TEXT   데이터                        |                                     정수                                    |
|      LONGTEXT     |       ~4G      |                      대용량 TEXT 데이터                    |              실수 : 부동 소숫점     (소수점 아래 7자리까지 표현)            |
|        BLOB       |     1~65535    |                         BLOB 데이터                        |            실수 : 부동   소숫점     (소수점 아래 15자리까지 표현)           |
|      LONGBLOB     |       ~4G      |     대용량 BLOB 데이터     (BLOB : Binary Large Object)    |     실수 : 고정 소숫점     (m : 전체 자릿수,     d : 소수점 이하 자릿수)    |

### DATA TYPE : 날짜 / 시간

|    <br>DATA TYPE    |    <br>BYTES    |                <br>COMMENT                |
|:-------------------:|:---------------:|:-----------------------------------------:|
|       <br>DATE      |      <br>3      |         <br>‘YYYY-MM-DD’ 형식 사용        |
|       <br>TIME      |      <br>3      |          <br>‘HH:MM:SS’ 형식 사용         |
|     <br>DATETIME    |      <br>8      |    <br>‘YYYY:MM:DD HH:MM:SS’ 형식 사용    |
|       <br>YEAR      |      <br>1      |        <br>‘YYYY’   형식으로   사용       |

### 변수의 사용

```sql
  -- SQL에서 변수 선언 및 활용
  SET @변수명 = 값;
  SELECT @변수명;
```

```sql
  -- 스토어드 프로그램에서 변수 선언
  DECLARE 변수명
  SET 변수명 = 값;
  SELECT 변수명;
```

### DATA 형 변환

```sql
  -- 함수를 이용한 형 변환 : CAST(), CONVERT()
  CAST (expression AS 데이터 형식 [ (길이) ] )
  CONVERT (expression, 데이터 형식 [ (길이) ] )

```

```sql
  SELECT CAST (AVG(amount) AS INTEGER) FROM buyTBL;
  SELECT CONVERT (AVG(amount), INTEGER) FROM buyTBL;
```

```sql
  -- 자동 형 변환 = 비교, 연산 시 데이터 타입이 다를 경우 자동으로 동일한 데이터 타입으로 형 변환을 진행한다.
  SELECT '100' + '200';				-- 300 : + 연산자 영향
  SELECT CONCAT(100, '200') 		-- ‘100200’ : CONCAT 영향
  SELECT 1 > '2dolors';				-- 0 : > 연산자 영향 (‘2dolors’ -> 2로 반환)
```

## 02. 내장/윈도우 함수

### 제어 흐름 함수

|                    <br>함수명                    |                                                         <br>기본구문                                                         |                                                        <br>설명                                                        |
|:------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|
|                    <br>**IF**                    |    <br>IF(수식, 값1, 값2)                                                                                                    |    <br>수식이 참이면 값1을, 거짓이면 값2를 반환                                                                        |
|                  <br>**IFNULL**                  |    <br>IFNULL(수식1, 수식2)                                                                                                  |    <br>수식1 값이   NULL이 아니면 수식1,   NULL이면   수식2   반환                                                     |
|                  <br>**NULLIF**                 |    <br>NULLIF(수식1, 수식2)                                                                                                  |    <br>수식1과 수식2가 같으면 NULL,<br>   <br>같지 않으면 수식1   반환                                                 |
|  <br>**CASE   ~ WHEN ~<br>   <br>ELSE   ~ END**  |    <br>CASE 수식<br>   <br>    WHEN 수식1 THEN 값1<br>   <br>    WHEN 수식2 THEN 값2<br>   <br>    ELSE 값3<br>   <br>END    |    <br>수식이 수식1과 같으면 값1,<br>   <br>수식이 수식2와 같으면 값2,<br>   <br>수식이 모두 같지 않으면 값3   반환    |

### 문자열 함수

|               <br>함수명               |                              <br>기본구문                              |                                                <br>설명                                               |
|:--------------------------------------:|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------:|
|                <br>ASCII               |    <br>ASCII(아스키코드)                                               |    <br>아스키코드에 해당하는 숫자값 반환                                                              |
|                 <br>CHR                |    <br>CHR(숫자)                                                       |    <br>숫자에 해당하는 아스키코드값 반환                                                              |
|             <br>BIT_LENGTH             |    <br>BIT_LENGTH(문자열)                                              |    <br>문자열의 BIT   크기   반환                                                                     |
|             <br>CHAR_LENGTH            |    <br>CHAR_LENGTH(문자열)                                             |    <br>문자열의 문자 개수 반환                                                                        |
|               <br>LENGTH               |    <br>LENGTH(문자열)                                                  |    <br>문자열의 BYTES 크기   반환                                                                     |
|               <br>CONCAT               |    <br>CONCAT(문자열1,문자열2, ∙∙∙)                                    |    <br>문자열과 문자열을 연결함                                                                       |
|                <br>INSTR               |    <br>INSTR(문자열, 검색어)                                           |    <br>문자열내 검색어를 찾아   시작 위치 반환                                                        |
|             <br>**FORMAT**             |    <br>FORMAT(숫자, 소수점자리수)                                      |    <br>소수점자리수만큼 표현,   1000단위 “,” 표시                                                     |
|               <br>INSERT               |    <br>INSERT(문자열,위치,길이,<br>   <br>              추가문자열)    |    <br>문자열의 위치부터 길이만큼 삭제 후 <br>   <br>추가문자열 삽입                                  |
|         <br>**LEFT   / RIGHT**         |    <br>LEFT / RIGHT<br>   <br>(문자열, 길이)                           |    <br>왼쪽 문자열에서 길이만큼 반환<br>   <br>오른쪽 문자열에서 길이만큼 반환                        |
|           <br>UPPER   / LOWER          |    <br>UPPER   / LOWER<br>   <br>(문자열, 길이)                        |    <br>소문자를 대문자로 변경<br>   <br>대문자를 소문자로 변경                                        |
|             <br>LPAD / RPAD            |    <br>LPAD   / RPAD<br>   <br>(문자열,길이,채울문자열)                |    <br>문자열을 길이만큼 문자열에 추가                                                                |
|    <br>TIRM<br>   <br>LTRIM / RTRIM    |    <br>TRIM()<br>   <br>LTRIM() / RTRIM()                              |    <br>앞뒤   공백제거<br>   <br>왼쪽 / 오른쪽   공백 제거                                            |
|               <br>REPEAT               |    <br>REPEAT(문자열, 횟수)                                            |    <br>문자열을 횟수만큼 반복                                                                         |
|             <br>**REPLACE**            |    <br>REPLACE(문자열, 기존   문자열, 바꿀   문자열)                   |    <br>문자열에서 기존 문자열을 찾아<br>   <br>바꿀 문자열로 변환                                     |
|               <br>REVERSE              |    <br>REVERSE(문자열)                                                 |    <br>문자열의 순서를 거꾸로 변환                                                                    |
|                <br>SPACE               |    <br>SPACE(길이)                                                     |    <br>길이만큼 공백 반환                                                                             |
|            <br>**SUBSTRING**           |    <br>SUBSTRING<br>   <br>(문자열,시작위치,길이)                      |    <br>시작위치부터 길이만큼만   문자열 반환, 길이   생략 시 문자열 끝까지                            |
|           <br>SUBSTRING_INDEX          |    <br>SUBSTRING_INDEX<br>   <br>(문자열, 구분자, 횟수)                |    <br>구분자가 횟수번째   나오면 그 이후는 버림, 횟수 음수이면 오른쪽부터 횟수를 세고 왼쪽을 버림    |

### 수학 함수

|     <br>함수명     |                          <br>기본구문                          |                         <br>설명                        |
|:------------------:|:--------------------------------------------------------------:|:-------------------------------------------------------:|
|       <br>ABS      |    <br>ABS(숫자)                                               |    <br>숫자의 절대값 반환                               |
|    <br>삼각함수    |    <br>SIN(), COS(), TAN()<br>   <br>ASIN(), ACOS(), ATAN()    |    <br>삼각함수 결과값 반환                             |
|    <br>**CEIL**    |    <br>CEIL(숫자)                                              |    <br>숫자의 올림값 계산                               |
|    <br>**FLOOR**   |    <br>FLOOR(숫자)                                             |    <br>숫자의 내림값 계산                               |
|    <br>**ROUND**   |    <br>ROUND(숫자)                                             |    <br>숫자의 반올림값 계산                             |
|       <br>MOD      |    <br>MOD(숫자1, 숫자2)                                       |    <br>숫자1을 숫자2로 나눈 나머지 값                   |
|       <br>POW      |    <br>POW(숫자1, 숫자2)                                       |    <br>숫자1의 숫자2   제곱값                           |
|      <br>SQRT      |    <br>SQRT(숫자)                                              |    <br>숫자의 제곱근 값                                 |
|    <br>**RAND**    |    <br>RAND()                                                  |    <br>0   이상 1   미만의   실수                       |
|  <br>**TRUNCATE**  |    <br>TRUNCATE<br>   <br>(숫자, 소수점자리수)                 |    <br>숫자를 소수점 자리수까지   구하고 나머지 버림    |

### 날짜 및 시간 함수

|                       <br>함수명                       |                              <br>기본구문                              |                                     <br>설명                                    |
|:------------------------------------------------------:|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
|          <br>**ADDDATE   /<br>   <br>SUBDATE**         |    <br>ADDDATE   / SUBDATE<br>   <br>(날짜, 차이)                      |    <br>날짜를 기준으로 차이를 더함<br>   <br>날짜를 기준으로 차이를 뺌          |
|           <br>ADDTIME   / <br>   <br>SUBTIME           |    <br>ADDTIME   / SUBTIME<br>   <br>(날짜/시간, 시간)                 |    <br>날짜/시간 기준으로 시간을 더함<br>   <br>날짜/시간 기준으로 시간을 뺌    |
|                       <br>CURDATE                      |    <br>CURDATE()                                                       |    <br>현재 연-월-일                                                            |
|                       <br>CURTIME                      |    <br>CURTIME()                                                       |    <br>현재 시:분:초                                                            |
|                 <br>**NOW   / SYSDATE**                |    <br>NOW() / SYSDATE()                                               |    <br>현재 연-월-일 시:분:초                                                   |
|  <br>**YEAR   / <br>   <br>MONTH   / <br>   <br>DAY**  |    <br>YEAR(날짜) /<br>   <br>MONTH(날짜) / <br>   <br>DAY(날짜)       |    <br>연도 / 월 / 일 반환                                                      |
|    <br>HOUR / MINUTE<br>   <br>SECOND / MICROSECOND    |    <br>HOUR(시간) / MINUTE(시간) / SECODE(시간) / MICORSECOND(시간)    |    <br>시 / 분 / 초 / 밀리초 반환                                               |
|                      <br>**DATE**                      |    <br>DATE(날짜/시간)                                                 |    <br>연-월-일 반환                                                            |
|                      <br>**TIME**                      |    <br>TIME(날짜/시간)                                                 |    <br>시:분:초 반환                                                            |
|                      <br>DATEDIFF                      |    <br>DATEDIFF(날짜1, 날짜2)                                          |    <br>두 날짜의 차이값 반환                                                    |
|                      <br>TIMEDIFF                      |    <br>TIMEDIFF(시간1, 시간2)                                          |    <br>두 시간의 차이값 반환                                                    |
|                      <br>DAYOFWEEK                     |    <br>DAYOFWEEK(날짜)                                                 |    <br>요일 반환(1:일,   2:월 ~  7:토)                                          |
|                      <br>MONTHNAME                     |    <br>MONTHNAME(날짜)                                                 |    <br>월 이름 반환                                                             |
|                      <br>DAYOFYEAR                     |    <br>DAYOFYEAR(날짜)                                                 |    <br>1년중 몇   번째 날짜인지 반환                                            |
|                      <br>LAST_DAY                      |    <br>LAST_DAY(날짜)                                                  |    <br>주어진 날짜 월의 마지막 날짜 구함                                        |
|                      <br>MAKEDATE                      |    <br>MAKEDATE(연도, 정수)                                            |    <br>연도에서 정수만큼 지난 날짜 반환                                         |
|                      <br>MAKETIME                      |    <br>MAKETIME(시, 분, 초)                                            |    <br>시:분:초 형태로 반환                                                     |
|                   <br>**PERIOD_ADD**                   |    <br>PERIOD_ADD(연월, 개월수)                                        |    <br>연월에서 개월수 지난   연월 반환                                         |
|                   <br>**PERIOD_DIFF**                  |    <br>PERIOD_DIFF(연월1,연월2)                                        |    <br>연월1 –   연월2   개월   수 반환                                         |
|                       <br>QUARTER                      |    <br>QUARTER(날짜)                                                   |    <br>날짜가 4분기중 몇 분기인지 반환                                          |
|                     <br>TIME_TO_SEC                    |    <br>TIME_TO_SEC(시간)                                               |    <br>시간을 초 단위로 구함                                                    |

### 시스템 정보 함수

|      <br>함수명      |      <br>기본구문      |                                               <br>설명                                              |
|:--------------------:|:----------------------:|:---------------------------------------------------------------------------------------------------:|
|     <br>**USER**     |    <br>USER()          |    <br>현재 사용자 확인                                                                             |
|   <br>**DATABASE**   |    <br>DATABASE()      |    <br>현재 사용중인 데이타베이스 확인                                                              |
|  <br>**FOUND_ROWS**  |    <br>FOUND_ROWS()    |    <br>바로 앞에 실행한 SELECT문에서 조회된 행의 개수 반환                                          |
|   <br>**ROW_COUNT**  |    <br>ROW_COUNT()     |    <br>바로 앞에 실행한 INSERT,   UPDATE, DELETE문에서   입력,   수정,   삭제한   행의 개수 반환    |
|      <br>VERSION     |    <br>VERSION()       |    <br>현재 MariaDB 버전   확인                                                                     |
|       <br>SLEEP      |    <br>SLEEP(초)       |    <br>쿼리의 실행을 초만큼 멈춤                                                                    |

### Text 데이터 대용량 입력하기

- 저장하고자 하는 문자가 16M 이상의 대용량일 경우 조치 방법   
my.ini 설정 파일에 max_allowed_packet 설정 값 추가
(windows : C:\Program Files\MariaDB 10.6\data\my.ini
linux : /etc/my.cnf.d/server.cnf)
```sql
[mysqld]
 max_allowed_packet=1000M
 ```
MariaDB restart : net stop/start mariadb (작업관리자  서비스 -> 재시작)


- 파일로 저장한 대용량 데이터를 테이블 데이터로 저장   
cmd창에서 실행해야 함   
```
LOAD DATA LOCAL INFILE 파일경로/파일명   
                                      INTO 테이블명;
```                    
- 저장한 대용량 데이터를 파일로 저장
```
SELECT *
    INTO OUTFILE 저장경로/파일명 
    FROM 테이블명;
   ```

### BLOB 파일 입력하기

- 이미지, 동영상, PDF 문서 등 TEXT외 파일 BLOB 형태로 저장
```
INSERT INTO 테이블명(컬럼, BLOB컬럼, …) 
     VALUES(값1, LOAD_FILE(파일경로/파일명), …);
```

- BLOB 데이터 파일로 저장
```
SELECT BLOB컬럼 INTO DUMPFILE 파일경로/파일명
    FROM 테이블명
    WHERE 조건;
```

### 윈도우 함수

- 행과 행 사이 관계를 쉽게 정의하기 위해 제공된는 함수
- 복잡한 SQL을 쉽게 활용 가능
- OVER절이 들어간 함수
- 집계 함수 : AVG(), COUNT(), MAX(), MIN(), STDDEV(), SUM(), VARIANCE()
- 비집계 함수
  - 순위 함수 : ROW_NUMBER(), DENSE_RANK(), RANK(), NTILE()
  - 분석 함수 : LEAD(), LAG(), FIRST_VALUE, CUME_DIST()

### 윈도우 순위 함수

- 조회결과에 순번, 순위(등수)를 매기는 역할을 하는 함수
- 구문 단순화, MariaDB 부하 감소
- 기본 구문
```sql
<순위함수이름>() OVER(
	[PARTITION BY 컬럼]
	ORDER BY 컬럼 [DESC]
);
```
- ROW_NUMBER() : 첫 행 1부터 다음 행에 1씩 증가
- DENSE_RANK() : 여러행이 동일한 값을 가질 경우 동순위로 처리
- RANK() : 동순위 있을 경우 다음 행은 동순위 + 동순위개수로 처리
- NTILE() : 몇 개의 그룹으로 분할
- 샘플 코드
```
SELECT ROW_NUMBER() OVER(ORDER BY height DESC) “키큰순위“,
	name, addr, height
    FROM userTBL;
```

### 윈도우 분석 함수

- 이동 평균, 백분율, 누계 등의 결과 계산
- LEAD() : 다음 행 데이터 값
- LAG() : 이전 행 데이터 값
- FIRST_VALUE() : 가장 큰 값
- CUME_DIST() : 누적합계의 백분율
```
SELECT LEAD(height, 1) OVER(ORDER BY height DESC) AS "n_height",
		 height, name, addr
    FROM userTBL;
```

### 피벗 구현

- 여러 ROW를 Column 값으로 변환하고, 필요시 집계하는 것
```sql
-- 4분기로 피벗
select pname, 
       if(season=1, amount, 0) '1Q', 
       if(season=2, amount, 0) '2Q', 
       if(season=3, amount, 0) '3Q', 
       if(season=4, amount, 0) '4Q', 
       amount 'Total'      
from pivotTest;
```
```sql
--피벗한 결과를 합해서 묶어줌
select pname, 
       sum(if(season=1, amount, 0)) '1Q', 
       sum(if(season=2, amount, 0)) '2Q', 
       sum(if(season=3, amount, 0)) '3Q', 
       sum(if(season=4, amount, 0)) '4Q', 
       sum(amount) 'Total'      
from pivotTest
group by pname;
```
### JSON

- JavaScript Object Notation
- 데이터 교환을 위해 만든 개방형 표준 포맷
- 속성(Key)와 값(Value)로 구성됨
- JavaScript 언어에서 파생되었지만, 다양한 곳에서 활용할 수 있는 독립적인 데이터 포맷
- 데이터 형식
```json
{“key1” : “value1“, “key2” : “value2”}
```
- 테이블 데이터를 JSON 형식으로 변환
```
SELECT JSON_OBJECT(‘키이름1’, 컬럼1, ‘키이름2’, 컬럼2)
  FROM 테이블명
  WHERE 조건절;
```
- 샘플 코드
```sql
SELECT JSON_OBJECT(‘name’, name, ‘height’, height)
  FROM userTBL
  WHERE height >= 180;
```

## 03. JOIN
>두 개 이상의 테이블로부터 하나의 결과 집합을 만들어 내는 것

### INNER JOIN
- 조인 중에서 가장 많이 사용되는 조인
- 두 개 테이블의 연결된 컬럼의
    데이터가 모두 존재해야만 조회됨
- 기본 구문
```sql
SELECT 컬럼1, 컬럼2, …
  FROM 테이블A
	INNER JOIN 테이블B
	ON 테이블A.컬럼 = 테이블B.컬럼
 WHERE 조건절;
```
- 예시
```sql
select a.userid, a.name, a.birthyear, a.addr, a.mobile1, a.mobile2,  
       b.prodName, b.price, b.amount
from usertbl a
 inner join buytbl b
 on a.userid = b.userid;
```
### OUTER JOIN
- 조인의 조건에 만족되지 않은 행까지 포함
- 기준이 되는 테이블A가 왼쪽
    - LEFT JOIN : 왼쪽 테이블 데이터 모두 출력
    - RIGHT JOIN : 오른쪽 테이블 데이터 모두 출력
- 기본 구문
```sql
SELECT 컬럼1, 컬럼2, …
  FROM 테이블A
	LEFT | RIGHT [OUTER] JOIN 테이블B
	ON 테이블A.컬럼 = 테이블B.컬럼
 WHERE 조건절;
```
- 예제
```sql
select a.userid, a.name, a.birthyear, a.addr, a.mobile1, a.mobile2,  
       b.prodName, b.price, b.amount
from usertbl a
 left join buytbl b
 on a.userid = b.userid;
 ```
### CROSS JOIN
- 한쪽 테이블의 모든 행들과 다른쪽 테이블의 모든 행을 조인
- CROSS JOIN 결과는 두 테이블 개수를 곱한 개수임
- 카티션곱 (Cartesian Product) 이라고도 함
- 기본 구문
```sql
SELECT *
  FROM 테이블A
	CROSS JOIN 테이블B
WHERE 조건절;
```
### SELF JOIN
- 자기 자신의 테이블과 자기 자신의 테이블 조인
- SELF JOIN의 대표적인 예는 조직도 테이블임
- 보통 상위정보 필드가 함께 포함되어 있는 경우 사용
- 샘플 코드
```sql
SELECT A.empid '사원id', A.empname '사원명', A.emptel '사원전화번호', 		 			 B.empid '부서장id', B.empname '부서장 성명', B.emptel '부서장 전화번호'     
  FROM empTBL A
	INNER JOIN empTBL B
	ON A.managerid = B.empid
WHERE A.empid = '204';
```

### UNION / UNION ALL
- 두 쿼리의 결과를 행으로 합치는 명령어
- UNION : 중복 ROW 제거하고 합함
```sql
select userid, name from usertbl
union
select empid, empname from emptbl;
```
- UNION ALL : 중복 ROW 제거 없이 모든 ROW 합함
```sql
select userid, name from usertbl
union all
select empid, empname from emptbl;
```

### IN / NOT IN
- IN : 데이터 포함 행 조회
```sql
select *
from usertbl u 
where addr in ('서울', '경기');
```
- NOT IN : 데이터 포함하지 않은 행 조회
```sql
select *
from usertbl u 
where addr not in ('서울', '경기');
```

### INLINE VIEW
- SQL문으로 뷰 생성 없이 FROM절에 사용하여 뷰와 동일한 역할 수행
- 기본 구문
```sql
SELECT A.컬럼1, A.컬럼2, …
  FROM (SELECT 컬럼1, 컬럼2. … FROM 테이블명 WHERE 조건절) A;
```
- WITH절 문장으로 변경
```sql
WITH A(컬럼1, 컬럼2)
As
( SELECT 컬럼1, 컬럼2. … FROM 테이블명 WHERE 조건절 )
SELECT A.컬럼1, A.컬럼2 FROM A;
```
## 04. SQL프로그래밍

### 스토어드 프로시저 프로그램 
- 분기문, 제어문, 반복문 등 기본적인 프로그램 기능 제공
```sql
DELIMITER $$
CREATE PROCEDURE 스토어드 프로시저 명( IN | OUT 파라미터)
BEGIN
	SQL 프로그램 코딩 영역;
END $$
DELIMITER ;

CALL 스토어드 프로시저 명();
```
- `$$ ~ $$` 까지 스토어드 프로시저 영역임을 표현 : $$는 다른 문자로 변경 가능

### 분기문 (IF 문)
```sql
IF <부울 표현식> THEN
	SQL 문장들1;
ELSEIF <부울 표현식> THEN
	SQL 문장들2;
ELSE
	SQL 문장들3;
END IF;
```
### 분기문 (CASE 문)
```sql
CASE
	WHEN <부울 표현식> THEN
		SQL 문장들1;
	WHEN <부울 표현식> THEN
		SQL 문장들2;
	ELSE
		SQL 문장들3;
END CASE;
```
- SELECT 문에서 컬럼의 데이터 조건별로 처리할 경우 많이 사용

### 반복문 (WHILE 문)
```sql
WHILE <부울 표현식> DO
	SQL 문장들;
END WHILE;
```

### WHILE ITERATE / LEAVE 구문
- ITERATE : 이후 문장 수행 없이 반복 수행 => 파이썬 CONTINUE
- LEAVE : WHILE 문 종료 => 파이썬 BREAK
- WHILE문의 이름을 정해 뒤에 붙임

### 오류 처리
```sql
DECLARE 액션 HANDLER FOR 오류조건 처리문장;
```
- 액션 : 오류 발생시 프로그램 진행 여부 결정
    - CONTINUE : DECLARE문의 처리문장 수행
    - EXIT : 프로그램 종료

- 오류조건 : 어떤 종류의 오류를 처리할 것인지 정의
    - SQLEXCEPTION : 대부분의 발생 오류
    - SQLWARNING : 경고 메시지
    - NOT FOUND : 커서나 SELECT ∙ ∙ ∙ INTO 시 데이터 없는 경우 발생 오류
- 처리 문장
    ∙ 처리 문장이 여러 개일 경우 예)
    ```sql
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
	    SHOW ERRORS;
	    ROLLBACK;
        SQL 문장들;
    END;
    ```
    - SHOW ERRORS : 오류 코드 및 메시지 출력
    - ROLLBACK : 트랜젝션 취소

### 동적 SQL
- 쿼리문장을 변수에 담아 실행함
- 쿼리문장 내 조건값 등을 동적으로 할당 가능함
```sql
PREPARE 쿼리문변수 FROM ‘SQL 쿼리문’;-- 쿼리문 생성
EXECUTE 쿼리문변수;-- 쿼리문 실행
DEALLOCATE PREPARE 쿼리문변수;-- 쿼리문 삭제
```