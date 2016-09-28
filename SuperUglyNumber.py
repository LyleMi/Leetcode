class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        nums = [1] * len(primes)
        idx = [0] * len(primes)
        cur = 1
        ugly = [1]

        for i in xrange(n-1):
            for j in xrange(len(primes)):
                if nums[j] == cur:
                    nums[j] = ugly[idx[j]] * primes[j]
                    idx[j] += 1
            cur = min(nums)
            ugly.append(cur)

        return ugly[-1]
