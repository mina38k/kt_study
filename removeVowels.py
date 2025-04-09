def solution(my_string):
    anwer=''
    for char in my_string:
        if char not in "aeiou":
            anwer += char
    return anwer
print(solution("bus"))
print(solution("nice to meet you"))