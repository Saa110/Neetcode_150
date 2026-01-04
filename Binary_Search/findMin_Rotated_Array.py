class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # The left part is sorted, but the pivot is to the right
                l = mid + 1
            else:
                # The right part is sorted, min is mid or to the left
                r = mid
        return nums[l]
