int romanToInt(char* s) {
    int sum = 0, curr = 0, pre = 0;
    int roman[] = {100, 500, 0, 0, 0, 0, 1, 0, 0, 50, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10};
    while (*s) {
        curr = roman[*s - 'C'];
        sum += curr - (pre < curr) * ( pre << 1 );
        pre = curr;
        s++;
    }
    return sum;
}