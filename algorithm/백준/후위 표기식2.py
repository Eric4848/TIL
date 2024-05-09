N = int(input())
calcs = input().rstrip()
nums = [int(input()) for _ in range(N)]
stack = []
for calc in calcs:
    if calc.isalpha():
        stack.append(nums[ord(calc) - 65])
    else:
        b = stack.pop()
        a = stack.pop()
        if calc == '+':
            stack.append(a + b)
        elif calc == '-':
            stack.append(a - b)
        elif calc == '*':
            stack.append(a * b)
        else:
            stack.append(a / b)
print(f'{stack[0]:.2f}')
