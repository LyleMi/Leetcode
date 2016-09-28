void rotate(int* nums, int numsSize, int k) {
    if(!(k %= numsSize)) return;
    int index = 0, index2 = numsSize-k, n = numsSize - 1;
    while(n-- > 0){
        if( index == index2 ){
            index = (++index2) + k - numsSize;
            n--;
        }
        nums[index] ^= nums[index2];
        nums[index2] ^= nums[index];
        nums[index] ^= nums[index2];
        index = (index + k) % numsSize;
    }
}