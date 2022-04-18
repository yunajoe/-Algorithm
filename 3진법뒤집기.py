def solution(n):
    q, r = divmod(n,3)
    start = r
    answer = []
    answer.append(r)
    num_q = []
    while q >= 3:
        q,r = divmod(q,3)
        answer.append(r)
        num_q.append(q)
    final = answer+ [num_q[-1]]
    index = []
    answer = []
    for i in range(len(final)-1,-1, -1):
        index.append(final[i])
        final2 = index[::-1]
        answer.append(3**i)
    return sum([x * y for x , y in zip(final, answer)])

# 합계: 90.0 / 100.0

# 다른사람풀이

def solution(n):
    tmp = ''
    while n > 0:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer




