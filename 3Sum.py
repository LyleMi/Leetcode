class Solution(object):

    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in xrange(len(nums) - 1):
            if i == 0 or (i > 0 and (nums[i] != nums[i-1])):
                front = i + 1
                back = len(nums) - 1
                target = -nums[i]
                while front < back:
                    if nums[front] + nums[back] == target:
                        res.append([nums[front], nums[i], nums[back]])
                        while front < back and nums[front] == nums[front+1]:
                            front += 1
                        while front < back and nums[back] == nums[back-1]:
                            back -= 1
                        front += 1
                        back -= 1
                    else:
                        if nums[front] + nums[back] < target:
                            front += 1
                        else:
                            back -= 1
        return res
