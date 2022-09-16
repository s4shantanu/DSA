package com.shnatanu;
import java.util.Arrays;

public class Cyclicsorting {
    public static void main(String[] args) {
        int[] arr = {5,3,2,1,4};
        sort(arr);
        System.out.println(Arrays.toString(arr));

    }
    static void sort(int[] arr) {
        int i = 0;
        while (i < arr.length) {
            int correct = arr[i] - 1;       //For maching the number with index.
            if (arr[i] != arr[correct]) {
                swap(arr, i , correct);
            } else {
                i++;
            }
        }
    }
    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}
