class Solution:
    def reverseString(self, s: list[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            
        return s

    
r  =  Solution()
print(r.reverseString(["h","e","l","l","o"]))
print(r.reverseString(["j","a","r","a","i","r"]))