int rangeBitwiseAnd(int m, int n) {
    int t = -1; // ~0 = -1
    while ((m ^ n) & t) t <<= 1;
    return m & t;
}