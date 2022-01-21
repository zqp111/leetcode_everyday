class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        l, r = [1]*len(a), [1]*len(a)
        for i in range(1, len(a)):
            l[i]= l[i-1]*a[i-1]
            r[len(a)-1 - i] = r[len(a)- i] * a[len(a)- i]
        
        return [l[i]*r[i] for i in range(len(a))]