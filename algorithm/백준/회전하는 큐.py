from collections import deque

total, num = map(int, input().split())
targets = list(map(int, input().split()))

queue = deque([i for i in range(1, total + 1)])
move = 0

for target in targets:
    while True:
        if target == queue[0]:
            queue.popleft()
            break

        if queue.index(target) <= len(queue) // 2:
            while target != queue[0]:
                queue.append(queue.popleft())
                move += 1

        else:
            while target != queue[0]:
                queue.appendleft(queue.pop())
                move += 1

print(move)
