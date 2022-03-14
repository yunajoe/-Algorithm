def solution(num):
    answer = 0
    num2 = num
    while num2 != 1:
        if num2 % 2 == 0:
            num2 = num2 // 2
            answer = answer + 1
        else:
            num2 = (num2 * 3) + 1
            answer = answer + 1
    if answer >=500:
        return -1
    return answer

# 통과!
