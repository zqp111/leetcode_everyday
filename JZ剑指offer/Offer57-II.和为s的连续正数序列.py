class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l, r = 1, 2
        result = []
        sumTmp = 3
        while r < target:
            if sumTmp < target:
                r += 1
                sumTmp += r
            elif sumTmp > target:
                sumTmp -= l
                l += 1
            else:
                result.append(list(range(l, r+1, 1)))
                sumTmp -= l
                l += 1
        return result