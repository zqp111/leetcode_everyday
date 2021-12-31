class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return [-1, -1]

        if (len(nums) == 1)  and (nums[0] == target): # 是否需要
            return [0, 0]
        
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1 
            elif nums[mid] > target:
                r = mid
            else:
                break
        # print(l, mid, r)
        if (l == r) and (nums[l] == target):
            return [l, r]
        if l >= r:
            return [-1, -1]
        
        if nums[l] != target:
            mid_tmp = mid
            while l < mid_tmp:
                
                l_mid = (l + mid_tmp) // 2
                if nums[l_mid] < target:
                    l = l_mid+1
                else:
                    mid_tmp = l_mid
                print('l: ', l)

        if nums[r] != target:
            mid_tmp = mid
            while r > mid_tmp:
                
                r_mid = (r + mid_tmp) // 2
                if nums[r_mid] > target:
                    r = r_mid - 1
                else:
                    mid_tmp = r_mid
                if r - mid_tmp == 1:
                    if nums[r] == target:
                        break
                    else:
                        r -= 1
                        break
                    # r = r-1
                # print('r: ', r)

        return r-l+1