import sys

input = sys.stdin.readline
N = int(input())
graphs = [[] for _ in range(N)]   # 간선을 저장할 리스트
is_early = [0 for _ in range(N)]   # 얼리어답터인 사람을 초기화
# 간선 저장
for _ in range(N-1):
    u, v = map(int, input().split())
    graphs[u-1].append(v-1)
    graphs[v-1].append(u-1)

leaves = []   # 말단(연결된 간선이 1개 = 필요한 얼리어답터가 1명)인 사람들을 담을 리스트
for i in range(len(graphs)):
    if len(graphs[i]) == 1:
        leaves.append(i)

# 얼리어답터 계산
while leaves:
    leaf = leaves.pop()   # 필요한 얼리어답터가 1명인 사람
    for early in graphs[leaf]:   # 얼리어답터 계산 후 삭제하므로 for문 사용하여 얼리어답터인 사람 결정
        for link in graphs[early]:   # 얼리어답터와 친구인 사람들마다
            graphs[link].remove(early)   # 얼리어답터인 친구를 제거(이미 얼리어답터이므로 얼리어답터 영향X)
            if len(graphs[link]) == 1:   # 필요한 얼리어답터가 1명이라면
                leaves.append(link)   # 리스트에 추가
        is_early[early] = 1   # 얼리어답터인 사람 저장
        graphs[early] = []   # 얼리어답터와 연결된 리스트 비움(얼리어답터가 말단이 되는 경우 제외)

print(sum(is_early))
