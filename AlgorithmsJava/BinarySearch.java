package AlgorithmsJava;

public class BinarySearch {
    public static void main(String[] args) {
        int[] array = createArray(1000000000);
        
        int target = 900030332;
        
        long begin = System.currentTimeMillis();
        //int indexLinear = indexOfTargetLinear(array, target);

        int indexBinary = indexOfTargetBinary(array, target);
        long end = System.currentTimeMillis();

        long total = end - begin;

        System.out.println(indexBinary);
        System.out.println("Number of Milliseconds: " + total);

        // System.out.println("index Linear Search: " + indexLinear
        //                 + "\nindex Binary Search: " + indexBinary
        //                 + "\ntarget: " + target);
    }

    //slow way O(n)
    public static int indexOfTargetLinear(int[] array, int target) {
        for (int i = 0; i < array.length; i++) {
            if (target == array[i]) {
                return i;
            }
        }
        //Not in list
        return -1;
    }

    //binary search O(log n)
    public static int indexOfTargetBinary(int[] array, int target) {
        int low = 0;
        int high = array.length -1;
        int iterations = 0;
        while (low <= high) {
            int middle = (low + high)/2;
            // System.out.println(middle);
            if (array[middle] == target) {
                System.out.println("Number of steps: " + iterations);
                return middle;
            } else if (array[middle] > target) 
                high = --middle;
            else 
                low = ++middle;
            iterations++;
        }
        //Element not in list
        return -1;
    }

    public static String arrayToString(int[] array) {
        String arrayString = "";
        for (int i = 0; i < array.length; i++) {
            arrayString += array[i];
            if (i + 1 < array.length)
                arrayString += ", ";
        }
        return arrayString;
    }

    public static int[] createArray(int numOfElemets) {
        int[] array = new int[numOfElemets];

        for (int i = 0; i < array.length; i++) {
            array[i] = i;
        }
        return array;
    }
}