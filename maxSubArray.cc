class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int pre = maxSum;

        for(int i = 1; i < nums.size(); i++){
            pre = nums[i] + max(pre, 0);
            maxSum = max(maxSum, pre);
        }

        return maxSum;
    }
};