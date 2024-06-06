from collections import deque


# 변경 함수
def change(a, b):
    q = deque([(a, 0)])   # deque에 시작 소수, 변경 횟수 0 추가
    is_visit = [False] * 10000   # 방문 여부를 idx번호 9999까지 False처리
    is_visit[a] = True   # 시작 소수 방문처리
    while q:   # bfs 진행
        now, cnt = q.popleft()   # 현재 소수, 변경 횟수
        # 확인
        if now == b:   # 목표 소수까지 변경되었다면
            return cnt   # 횟수를 반환

        strNow = str(now)   # 현재 소수를 문자열로 변경
        for i in range(4):   # 4자리별로
            for j in range(10):   # 0~9까지로
                if i == j == 0:   # 첫자리가 0이라면
                    continue   # 넘어간다
                nxt = int(strNow[:i] + str(j) + strNow[i+1:])   # 하나 변경한 수
                if primes[nxt] and not is_visit[nxt]:   # 변경한 수가 소수고 방문하지 않았다면
                    q.append((nxt, cnt + 1))   # 바꾼 소수와 변경횟수 + 1 저장
                    is_visit[nxt] = True   # 해당 소수 방문처리
    return 'Impossible'   # bfs 종료시 Impossible 반환


# 소수 선정
primes = [True] * 10000   # 9999번 idx까지 True로 초기화
primes[0] = False   # 0과
primes[1] = False   # 1을 소수 아님 처리
for i in range(2, 100):   # 2부터 10000의 루트(100)까지
    if primes[i]:   # 소수이면
        for j in range(i ** 2, 10000, i):   # 그 제곱부터 9999까지 자신 간격으로
            primes[j] = False   # 소수가 아니다
# 테스트 케이스별 출력
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(change(A, B))
