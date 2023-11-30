> 가중치의 합이 최소가 되는 신장(스패닝) 트리
> 최소 신장 트리 문제 중 간선이 많을 때 유리 

## 1. 과정
1. 간선들을 노드별로 (가중치, 도착지) 형태로 저장
2. heap을 만들어 가중치 0과 시작정점을 저장
3. heap에서 pop한다(가중치가 가장 작은 간선)
4. 도착지가 방문한적 없다면 방문처리 하고 해당 간선의 가중치를 정답에 더한다
5. 도착지와 연결된 간선들을 heap에 추가한다(가중치별로 정렬)
6. 모든 도착지를 방문하면 종료

## 2. 문법
```python
heapq.heappush(q, (0, 1))   # 처음에 힙을 만들기 위해 가중치 0, 시작노드 설정

while q:
    weight, now = heapq.heappop(q)  # 가중치, 현재 위치(이전의 목적지)
    if not is_visited[now]:  
        is_visited[now] = True  
        answer += weight  
        for nxt_weight, nxt in lines[now]:  
            heapq.heappush(q, (nxt_weight, nxt))  
print(answer)
```

## 3. 시간 복잡도
$$O(V) * O(logV) + O(\Sigma^V_{v=1}degree(v)) = O(2E)= O(E) * O(logV)$$
$$O(VlogV + ElogV)$$
$$O(ElogV)$$
