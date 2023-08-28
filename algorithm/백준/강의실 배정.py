import heapq   # 힙 사용
import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort()   # 수업 시간을 시작 시간을 기준으로 정렬한 후
q = []
heapq.heappush(q, times[0][1])   # 힙에 처음 시작하는 수업의 종료 시간을 추가한다

for i in range(1, N):   # 모든 수업시간들을 돌아가며
    if q[0] <= times[i][0]:   # 가장 일찍 끝나는 수업이 현재 수업 시작 시간과 같거나 작으면
        heapq.heappop(q)   # 그 시간을 제거한다
    heapq.heappush(q, times[i][1])   # 현재 수업 종료 시간을 추가한다
print(len(q))   # 힙의 길이가 필요한 강의실 수이다
