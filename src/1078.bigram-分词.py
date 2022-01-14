#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()

        status = 0
        result = []
        i = 0
        while i < len(words):
            if status == 0 and words[i] == first:
                status = 1
                i += 1
            elif status == 1 :
                if words[i] == second:
                    status = 0
                    if i < len(words) - 1:
                        result.append(words[i+1])
                    # i += 1
                else:
                    status = 0
            else:
                i +=1
        return result
# @lc code=end

