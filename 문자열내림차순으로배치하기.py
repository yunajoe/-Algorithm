def solution(s):
    s = sorted(s, reverse = True)  # s.sort() 는 only 리스트에서만..
    s = "".join(s)
    return s

# 통과!!


# 다른사람풀이

def solution(s):
    return "".join(sorted(s, reverse=True))
