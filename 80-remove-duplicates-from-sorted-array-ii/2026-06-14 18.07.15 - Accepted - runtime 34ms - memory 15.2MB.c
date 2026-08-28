int removeDuplicates(int* nums, int numsSize) {
    int j=0;
    int count=1;

        for(int i=0;i<numsSize;i++){
            if(j<2||nums[i]!=nums[j-2]){
                nums[j]=nums[i];
                j++;
            }
        }
            
        
    
    return j;
}