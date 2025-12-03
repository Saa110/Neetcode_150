class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table={}
        for i in range(len(nums)):
            if hash_table.get(nums[i])==None:
                hash_table[nums[i]]=[nums[i],i,0]
            else:
                hash_table[nums[i]]=[hash_table.get(nums[i])[0],hash_table.get(nums[i])[1],i]
        for i in range(len(nums)):
            if hash_table.get(target-nums[i])!=None:
                if hash_table.get(target-nums[i])[0]!=nums[i]:
                    return [i,hash_table.get(target-nums[i])[1]]
                elif hash_table.get(target-nums[i])[2]!=0:
                    return [hash_table.get(target-nums[i])[1],hash_table.get(target-nums[i])[2]]
        else:
            return -1

        
