/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    console.log(x, n)
    if (n === 0) return 1
    if (n < 0) return myPow(1 / x, -n)
    return ((n & 1) ? x : 1) * myPow(x * x, Math.floor(n / 2))
};

// seems n >>> 1 faster than Math.floor?