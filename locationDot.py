def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        return 4
    else:
        if dot[1] > 0:
            return 2
        return 3

print(solution([2,4]))