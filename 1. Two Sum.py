class Solution:
    def twoSum(self, nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
ans=Solution()
a=ans.twoSum([3,2,4],7)
print(a)
