class NumArray(object):
    def __init__(self, nums):
        self.sums = [0]
        for i in xrange(len(nums)):
            self.sums.append(nums[i]+self.sums[i])

    def sumRange(self, i, j):
        return self.sums[j+1]-self.sums[i]