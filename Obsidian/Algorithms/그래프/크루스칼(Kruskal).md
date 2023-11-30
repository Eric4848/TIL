> 가중치의 합이 최소가 되는 신장(스패닝) 트리
> 최소 신장 트리 문제 중 간선이 적을 때 유리

## 1. 과정
1. 간선을 가중치 오름차순으로 정렬
2. 순환이 형성되지 않도록 선택해 나간다
	1.  서로소 집합을 이용해 구분
	2. Union & Find 방식
		1. 각자를 부모로 설정
		2. 두 노드의 부모 노드 찾기(Find)
		3. 두 노드를 합칠 때 작은 쪽 노드를 부모로 설정(Union)
		4. 큰 노드의 부모를 작은 쪽 노드로 변경 (Union)
3. 모든 노드들이 연결되면(노드의 갯수 -  1만큼 연결하면) 최솟값이다 


## 2. 문법
#### 1. Union & Find
```python
def find(x):  
    if x != computers[x]:  # 부모노드가 자기가 아닌경우
        computers[x] = find(computers[x])  # 부모의 부모노드를 검색하여 저장
    return computers[x]  # 부모노드를 반환
  
  
def union(x, y):
	# 부모 노드를 찾는다
    x = find(x)
    y = find(y)  
    # 작은 쪽을 부모노드를 설정한다
    if x < y:
        computers[y] = x  
    else:  
        computers[x] = y
```
#### 2. 크루스칼(Kruskal)
```python
while cnt != N:  # N == 노드의 갯수
    a, b, c = lines.pop()  # 간선들은 내림차순으로 정렬(pop은 우측부터)
    if find(a) == find(b):  # 두 부모노드가 같은 경우
        continue  # 순환이 생기므로 넘어간다
    union(a, b)  
    answer += c  
    cnt += 1  
print(answer)
```
## 3. 시간 복잡도
$$O(nlogn) = O(ElogE)$$
