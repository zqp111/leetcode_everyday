#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        n=len(points)
        ret=0
        for i in range(n-1):
            x=collections.defaultdict(int)
            if ret>=n-i:
                break
            for j in range(i+1,n):
                dy,dx=points[j][1]-points[i][1],points[j][0]-points[i][0]
                g=gcd(dy,dx)
                if dx==0:
                    k=1<<15
                elif dy==0:
                    k=1
                else:
                    dy,dx=dy//g,dx//g
                    k=(dy<<15)+dx
                x[k]+=1
            ret=max(ret,max(x.values()))
        return ret+1
# @lc code=end

