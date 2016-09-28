int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int * a = (int *)malloc(sizeof(int)*numsSize);
    for(int i=0;i<numsSize;i++) a[i] = 1;
    int left = 1,right=1;
    for(int i=0;i<numsSize;i++){
        a[i]*=left;
        a[numsSize-1-i]*=right;
        left*=nums[i];
        right*=nums[numsSize-1-i];
    }
    *returnSize = numsSize;
    return a;
}