class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)
        mid=int(l/2+r/2)
        while (l<r):
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid
            else:
                l=mid+1
            mid =int(l/2+r/2)
        return -1
        
