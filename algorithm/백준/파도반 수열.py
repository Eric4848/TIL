arrays = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    arrays.append(arrays[-1]+arrays[-5])
for _ in range(int(input())):
    print(arrays[int(input())])
