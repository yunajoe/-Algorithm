import heapq as hp

def solution(scoville, K):
    cnt = 0
    while True:
        first = hp.heappop(scoville)
        second =hp.heappop(scoville)
        new = first + second * 2
        hp.heappush(scoville, new)
        cnt = cnt + 1
        for i in scoville:
            if i < K:
                first = hp.heappop(scoville)
                second =hp.heappop(scoville)
                new = first + second * 2
                hp.heappush(scoville, new)
                cnt = cnt + 1
            else:
                pass
        else:
            break
    return cnt
# 14.3 / 100.0


# 다른사람풀이
from heapq import heappush, heappop
def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        else:
            a = heappop(scoville)
            b = heappop(scoville)
            heappush(scoville, a+b*2)
            answer += 1
    if scoville[0] < K:  # while 문이 다 끝난다음에 시행된다. 리스트안에 모든 것들이 heappush이루어지면 1개의 원소가 남는다.
        return -1
    else:
        return answer


















