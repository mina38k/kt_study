def solution(n, numlist):
    return [i for i in numlist if i % n==0]
print(solution(3,[4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution(5,[1, 9, 3, 10, 13, 5]))
print(solution(12,[2, 100, 120, 600, 12, 12]))