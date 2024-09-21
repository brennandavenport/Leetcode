package AlgorithmsJava;

public class InsertionSort {
    public static int[] insertionSort(int[] array) {
        for (int i = 1; i < array.length; i++) {
            int key = array[i];
            int j = i - 1;
            
            // Move elements of array[0..i-1] that are greater than key
            // to one position ahead of their current position
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j--;
                for (int num : array) {
                    System.out.print(num + ", ");
                }
                System.out.println();
            }
            
            array[j + 1] = key;
        }
        return array;
    }


    public static void main(String[] args) {
        int[] array = {9,4,654,65,34,3456, 5};
        array = insertionSort(array);
        for (int num : array) {
            System.out.print(num + ", ");
        }
    }
}
