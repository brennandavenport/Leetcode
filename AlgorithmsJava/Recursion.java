package AlgorithmsJava;

public class Recursion {
    public static int binarySearch(int[] array, int target, int low, int high) {
        if (low > high) 
            return -1;
        
        int middle = (low + high) / 2;

        if (array[middle] == target) 
            return middle;
        else if (array[middle] > low) {
            return binarySearch(array, target, middle + 1, high);
        } else {
            return binarySearch(array, target, low, middle - 1);
        }
    }

    public static void main(String[] args) {
        int[] arr = {1,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60};

        int index = binarySearch(arr, 60, 0, arr.length - 1);
        System.out.println(index);
    }
}
