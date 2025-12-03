class Solution:
    # Prefix and Siffix Array
    def Prefix_suffix_sol(self, height: List[int]) -> int:
        suffix=[]
        prefix=[]
        temp_max=0
        for i in range(len(height)):
            suffix+=[temp_max]
            temp_max=max(height[i],temp_max)
        temp_max=0
        for i in range(len(height)-1,-1,-1):
            prefix=[temp_max]+prefix
            temp_max=max(height[i],temp_max)
        trapped_water=0
        print (suffix, "\n",prefix )
        for i in range(len(height)):
            temp_add=min(suffix[i],prefix[i])-height[i]
            if temp_add>0:

                trapped_water+= min(suffix[i],prefix[i])-height[i]
        return trapped_water

    def trap(self, height: List[int]) -> int:
        #two_pointers Solution
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        
        
    
        


        
