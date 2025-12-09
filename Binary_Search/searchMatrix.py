class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        if not nums:
            return False
        l=0
        quanta=len(nums[0])
        r=len(nums)*quanta
        mid=int(l/2+r/2)
        while (l<r):
            if nums[mid//quanta][mid%quanta]==target:
                return True
            elif nums[mid//quanta][mid%quanta]>target:
                r=mid
            else:
                l=mid+1
            mid =int(l/2+r/2)
        return False
        
