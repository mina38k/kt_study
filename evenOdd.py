def solution(num_list):
    a=0
    b=0
    for i in num_list:
        if i % 2==0:
            a+=1
        else:
            b+=1
    answer = [a,b]
    return answer

print(solution([1,2,3,4,5]))