package AlgorithmsJava;


public class SelectionSort {
    public static int[] selectionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int minIndex = i;
            for (int j = i + 1; j< array.length; j++) {
                if (array[j] > array[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
        return array;
    }
    public static void main(String[] args) {
        int[] array = {7,3,4,9,8,2,1,5};
        array = selectionSort(array);
        for (int num : array) {
            System.out.println(num);
        }
    }
}


