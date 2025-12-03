class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram( s: str, t: str) -> bool:
            if len(s)!=len(t):
                return False
            for i in s:
                if i in t:
                    t="".join(t.rsplit(i, 1))
                else :
                    return False
            else:
                return True
        
        R_list=[[strs[0]]]
        strs=strs[1:]
        for i in strs:
            for j in range(len(R_list)):
                if isAnagram(i,R_list[j][0]):
                    R_list[j]+=[i]
                    break
            else:
                R_list+=[[i]]
        return R_list

        
