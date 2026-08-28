
int removeDuplicates(int* nums, int numsSize) {
    int duplicates=0;
    for(int i=1;i<numsSize;i++){
        if(nums[duplicates]!=nums[i]){
            duplicates++;
            nums[duplicates]=nums[i];
        }
    }
    return duplicates+1;
}
    
    
    
    
     

    
