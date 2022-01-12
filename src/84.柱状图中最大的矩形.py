#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = []
        right = [len(heights)]*len(heights)
        stack = []
        for i in range(len(heights)) :
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            if stack:
                left.append(stack[-1])
            else:
                left.append(-1)
            
            stack.append(i)
        # print(left)

        
        # stack = []
        # for i in range(len(heights)-1, -1, -1):
        #     while stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()
        #     if stack:
        #         right.insert(0, stack[-1])
        #     else:
        #         right.insert(0, len(heights))
        #     stack.append(i)
        # print(right)
        re = []
        for i in range(len(heights)):
            re.append((right[i]-left[i]-1)*heights[i])
        # print(re)
        return max(re)
# @lc code=end

