var rob = function(nums) {
    let prevNo = 0, prevYes = 0
    nums.forEach(n => [prevNo, prevYes] = [Math.max(prevNo, prevYes), n + prevNo])
    return Math.max(prevNo, prevYes)
};