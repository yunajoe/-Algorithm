def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        mid = len(s) // 2
        answer = answer + s[mid]
    else:
        mid = len(s) // 2
        answer = answer + s[mid-1:mid+1]

    return answer

# 통과!

# 다른사람풀이

def solution(s):
    answer = ''
    start = (len(s) -1) //2
    end = (len(s) // 2) + 1
    answer = s[start:end]
    return answer