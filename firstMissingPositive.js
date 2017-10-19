/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    const n = nums.length // will faster than only use .length
    for (let i = 0; i < n; i++) {
        while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i])
            nums[i] = [nums[nums[i] - 1], nums[nums[i] - 1] = nums[i]][0]
            // below version is not fast enough
            // [nums[i], nums[nums[i] - 1]] = [nums[nums[i] - 1], nums[i]]
            // nums[i] = (nums[nums[i] - 1] ^= nums[i] ^= nums[nums[i] - 1]) ^ nums[i]
    }

    for (let i = 0; i < n; i++) {
        if (nums[i] != i + 1)
            return i + 1
    }
    return n + 1
};