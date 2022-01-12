#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        count = 0
        a = num
        re = [0]
        while a!= 0:
            a = a >> 1
            count +=1
        a = 1
        for _ in range(count-1):
            a = a << 1
            re.extend([i+1 for i in re])
        re.extend([i+1 for i in re[:num-a+1]])
        return re
        
        
# @lc code=end

