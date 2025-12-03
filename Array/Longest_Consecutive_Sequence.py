class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Use a set for O(1) lookups. 
        # It's cleaner than a dict where values are just '1'
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # 2. Check if 'n' is the start of a sequence
            # We do this by checking if (n-1) is NOT in the set
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                
                # 3. Update max length
                longest = max(length, longest)
                
        return longest
