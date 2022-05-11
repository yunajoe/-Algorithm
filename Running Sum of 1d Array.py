class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = []
        for i in range(len(nums)):
            total.append(sum(nums[:i+1]))
            
        return total
        
# 다른사람풀이

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
        return nums
            
                
                