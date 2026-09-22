class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        "Finding Prefixes of s in words"
        "Finding combinations"
        counts = 0
        n = 0

        for char in words:
            if s.startswith(char):
                counts +=1
            n = 1

        return counts
       
r = Solution()
print(r.countPrefixes(["a","b","c","ab","bc","abc"],"abc"))