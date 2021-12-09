from math import *


A = factorial(6)
l_ = set()
nums_ = [0,1,1,2,2,2]
tmp = ''

if __name__ == '__main__':
    # def subsets(nums):
    #     N = pow(2,len(nums))
    #     ans = []
    #     for i in range(N):
    #         tmp = []
    #         idx = 0
    #         m = i
    #         print(i)
    #         while m:
    #             if m & 1:
    #                 tmp.append(nums[idx])
    #             idx += 1
    #             m = m >> 1
    #         ans.append(tmp)
    #     return ans
    
    # print(subsets([1,2]))



    def l(nums, tmp):
        a = tmp
        if len(nums) <= 1:
            a += str(nums[0])
            l_.add(int(a))
            return 
        for i in range(len(nums)):
            a += str(nums[i])
            l(nums[:i]+nums[i+1:], a)
            a = a[:-1]

    l(nums_, tmp)

    print(len(l_), l_)