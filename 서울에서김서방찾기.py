def solution(seoul):
    num ="".join([str(i) for i in range(len(seoul)) if seoul[i] == "Kim"])
    answer = f"김서방은 {num}에 있다"
    return answer

# 통과!


# 다른사람풀이

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))