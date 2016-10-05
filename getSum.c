int getSum(int a, int b) {
    int s = 0, c = 0, i = 1;
    while (i != 0) {
        s |= ( a ^ b ^ c ) & i;
        c = ( ( a & b ) | ( a & c ) | ( b & c ) & i ) << 1;
        i = i << 1;
    }
    return s;
}