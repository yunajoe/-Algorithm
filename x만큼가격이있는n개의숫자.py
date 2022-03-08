# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴

def solution(x, n):
    answer = []
    if x>=0:
        for i in range(x,(x*n)+1,x):
            answer.append(i)
    else:
        for i in range(x,(x*n)-1,x):
            answer.append(i)
    return answer

# 정확성: 92.9  왜지?

def solution(x, n):
    answer = []    
    for i in range(1,n+1):
        answer.append(i*x)
    return answer


def solution(x,n):
    answer = [i * x for i in range(1, n+1)]
    return answer 

