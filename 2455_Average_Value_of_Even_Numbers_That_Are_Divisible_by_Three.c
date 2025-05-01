int averageValue(int* nums, int numsSize) {
    int length=0,sum=0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]%2==0){
            if(nums[i]%3==0){
                length++;
                sum+=nums[i];
            }
        }
    }
    if(length==0){
        return 0;
    }
    return sum/length;
}