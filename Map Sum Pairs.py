
# nsert 함수로는 k, value 형ㅇ태의 dictionary 를 만든다. 
# sum은 pefix가 시작하는 key의 value를 찾고 합을 return한다. 
class MapSum:
    def __init__(self):
        self.key = key  
        self.val = val         
        
    def insert(self, key: str, val: int) -> None:
        dic = dict(key=val)  
        

    def sum(self, prefix: str) -> int: 
        answer = 0 
        for k, v in dic.items():
            if k.startswith(prefix):
                answer = answer + v
        return answer
                
# 요렇게 하면은 name error가난당 

class MapSum:
    def __init__(self):
        self.dic = {}        # dicnary 객체 생성   

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val   # key, value 담아줌 
        

    def sum(self, prefix: str) -> int:
        answer = 0 
        for k, v in self.dic.items():
            if k.startswith(prefix):
                answer = answer + v
        return answer
                
            
# 위에꺼 조금수정 

class MapSum:
    def __init__(self):
        self.dic = {}          

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val
        

    def sum(self, prefix: str) -> int:
        return sum([v for k, v in self.dic.items() if k.startswith(prefix)])
        
