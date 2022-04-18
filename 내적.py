def solution(a, b):
    result = list(zip(a,b))
    answer = []
    for i in result:
        each = i[0] * i[1]
        answer.append(each)
    return sum(answer)

# 다른사람 풀이 1


def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])



