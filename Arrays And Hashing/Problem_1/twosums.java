public class twosums {
    public static void main(String[] args) {
        int[] nums = {3, 3};
        int target = 6;
        int[] answer = twoSum(nums, target);
        for (int num: answer) {
            System.out.println(num);
        }
    }

    public static int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (((nums[i] + nums[j]) == target) && (i != j)) {
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
}
