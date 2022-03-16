# price를 count번까지 피라미드식으로 계산한다.

def solution(price, money, count):
    total = 0
    for i in range(1,count+1):
        total = total + (i * price)
    if money > total:
        return 0
    return abs(money-total)


# 다른사람풀이

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

# 다른사람풀이 2

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))

# 다른사람풀이 2 보고 조금 바꿔봄

def solution(price, money, count):

    answer = max(sum([price * i for i in range(1,count+1)])-money,0)
    return answer