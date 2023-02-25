h, b, c, s = map(int, input().split())
total = float(h * b * c * s)
total /= 1024
total /= 1024
total /= 8
print(format(total, '.1f')+' MB')
