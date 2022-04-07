from itertools import permutations

def IsPrime(n):
    if n == 0 or n ==1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True  # 소수찾는 function

def solution(numbers):
    result = []
    for i in range(1,len(numbers)+1):
        a = list(permutations(numbers,i))
        per = list(map("".join, a))
        for p in list(set(per)):
            if IsPrime(int(p)):
                result.append(int(p))
    result2 = list(set(result))
    return len(result2)

# list(set(per))
'''
['0', '1']
['11', '10', '01']
['011', '101', '110']

int(p)로 바꾸면 011이 11이 되고, 01이 1이 된다.
그래서 IsPrime(int(p)) = [11,11,101]되기 떄문에 다시 set을 해줘야한다.
'''











