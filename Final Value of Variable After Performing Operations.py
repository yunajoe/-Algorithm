class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dic = {"--X":-1,"X--":-1, "++X":1,"X++":1}
        
        res = []
        for k, v in dic.items():
            for o in operations:
                if k == o:
                    res.append(v)
        return sum(res)
# 다른풀이 2  
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer =0 
        for i in operations:
            if i.__contains__("+"):
                answer = answer + 1
            else:
                answer = answer - 1
        return answer
                
# 다른풀이 3 
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([+1 if "+" in o else -1 for o in operations]) 



                
        