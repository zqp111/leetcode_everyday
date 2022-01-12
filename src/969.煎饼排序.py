#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

# @lc code=start
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        for i in range(len(arr), 0, -1):
            # print(i, arr)
            max_i = arr.index(i)+1
            if max_i == i:
                continue
            if max_i == 1:
                answer.append(i)
                arr[:i] = arr[i-1::-1]
            else:
                answer.append(max_i)
                arr[:max_i] = arr[max_i-1::-1]
                # print(arr)
                answer.append(i)
                arr[:i] = arr[i-1::-1]
        # print(arr)
        # print(answer)
        return answer
# @lc code=end

