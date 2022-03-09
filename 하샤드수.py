
def solution(x):        
    num = list(str(x))   
    each_num = list(map(int, num))
    result = sum(each_num)    
    if x % result == 0:
        return True
    return False

# 통과!!! 

## 다른 사람 풀이
def solution(x):         
    result = sum([int(i) for i in str(x)])
    if x % result == 0: 
        return True 
    return False
        
