class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = len(nums) // 2
        answer= [i for i in nums if nums.count(i) > freq]
        answer2 = list(set(answer))
        final = int("".join(map(str, answer2)))
        return final

# 41 / 43 test cases passed.


from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = len(nums)//2
        a = Counter(nums)
        for i, v in a.items():
            if v > freq:
                return i
# 성공!

# 다른 사람풀이

class Solution:
    def majorityElement(self, nums):
        counts =Counter(nums)
        return max(counts.keys(), key=counts.get)
    # max(counts.keys(), key=lambda x: counts[x])


