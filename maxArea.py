class Solution(object):

    def maxArea(self, height):
        left = len(height)-1
        right = 0
        H = min(height[right], height[left])
        maxC = left * H

        while right < left:
            H = min(height[right], height[left])
            maxC = max(maxC, (left-right) * H)
            while right < left and height[right] <= H:
                right += 1
            while right < left and height[left] <= H:
                left -= 1

        return maxC
