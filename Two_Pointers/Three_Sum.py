class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        rtr_list=[]
        while l<r:
            if numbers[l]+numbers[r]==target:
                rtr_list.append([-target,numbers[l],numbers[r]])
            if numbers[l]+numbers[r]>target:
                r-=1
            else:
                l+=1
        return rtr_list
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rtr_list=[]
        nums.sort()
        for i in range(len(nums)-1):
            target=-nums[i]
            temp=self.twoSum(nums[i+1:len(nums)],target)
            if len(temp)>0:
                for j in temp:
                    if j not in rtr_list:
                        rtr_list.append(j)
        return rtr_list


        
