int countPrimes(int n) {
    if (n <= 2) return 0;
    if (n == 3) return 1;

    bool* isprimes = (bool*)malloc(sizeof(bool) * n);
    int sqr = sqrt(n);
    int count = 1;

    for(int i = 3; i < n; i+=2) isprimes[i] = true;

    for(int i = 3; i <= sqr; i+=2){
        if(isprimes[i])
            for(int j = i*i; j < n; j+=2*i)
                isprimes[j] = false;
    }

    for(int i = 3; i < n; i+=2){
        if(isprimes[i])
            count++;
    }

    return count;
}
