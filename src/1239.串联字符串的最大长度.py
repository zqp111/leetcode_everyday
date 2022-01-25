#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#

# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        masks = [0]
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")
                if ((mask >> idx) & 1):   # // 若 mask 已有 ch，则说明 s 含有重复字母，无法构成可行解
                    mask = 0
                    break
                mask |= 1 << idx   # 将 ch 加入 mask 中
            if mask == 0:
                continue
            
            n = len(masks)
            for i in range(n):
                m = masks[i]
                if (m & mask) == 0:   # m 和 mask 无公共元素
                    masks.append(m | mask)
                    ans = max(ans, bin(m | mask).count("1"))
        
        return ans
# @lc code=end

