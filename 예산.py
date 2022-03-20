def solution(d, budget):
    num = len(d)-1
    i = 0
    answer = 0
    if sum(d) == budget:
        return len(d)
    else:
        while i == num:
            if d[i:num] == budget:
                answer = answer + 1
                i = i + 1
        return answer


# 실패! 17.4 %


# 다른 사람 풀이 1
def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        budget = budget - i
        if budget <0:
            break
        else:
            answer = answer + 1
    return answer



# 다른 사람 풀이 2
def solution(d, budget):
    answer = 0
    total = 0
    d.sort()

    for i in range(len(d)):
        total = total + d[i]
        if total > budget:
            break
        else:
            answer = answer + 1
    return answer


def solution(d, budget):
    d.sort() # [1,2,3,4,5]
    # while 문은 True일 경우 시행이 되고, False면 멈춘다.
    while budget < sum(d): # budget이 d의 합보다 작으면 True
        d.pop() # list.pop() 은 list의 맨 마지막 index를 제거해준다.
    else:
        return len(d)





