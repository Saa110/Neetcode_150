class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp=1
        prefix=[]
        for i in range(len(nums)):
            prefix+=[temp]
            temp*=nums[i]
        suffix=[]
        temp=1
        for i in range(len(nums)-1,-1,-1):
            suffix=[temp]+suffix
            temp*=nums[i]
        rtr_list=[]
        #print(suffix,"/n",prefix)
        for i in range(len(nums)):
            rtr_list.append(suffix[i]*prefix[i])
        return rtr_list
