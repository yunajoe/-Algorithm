

from heapq import *
# Heap 기능을 제공하기 위한 라이브러리
# heapq.heappush() 원소를 삽입할 때
# heapq.heappop() 원소를 꺼낼 때 (항상 작은 원소를 꺼냄)

def solution(scoville, K):
    count = 0
    heapify(scoville)  # 오름차순 정렬
    while scoville[0] < K:  # scovile의 첫번째 요소가 K 보다 작을 때만 수행한다.
        num1 = heappop(scoville) #  힙 리스트에서 요소빼기...1
        num2 = heappop(scoville) #  힙 리스트에서 요소빼기...2
        heappush(scoville, num1 + num2 * 2)  # 힙 리스트에 값 추가하기
        count = count + 1
    return count if scoville[0] >= K else -1


print(solution([1, 2, 3, 9, 10, 12],7))