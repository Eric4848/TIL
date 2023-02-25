# Map

>

- 각 요소에 동일한 처리를 진행해준다
- map(a, b)
  - 모든 b값들에 a라는 것을 실행한다

ex)

```python
map(int, lista)
```

- lista의 모든 요소에 int()를 실행한다

# Function

>

```python
def add(a, b):
    return a + b
```

- add -> 이름
  - 이름이므로 내용에 해당하는 주소를 저장
- (a, b):  
   return a + b -> 값

# 익명 값

>

- 값을 저장하지 않고 필요할 때만 사용  
  ex)

```python
print(1)
```

- 1은 저장되지 않고 출력 후 사라진다

# 익명 함수 lambda

>

- 익명 값과 마찬가지로 저장하지 않고 필요할 때만 사용
  ex)

```python
print(a.sort(key=lambda x: x[1]))
```

- a리스트에서 리스트 첫 요소별로 그 요소의 두번째 값을 기준으로 sort
- lambda는 사용하고 사라진다

lambda x: x...

- lambda 뒤의 x -> 입력값
- : 뒤 -> 함수 내용

# ToDo

>

1. 정렬 알고리즘
2. MST
