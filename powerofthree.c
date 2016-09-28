bool isPowerOfThree(int n) {
    if(n<=0) return false;
    while((n%9) == 0)n/=9;
    if(n%3==0) n/=3;
    return !(n-1);
}