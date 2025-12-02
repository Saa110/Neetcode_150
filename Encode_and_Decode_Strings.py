class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: Length + Delimiter(#) + String
            # Example: "5#Hello"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Move j forward until we find the delimiter '#'
            while s[j] != "#":
                j += 1
            
            # Extract the length (everything from i to j)
            length = int(s[i:j])
            
            start_of_string = j + 1
            end_of_string = j + 1 + length
            
            # Extract the string
            res.append(s[start_of_string : end_of_string])
            
            # Move i to the start of the NEXT segment
            i = end_of_string
            
        return res
