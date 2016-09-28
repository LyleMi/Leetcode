class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums))[::-1]:
            if target - nums[i] in nums[:i]:
                return [nums.index(target - nums[i]),i]