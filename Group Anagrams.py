class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:         
        value = []     
        for word in strs:
            new = "".join(sorted(word))
            value.append(new)   
       # print(value)  # ['aet', 'aet', 'ant', 'aet', 'ant', 'abt']      
        dic = {}
        for v in range(len(value)):
            dic[strs[v]] = value[v]  
            
        flipped = {}
        for key, value in dic.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)
        answer = []        
        for x, y in flipped.items():
            answer.append(y)
        return answer
                
# 53 / 115 test cases passe
'''

input >> ["",""]
output >> [[""]]
expected>> [["",""]]
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        flipped = {}
        for word in strs:
            words = "".join(sorted(word))
            if words not in flipped:
                flipped[words] = [word]
            else:
                flipped[words].append(word)
                
        answer= []
        for v in flipped.values():
            answer.append(v)
        return answer
       
                
                
                
        
                
        

        
       
  
        
        
    
            
    
    
        
       
            
        
            
        
                
        
            

            
            
        
        
        




# 106 / 115 test cases passed.