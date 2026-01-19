from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # Ensure A is the smaller array so we binary search on the smaller range
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        
        while True:
            # i is the pointer for A, j is the pointer for B
            i = (l + r) // 2 
            j = half - i - 2 # -2 handles 0-based indexing offsets
            
            # Handle Edge Cases (Out of Bounds) using Infinity
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j + 1) < len(B) else float('inf')
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd: return the min of the right side
                if total % 2:
                    return min(Aright, Bright)
                # even: return the average of max-left and min-right
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # If A's left value is too big, move pointer to the left
            elif Aleft > Bright:
                r = i - 1
            # Otherwise, move pointer to the right
            else:
                l = i + 1
