def solution(box, n):
    a=box[0]//n
    b=box[1]//n
    c=box[2]//n
    return a*b*c

print(solution([1,1,1],1))
print(solution([10,8,6],3))