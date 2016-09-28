int reverse(int x) {
    int result = 0, tail, newResult;
    while(x!=0){
        tail = x % 10;
        newResult = result * 10 + tail;
        if ((newResult - tail) / 10 != result) return 0;
        result = newResult;
        x /= 10;
    }
    return result;
}