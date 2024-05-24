package miscellaneous;

public class BuildingsFacingSun {
    public static int countBuildingsFacingSun(int[] heights) {
        if (heights == null || heights.length == 0) {
            return 0;
        }

        int count = 0;
        int maxHeight = Integer.MIN_VALUE;

        for (int height : heights) {
            if (height > maxHeight) {
                count++;
                maxHeight = height;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[] heights = {7, 4, 8, 2, 9};
        System.out.println("Number of buildings facing the sun: " + countBuildingsFacingSun(heights));
    }
}
