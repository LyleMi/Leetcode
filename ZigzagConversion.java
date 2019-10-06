class Solution {
    public String convert(String s, int numRows) {
        int len = s.length();
        if (numRows == 1 || len < numRows) {
            return s;
        }
        StringBuffer buf = new StringBuffer();
        int mod = (numRows - 1) << 1;
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; (j <= (len / numRows)) && ((j * mod + i) < len); j++) {
                buf.append(s.charAt(j * mod + i));
                if ((i % (numRows - 1) != 0) && ((j + 1) * mod - i) < len) {
                    buf.append(s.charAt((j + 1) * mod - i));
                }
            }
        }
        return buf.toString();
    }
}
