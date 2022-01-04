class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        a1 = 0
        a2 = 1
        for i in range(n-1):
            tmp = int((a1 + a2)%(1e9+7))
            a1 = a2
            a2 = tmp

        return tmp