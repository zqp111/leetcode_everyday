#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ## dp
        # N = len(A)

        # ans = cur = None
        # for x in A:
        #     cur = x + max(cur, 0)
        #     ans = max(ans, cur)

        # # ans is the answer for 1-interval subarrays.
        # # Now, let's consider all 2-interval subarrays.
        # # For each i, we want to know
        # # the maximum of sum(A[j:]) with j >= i+2

        # # rightsums[i] = sum(A[i:])
        # rightsums = [None] * N
        # rightsums[-1] = A[-1]
        # for i in xrange(N-2, -1, -1):
        #     rightsums[i] = rightsums[i+1] + A[i]

        # # maxright[i] = max_{j >= i} rightsums[j]
        # maxright = [None] * N
        # maxright[-1] = rightsums[-1]
        # for i in xrange(N-2, -1, -1):
        #     maxright[i] = max(maxright[i+1], rightsums[i])

        # leftsum = 0
        # for i in xrange(N-2):
        #     leftsum += A[i]
        #     ans = max(ans, leftsum + maxright[i+2])
        # return ans

        ## PreSum
        # N = len(nums)

        # # Compute P[j] = sum(B[:j]) for the fixed array B = A+A
        # P = [0]
        # for _ in range(2):
        #     for x in nums:
        #         P.append(P[-1] + x)

        # # Want largest P[j] - P[i] with 1 <= j-i <= N
        # # For each j, want smallest P[i] with i >= j-N
        # ans = nums[0]
        # deque = collections.deque([0]) # i's, increasing by P[i]
        # for j in range(1, len(P)):
        #     # If the smallest i is too small, remove it.
        #     if deque[0] < j-N:
        #         deque.popleft()

        #     # The optimal i is deque[0], for cand. answer P[j] - P[i].
        #     ans = max(ans, P[j] - P[deque[0]])

        #     # Remove any i1's with P[i2] <= P[i1].
        #     while deque and P[j] <= P[deque[-1]]:
        #         deque.pop()

        #     deque.append(j)

        # return ans

        ## dp
        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for a in nums:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum

# @lc code=end

