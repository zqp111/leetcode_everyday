class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        zeros = 0
        while nums[0] == 0:
            zeros += 1
            nums.pop(0)
    
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == last: return False
            zeros -= (nums[i] - last-1)
            if zeros <0: return False
            last = nums[i]
        return True
