from collections import deque

S = int(input())

q = deque([[1, 0, 0]])  # 화면의 이모티콘 개수, 클립보드 이모티콘 개수, 연산 횟수

is_visited = [[False] * (S+2) for _ in range(S+2)]   # 화면의 갯수, 클립보드의 갯수별로 방문여부를 0으로 초기화
is_visited[1][0] = True   # 1개 출력, 클립보드 없음을 방문처리

while q:
    smiles, clips, time = q.popleft()

    if smiles == S:  # 만약 스크린의 개수와 S가 동일하다면
        print(time)  # 걸린 횟수를 출력 후
        break  # 탈출

    for i in range(3):  # 연산을 3번 수행한다.

        # 화면에 있는 이모티콘을 복사해서 클립보드에 저장
        if i == 0:
            new_clips, new_smiles = smiles, smiles

        # 화면에 클립보드에 있는 이모티콘 들을 추가
        elif i == 1:
            new_smiles, new_clips = smiles + clips, clips

        # 화면에 있는 이모티콘 개수 한개 빼기
        else:
            new_smiles, new_clips = smiles - 1, clips

        # 만약 새로 계산된 이모티콘과 클립보드의 개수가 범위를 벗어나거나 이미 방문한 적이 있다면 continue
        if new_smiles >= S+2 or new_smiles < 0 or new_clips >= S+2 or new_clips < 0 or is_visited[new_smiles][new_clips]:
            continue

        # 방문처리 후 연산 횟수를 +1 하여 큐에 추가
        is_visited[new_smiles][new_clips] = True
        q.append([new_smiles, new_clips, time + 1])


# 오답
# S = int(input())
# dp = [i for i in range(S+2)]
# dp[1] = 0
# for i in range(3, S+1):
#     dp[i] = min(dp[i], dp[i+1])
#
#     if i % 2 == 0:
#         dp[i] = min(dp[i // 2] + 2, dp[i])
#
#     jump = 2
#     for j in range(2*i, S+2, i):
#         dp[j] = min(dp[i] + jump, dp[j])
#         jump += 1
#
# print(dp[S])

# 메모리 초과
# from collections import deque
#
# S = int(input())
# q = deque([(0, 1, 0)])
# while q:
#     time, smiles, clips = q.popleft()
#     if smiles == S:
#         print(time)
#         break
#
#     q.append((time+1, smiles, smiles))
#
#     q.append((time+1, smiles + clips, clips))
#
#     q.append((time+1, smiles - 1, clips))
#
