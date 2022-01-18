class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        self.getTopK(arr, 0, len(arr)-1, k-1)
        return arr[:k]
    
    def getTopK(self, arr, l, r, target):
        splitK = self.split(arr, l, r)
        if splitK < target:
            self.getTopK(arr, splitK+1, r, target)
        elif splitK > target:
            self.getTopK(arr, l, splitK-1, target)
        else:
            return
            
    def split(self, arr, l, r)->int:
        i = l
        for j in range(l, r):
            if arr[j] < arr[r]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i
