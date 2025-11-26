class Solution:
    def index(self, elements, target):
        for i in range(len(elements)):
            for j in range(i+1, len(elements)):
                if (elements[j] == target - elements[i]):
                    return [i, j]


soln = Solution()
nums = [2, 7, 11, 15]
target = 17
result = soln.index(nums, target)
print(result)
