int hammingWeight(uint32_t n) {
    int t=0;
    while (n!=0){
        t+=n&1;
        n/=2;
    }
    return t;
}