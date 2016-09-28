int missingNumber(int* nums, int numsSize) {
    int missing = 0, i = 0;
    while(i < numsSize) missing ^= (i ^ nums[i++]); 
    return missing;
}