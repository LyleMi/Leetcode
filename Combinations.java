class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> combs = new ArrayList<List<Integer>>();
        List<Integer> temp = new ArrayList<Integer>();
        for(int i = 0; i < k; i++) { temp.add(0); }
        int i = 0;
        while (i >= 0) {
            temp.set(i, temp.get(i) + 1);
            if(temp.get(i) > n) {
                i -= 1;
            } else if (i == k-1) {
                combs.add(new ArrayList<Integer>(temp));
            } else {
                i += 1;
                temp.set(i, temp.get(i-1));
            }
        }
        return combs;
    }
}
