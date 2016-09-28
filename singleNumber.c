int singleNumber(int* nums, int numsSize) {
    int re = 0;
    for(int i=0; i<numsSize; i++) re ^= *(nums+i);
    return re;
}