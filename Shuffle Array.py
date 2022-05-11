class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]: 
        first = nums[:n]
        second = nums[n:]
        answer = []
        for i in range(len(first)):
            each = [first[i],",",second[i]]
            vars = "".join([str(_) for _ in each])
            answer.append(vars)
        return answer




   
        
        
        