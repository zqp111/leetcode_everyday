#
# @lc app=leetcode.cn id=2121 lang=python3
#
# [2121] 相同元素的间隔之和
#

# @lc code=start
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n   # 每个元素与相同元素间隔之和
        total = defaultdict(int)   # 每个数值出现下标之和
        cnt = defaultdict(int)   # 每个数值出现次数
        # 正向遍历并更新两个哈希表以及间隔之和数组
        for i in range(n):
            val = arr[i]
            if val in cnt:
                res[i] += i * cnt[val] - total[val]
            total[val] += i
            cnt[val] += 1
        # 清空哈希表，反向遍历并更新两个哈希表以及间隔之和数组
        total.clear()
        cnt.clear()
        for i in range(n - 1, -1, -1):
            val = arr[i]
            if val in cnt:
                res[i] += total[val] - i * cnt[val] 
            total[val] += i
            cnt[val] += 1
        return res
# @lc code=end

