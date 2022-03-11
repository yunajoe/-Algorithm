def solution(s):
    c1 = (len(s) == 4)or (len(s == 6))
    c2 = s.isdigit()

    if c1 and c2:
        return True
    return False

# 정확성 62.5  실패!!

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            return True
        return False
    return False

# 성공!!


# 다른 사람 풀이
def solution(s):
    return s.isdigit() and len(s) in (4,6)

