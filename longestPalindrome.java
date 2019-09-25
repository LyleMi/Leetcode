class Solution {
    public String longestPalindrome(String s) {
        int len = s.length(), start = 0, end = 0;
        boolean[][] match = new boolean[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = i; j >= 0; j--) {
                match[i][j] = (s.charAt(i) == s.charAt(j)) && (i-j < 2 || match[i-1][j+1]);
                if (match[i][j] && i - j > end - start) {
                    start = j;
                    end = i;
                }
            }
        }
        return len!=0 ? s.substring(start, end+1) : "";
    }
}
