from functools import cmp_to_key


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(num1, num2): 
            if num1+num2 < num2+num1:
                return -1
            elif num1+num2 > num2+num1:
                return 1
            else:
                return 0
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp))
        return ''.join(nums)