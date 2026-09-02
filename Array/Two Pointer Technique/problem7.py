class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        intersec =set()

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    intersec.add(nums1[i])

        return list(intersec)


r = Solution()
print(r.intersection([1,2,2,1],[2,2]))