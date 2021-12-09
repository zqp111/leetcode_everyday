#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        # def get_Ak(A, k_num):
        #     ans = 0
        #     pre = 0
        #     dict_items = {}
        #     k = k_num
        #     for i in range(len(A)):
        #         if A[i] not in dict_items.keys() or dict_items[A[i]]==0:
        #             dict_items[A[i]] = 1
        #             k -= 1
        #         if k < 0:
        #             j = i
        #             pre = 0
        #             while 1:
        #                 j -= 1
        #                 if A[j] == A[i]:
        #                     pre += 1
        #                 else:
        #                     k += 1
        #                     pre += 1
        #                     # ans += pre
        #                 if k_num -1 == k:
        #                     pre -= 1
        #                     # print(dict_items)
        #                     # print(A[j])
        #                     dict_items.pop(A[j])
        #                     break
        #                 ans += pre
        #         pre += 1
        #         ans += pre

        #         print(ans, k, k_num)
        #     return ans

        # a = get_Ak(A, K)
        # b = get_Ak(A, K-1)
        # print(a, b)
        # return a-b
        a = self.atMostK(A, K)
        b = self.atMostK(A, K-1)
        print(a, b)
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        counter = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if counter[A[j]] == 0:
                K -= 1
            counter[A[j]] += 1
            while K < 0:
                counter[A[i]] -= 1
                if counter[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res
            
# @lc code=end

