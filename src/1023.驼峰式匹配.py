#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#

# @lc code=start
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        return [self.IsMatch(s, pattern) for s in queries]
        
    def IsMatch(self, src: str, pattern):
        count = 0
        n = len(pattern)
        # print(src)
        for i, char in enumerate(src):
            if count >= n: return src[i:].islower()
            if char == pattern[count]:
                count += 1
            elif char.isupper():
                if char != pattern[count]:
                    return False
                count += 1
            # print(count)
        return count == n
# @lc code=end

