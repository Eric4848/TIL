w, h, b = map(int, input().split())
total = w * h * b
total /= 1024
total /= 1024
total /= 8
print(format(total, '.2f') + ' MB')
