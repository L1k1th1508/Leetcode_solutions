/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    int small=0;
    int count=0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]<target){
            small++;
        }
        else if(nums[i]==target){
            count++;
        }
    }
    *returnSize=count;
    if(count ==0){
        return NULL;
    }
    int *result=malloc(count*sizeof(int));
    for(int i=0;i<count;i++){
        result[i]=small+i;
    }
    return result;
    
}