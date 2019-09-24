class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1
        imin, imax = 0, n2 * 2
        while imin <= imax:
            j = (imin + imax) >> 1
            i = n1 + n2 - j
            l1 = -0xfffffff if i == 0 else nums1[(i-1) >> 1]
            l2 = -0xfffffff if j == 0 else nums2[(j-1) >> 1]
            r1 = 0xfffffff if i == n1 << 1 else nums1[i >> 1]
            r2 = 0xfffffff if j == n2 << 1 else nums2[j >> 1]
            if l1 > r2:
                imin = j + 1
            elif l2 > r1:
                imax = j - 1
            else:
                return (max(l1, l2) + min(r1, r2)) / 2
