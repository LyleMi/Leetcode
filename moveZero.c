void moveZeroes(int* nums, int numsSize) {
    for(int i=0; i<numsSize; i++){
        if(!nums[i]){
            int p = i;
            while(!nums[p]){
                p++;
                if(p > numsSize-1) return;
            }
            nums[i] = nums[p];
            nums[p] = 0;
        }
    }
}