class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        windows = []
        for i in range(k):
            while windows and nums[i] > windows[-1]:
                windows.pop(-1)
            windows.append(nums[i])
        result = [windows[0]]
        
        for i in range(k, len(nums)):
            if windows[0] == nums[i-k]:
                windows.pop(0)
            while windows and nums[i] > windows[-1]:
                windows.pop(-1)
            windows.append(nums[i])

            result.append(windows[0])

        return result