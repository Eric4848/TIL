T = int(input())
for _ in range(T):
    n = int(input())
    arrays = [0] + list(map(int, input().split()))
    is_used = [False for _ in range(n + 1)]
    circle = 0
    queue = []

    while sum(is_used) != n:
        for i in range(1, n + 1):
            if not is_used[i]:
                is_used[i] = True
                queue.append(arrays[i])
                while queue:
                    nxt = queue.pop()
                    if not is_used[nxt]:
                        queue.append(arrays[nxt])
                        is_used[nxt] = True
                circle += 1

    print(circle)
