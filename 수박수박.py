def solution(n):
    answer = ''
    if n % 2 == 0:
        q = n // 2
        answer = answer + "수박" * q
    else:
        q = n // 2
        answer = answer + ("수박" * q) + "수"
    return answer


# 다른사람풀이 최곤데?!
def water_melon(n):
    s = "수박" * n
    return s[:n]