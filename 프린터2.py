def solution(priorities, location):
    answer = []
   # cnt = 0
    goal = priorities[location]
    new = priorities[1:]
    for x, y in zip(priorities, new):
        start = priorities[0]
        if start < y:
           # cnt = cnt + 1
            priorities.append(start)
            priorities.pop(0)
    return priorities.index(goal)+1



# 10 .. 실패!




def solution(priorities, location):
    goal = priorities[location]
    new = priorities[1:]
    pri = priorities
    cnt = 0
    if goal == max(priorities):
        return 1
    else:
        for x, y in zip(pri, new):
            start = pri[0]
            if start <= y:
                cnt += 1
                pri.append(start)
                pri.pop(0)
    return len(pri) - cnt + 1

# 20.. 실패!


# 다른 사람풀이 - 1
def solution(priorities, location):
    answer = 0
    arr = [ (v,i) for i, v in enumerate(priorities)]
     # [(2, 0), (1, 1), (3, 2), (2, 3)]
     # [(1, 0), (1, 1), (9, 2), (1, 3), (1, 4), (1, 5)]

    while len(arr) != 0:
        if arr[0][0] < max(arr)[0]:  # 첫번째가 max보다 작을때
            arr.append(arr[0]) # 첫번째를 맨 뒤에다 붙이고
            arr.pop(0)  # 첫번째를 삭제함
        else: # 첫번째가 max일떄?
            num = arr.pop(0)
            answer = answer + 1
            if num[1] == location:
                break
    return answer







