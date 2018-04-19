class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        for(int i = 0; i < nums.length; i++) {
            int temp = res.size();
            for(int j = 0; j < temp; j++) {
                List<Integer> add = new ArrayList<>(res.get(j));
                add.add(nums[i]);
                res.add(add);
            }
        }
        return res;
    }
}