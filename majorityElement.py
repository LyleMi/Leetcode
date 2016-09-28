def majorityElement(self, nums):
    nums.sort()
    '''
    k = 0
    for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                k+=1
            else:
                k=0
             k>= len(nums)/2:
                return nums[i]if
    return nums[0]
    '''
    return nums[len(nums)/2]