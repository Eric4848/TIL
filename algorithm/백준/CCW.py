# 외적을 이용한 문제

a = list(map(int,  input().split()))
b = list(map(int,  input().split()))
c = list(map(int,  input().split()))

D = a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - b[0] * a[1] - c[0] * b[1] - a[0] * c[1]

if D > 0:
    print(1)
elif D < 0:
    print(-1)
else:
    print(0)




# d1 = []
# d2 = []
#
# for i in range(2):
#     d1.append(b[i] - a[i])
#
# for i in range(2):
#     d2.append(c[i] - b[i])
#
#
# if d1[1] != 0 and d2[1] != 0:
#     if d1[0]/d1[1] == d2[0]/d2[1]:
#         print(0)
#
# elif d2[0] != 0 and d1[0] != 0:
#     if d1[1]/d1[0] == d2[1]/d2[0]:
#         print(0)
#
# elif d1[0] > 0:
#     if d2[1] > 0:
#         print(1)
#     else:
#         print(-1)
# else:
#     if d2[1] > 0:
#         print(-1)
#     else:
#         print(1)