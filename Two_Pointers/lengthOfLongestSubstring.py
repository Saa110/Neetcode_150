class Solution:
    def my_lengthOfLongestSubstring(self, s: str) -> int:
        longest_str=""
        max_len=0
        for i in s:
            temp=longest_str.find(i)
            if temp==-1:
                longest_str+=i
                print(longest_str)
                max_len=max(max_len,len(longest_str))
            else:
                longest_str=longest_str[temp+1:]+i
        return max_len
    def Optimal_lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
    
        
