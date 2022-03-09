def solution(phone_number):
    answer = ''
    last = phone_number[-4:] # -4부터 끝까지.. 
    first = phone_number[:-4]  # 처음부터 -5까지.. 
    first = len(first)*"*"    
    answer = first + last    
    return answer

# 통과!! 

### 다른 사람 풀이 ### 

def solution(phone_number):
    answer = ''
    last = phone_number[-4:]
    first = (len(phone_number) - 4) * "*"
    answer = first + last
    return answer

