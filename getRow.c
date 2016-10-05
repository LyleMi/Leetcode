int* getRow(int row, int* returnSize) {
    if (row < 0) return NULL;
    int * ret = (int*)malloc(sizeof(int) * (row + 1));
    ret[0] = 1;
    for (int i = 1; i <= row; i++) {
        ret[i] = (int)(((long)ret[i - 1] * (row - i + 1)) / i);
    }
    *returnSize = row + 1;
    return ret;
}