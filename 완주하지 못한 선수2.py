def solution(participant, completion):
    dic = {}
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] = dic[p] + 1

    for c in completion:
        if c in dic:
            dic[c] = dic[c]-1

    for k, v in dic.items():
        if v != 0:
            return k

# 통과!

# 다른 사람풀이


import collections

def solution(participant, completion):
    dic1 = collections.Counter(participant)
    dic2 = collections.Counter(completion)
    answer = dic1 - dic2
    return "".join(list(answer.keys()))