class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # target이 있는지 없는데 확인
        if target in nums:
            return nums.index(target)
        nums.append(target)
        answer = sorted(nums)
        return answer.index(target)

