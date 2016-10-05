int getSum(int a, int b) {
    int s = 0, c = 0;
    for (int i = 0;  i < 32 ; i ++ ) {
        s |= ( a ^ b ^ c ) & ( 1 << i );
        c = ( ( ( a & b ) | ( a & c ) | ( b & c) ) & ( 1 << i ) ) << 1;
    }
    return s;
}