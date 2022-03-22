def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == True:
            answer = answer + absolutes[i]
        else:
            answer = answer - absolutes[i]
    return answer

# 통과

# 다른사람풀이 1


def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer


# 다른사람풀이 2

def solution(absolutes, signs):
    answer = sum([a if s else -a for a, s in zip(absolutes, signs)])
    return answer