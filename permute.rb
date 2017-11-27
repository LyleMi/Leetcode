def permuteRecursive(nums, start, result)
    nums = Array.new(nums)
    if start >= nums.length
        result.push(nums)
    else
        for i in start..(nums.length - 1) do
            nums[start], nums[i] = nums[i], nums[start]
            result = permuteRecursive(nums, start + 1, result)
            nums[start], nums[i] = nums[i], nums[start]
        end
    end
    result
end

def permute(nums)
    permuteRecursive(nums, 0, Array.new())
end
