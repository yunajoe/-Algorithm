# 처음시도..ㅎ

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            ones = mat[i].count(1)
            res.append(ones) 
            
        answer = []
        new_res = sorted(res)        
        for value in new_res:
            i = res.index(value)
            answer.append(i)
        
        if len(answer) != len(list(set(answer))):
            for i in range(len(answer)-1):
                if answer[i] == answer[i+1]:
                    answer.pop(i+1)
                    print(answer)


# 다른풀이 

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]: 
        answer = []
        for x in sorted([(i, row) for i, row in enumerate(mat)], key=lambda x: (sum(x[1]), x[0])):
                        answer.append(x[0])
        return answer[:k]



# 다른풀이 보고 조금 변형 ㅎ

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            ones = mat[i].count(1)
            res.append(ones)
        
        new = sorted((i,r) for i, r in enumerate(res))
        new.sort(key=lambda x: x[1])
        answer = []
        for i in new:
            answer.append(i[0])
        return answer[:k]