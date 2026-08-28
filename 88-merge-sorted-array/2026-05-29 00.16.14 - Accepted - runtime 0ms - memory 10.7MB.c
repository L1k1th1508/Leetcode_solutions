void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i=0;
    int j=0;
    int k=0;
    int *copy1=malloc(m*sizeof(int));
    for(int a=0;a<m;a++){
        copy1[a]=nums1[a];
    }
    int *copy2=malloc(n*sizeof(int));
    for(int b=0;b<n;b++){
        copy2[b]=nums2[b];
    }
    
    while(i<m&&j<n){
    if(copy1[i]<copy2[j]){
        nums1[k]=copy1[i];
        
        i++;
    }
    else{
        nums1[k]=copy2[j];
        j++;
    }
    k++;
    }
    while(j<n){
        nums1[k]=copy2[j];
        j++;
        k++;
    }
    while(i<m){
        nums1[k]=copy1[i];
        i++;
        k++;
    }
}