int titleToNumber(char* s) {
    int l = 0, base = 1;
    for(int i = strlen(s)-1; i>=0; i--){
        l += (int)(*(s+i)-'A'+1) * base;
        base *= 26;
    }
    return l;
}
