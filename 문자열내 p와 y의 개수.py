# S 문자열안에 있는 문자를 대문자 또는 소문자로 변경하자! 
# 전체문자.count("찾고싶은문자")
def solution(s):
    s = s.upper()
    P_len = s.count("P")
    Y_len = s.count("Y")
    
    if P_len == Y_len:
        return True
    return False
   
 # 통과!! 
 
 
 # 다른사람풀이 
 from collections import Counter 

def word_count(s):
    c = Counter(s.lower())
    p_len = c["p"]  # 키가 p인 value값 뽑기 
    c_len = c["y"] # 키가 y인 value값 뽑기 
    return p_len == c_len

    


        
    
