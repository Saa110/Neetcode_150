class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        H_map={}
        R_list=['a']*k
        for i in range(len(nums)):
            if H_map.get(nums[i])==None:
                H_map[nums[i]]=1
            else:
                H_map[nums[i]]+=1
        a=(H_map.keys())
        print(H_map)
        for i in a:
            print(i)
            for j in range(k):
                print("j=",j,"H_map=",H_map[i],"R_list=",R_list[j])
                if R_list[j]=='a' or H_map[i]>H_map[R_list[j]]:
                    R_list=R_list[0:j] +[i] +R_list[j:k-1]
                    print(R_list)
                    break
            
        return R_list
