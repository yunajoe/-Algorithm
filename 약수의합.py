def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)
    return sum(answer)

 # 통과


 # 다른사람풀이 - 1

def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])


# 다른사람풀이 - 2

def sumDivisor(num):
    # num / 2 의 수들만 검사하기
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])


