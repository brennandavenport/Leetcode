package AlgorithmsJava;

import java.util.LinkedList;

public class BubbleSort {
    public static int[] bubbleSort(int[] array){
        int length = array.length;
        boolean sorted = false;

        while (!sorted) {
            sorted = true;
            for (int i = 0; i < length; i++) {
                if (i+1 < length && array[i] > array[i+1]) {
                    sorted = false;
                    int temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                }
            }
        }
        return array;
    }

    public static void main(String[] args) {
        int[] array = {1,2,5,8,9,7,6,4,3};
        array = bubbleSort(array);
        for (int num : array) {
            System.out.println(num);
        }

        LinkedList<Integer> numbers = new LinkedList<Integer>();
    }
}
