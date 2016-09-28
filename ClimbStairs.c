int climbStairs(int n) {
    int x = 1, y = 1;
    for(int i=0;i<(n>>1);i++) y += (x += y);
    return (n&0x1)?y:x;
}