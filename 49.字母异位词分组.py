#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for word in strs:
            key = ''.join(sorted(word))
            if dic.get(key, None) is not None:
                dic[key].append(word)
            else:
                dic[key] = [word]
        return list(dic.values())
# @lc code=end

