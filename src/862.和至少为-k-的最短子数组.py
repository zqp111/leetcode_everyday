#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#

# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        
        ans, q = float('inf'), deque() # q中存储格式：(i, sum_i)
        for i, sum_i in enumerate(preSum):

            # 将deque末尾比sum_i大的值都pop，保持递增的deque
            # 前面的sum都被sum_i小，才能保证将sum_i有的比
            while q and sum_i <= q[-1][1]:
                q.pop()

            # 如果有能符合条件的，那么肯定是deque中第一个和最后一个
            # 如果符合就把第一个扔掉，找到第一个不符合的，那么就是距离最近的
            while q and sum_i - q[0][1] >= k:
                ans = min(ans, i - q.popleft()[0])

            q.append((i, sum_i))

        return ans if ans != float('inf') else -1

# @lc code=end

