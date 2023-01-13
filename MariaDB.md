## 기본 명령문
Databse 조회
```sql
SHOW DATABASES;
```

Databse 선택
```sql
USE 데이터베이스명;
```

TABLE 조회
```sql
SHOW TABLES;
SHOW TABLES STATUS;
```

TABLE 구조 조회
```sql
DESC | DESCRIBE 테이블명;
```

## DML
>Data Manpulation Language. 테이블을 대상으로 하며, 테이블이 정의되어 있어야 한다. 결과를 임시로 저장하여 중간에 rollback이 가능하다.   

1. SELECT   
```sql
SElECT 조회 표현식
[FROM] (뷰)테이블명
[WHERE] 조회 조건
[GROUP BY] 
[HAVING] 
[ORDER BY] 정렬
[LIMIT] 검색 개수
```   

SELECT 표현식   

```sql
-- 테이블 컬럼 전체 조회
SElECT * 
```

```sql
-- 테이블 특정 컬럼 조회
SElECT 컬럼명, ... 
```

```sql
-- 특정 컬럼 별칭 사용 AS는 생략 가능
SElECT 컬럼명1, [AS] 별칭1, ...
```

```sql
-- 중복 삭제 데이터 조회
SElECT DISTINCT 컬럼명 
```
FROM (뷰)테이블명

```sql
-- 현제 선택된 DATABASE의 테이블 사용
SElECT * 
FROM (뷰)테이블명 
```

```sql
-- 특정 DATABASE의 테이블 사용
SElECT * 
FROM 데이터베이스명.(뷰)테이블명 
```

2. INSERT   
3. UPDATE   
4. DELETE   

## DDL

>Data Definition Language. 데이터베이스의 객체를 관리하는 언어. 바로 적용돼서 Rollback이 불가능하다.   

1. CREATE   
2. ALTER   
3. DROP   

## DCL

>Data Control Language. 사용자에게 권한을 부여한다.   

1. GRANT    
2. REVOKE

## TCL

>Transactin Control Language. 데이터 변경내용을 DBMS에 반영, 취소한다. 트랜잭션 단위로 처리한다.

1. COMMIT   
2. ROLLBACK   


