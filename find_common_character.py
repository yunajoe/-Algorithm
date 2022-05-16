class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            ele = list(word)
            counts = dict()
            for e in ele:
                counts[e] = counts.get(e,0) + 1
            res.append(counts)
        common_pairs = dict()
        
        dic1 = res[0]
        res_dic = res[1:]
        
        for k in dic1.keys():
            for each in res_dic:
                if (k in each.keys() and dic1[k]) == each[k]:
                    common_pairs[k] = dic1[k]
        print(common_pairs)
                
# 다른 사람 풀이

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = list(words[0])
        for word in words:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check  
            
        
# 다른 사람 풀이
from collections import Counter

class Solution:    
    def commonChars(self, words: List[str]) -> List[str]:
        compare = collections.Counter(words[0])
        
        for i in range(len(words)):
            cnt = collections.Counter(words[i])
            compare = compare & cnt
            
        answer = list(compare.elements())
      
        return answer
        