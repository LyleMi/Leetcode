bool isHappy(int n) {
    if(n<10){
        if(n==1 || n==7) return true;
        return false;
    }
    int sum = 0,i;
    while(n!=0){
        i = n%10;
        n/=10;
        sum += i*i;
    }
    return isHappy(sum);
}
