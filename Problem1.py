class Solution:
    def addTwoNumbers(self, l1 , l2):
        output = []
        caries = 0

        for i in range(len(l1)):
            for j in range(len(l2)):
                sum = l1[i] + l2[j]

                if len(sum) > 1:
                    output.append(sum[::-1])
                    caries += sum[0]

                else:
                    output.append(sum)
                carries = 0
        return output

r = Solution()
print(r.addTwoNumbers([2,4,3], [5,6,4]))