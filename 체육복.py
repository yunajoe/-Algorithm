def solution(n, lost, reserve):
    before = [reserve[i]-1 for i in range(len(reserve))]
    after = [reserve[i]+1 for i in range(len(reserve))]
    total = before + after
    print(total)

    result = []
    for x in lost:
        if x in total:
            result.append(x)
    print(result)
    cnt = 0
    for a in lost:
        for b in result:
            if a == b:
                cnt = cnt + 1
    cal = len(lost) - cnt
    final = n - cal
    if len(lost) > len(reserve):
        return final-1
    return final

# 정확성: 65.0 실패!



# 다른 사람풀이
def solution(n, lost, reserve):
    answer = 0
    r2 = [r for r in reserve if r not in lost]
    # 여분은 있지만 안 잃어버린 사람 , 빌려줄수 있음
    l2 = [l for l in lost if l not in reserve]
    # 잃어버렸지만 여분 있는 사람.
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다 >>> 이 전제때문에 썼음.
    for i in r2:
        after = i + 1
        before = i - 1
        if after in l2:
            l2.remove(after)
        elif before in l2:
            l2.remove(before)
    return n - len(l2)


