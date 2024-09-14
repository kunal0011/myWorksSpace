package amazon;

public class OptimalDivision553 {
    public String optimalDivision(int[] nums) {
        // If there's only one number, return it as it is
        if (nums.length == 1) {
            return Integer.toString(nums[0]);
        }
        // If there are two numbers, return them divided without parentheses
        if (nums.length == 2) {
            return nums[0] + "/" + nums[1];
        }
        // For more than two numbers, format as "a/(b/c/d/...)"
        StringBuilder sb = new StringBuilder();
        sb.append(nums[0]).append("/(");
        for (int i = 1; i < nums.length; i++) {
            sb.append(nums[i]);
            if (i != nums.length - 1) {
                sb.append("/");
            }
        }
        sb.append(")");
        return sb.toString();
    }
}
