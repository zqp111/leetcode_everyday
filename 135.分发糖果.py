#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        results = [0 for _ in range(len(ratings))]

        def get_r(idx, results, ratings):
            if results[idx] > 0:
                return results[idx]
            elif idx == 0:
                if ratings[idx] > ratings[idx+1]:
                    a = get_r(idx+1, results, ratings) +1
                    results[idx] = a
                    return a
                else:
                    results[idx] = 1
                    return 1
            elif idx == len(ratings)-1:
                if ratings[idx] > ratings[idx-1]:
                    a = get_r(idx-1, results, ratings) +1
                    results[idx] = a
                    return a
                else:
                    results[idx] = 1
                    return 1
            else:
                a = 0
                b = 0
                # print(idx, '11111')
                if ratings[idx] > ratings[idx+1]:
                    a = get_r(idx+1, results, ratings)
                if ratings[idx] > ratings[idx-1]:
                    b = get_r(idx - 1, results, ratings)
                a = max(a,b)+1
                #print(idx, a)
                results[idx] = a
                return a

        for i in range(len(ratings)):
            # print(i)
            get_r(i, results, ratings)
            # print(results)
        return sum(results)

# @lc code=end

