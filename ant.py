def solution(hp):
    return hp //5 + hp % 5//3 + hp % 5 % 3

print(solution(23))
print(solution(24))