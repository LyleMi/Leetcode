class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() < 2) {
            return 0;
        }

        int level = 0, curMax = 0, nextMax = 0, i = 0, n = nums.size();

        // while (curMax + 1 > i) {
        while (true) { // will always reach the last index.
            for (level++; i <= curMax; i++) {
                nextMax = max(nextMax, nums[i] + i);
                if (nextMax >= n - 1) return level;
            }
            curMax = nextMax;
        }
    }
};