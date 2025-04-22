def solution(my_string):
    answer = []
    for char in my_string:
        if char.isdigit():
            answer.append(int(char))
    answer.sort()
    return answer

print(solution("hi12392"))
print(solution("p2o4i8gj2"))