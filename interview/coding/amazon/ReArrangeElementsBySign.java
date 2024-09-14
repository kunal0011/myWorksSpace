package amazon;

public class ReArrangeElementsBySign {
    public int[] rearrangeArray(int[] nums) {
        int posidx = 0;
        int negidx = 1;
        int ans[] = new int[nums.length];
        for(int i = 0;i<nums.length;i++){
            if(nums[i]<0){
                ans[negidx] = nums[i];
                negidx+=2;
            }
            else{
                ans[posidx] = nums[i];
                posidx+=2;
            }
        }
        return ans;
    }
}
