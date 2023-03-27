def solution(prices):
    answer = [0 for _ in prices]
    for idx, price in enumerate(prices):
        if idx == len(prices) - 1:
            break
        for future in range(idx + 1, len(prices)):
            answer[idx] += 1
            if prices[future] < price:
                break
    return answer


print(solution([1, 2, 3, 2, 3]))
