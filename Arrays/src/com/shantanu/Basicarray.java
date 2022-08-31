package com.shantanu;

import java.sql.SQLOutput;
import java.util.Arrays;
import java.util.Scanner;

public class Basicarray {
    public static void main(String[] args) {
//        store 5 ros integer in ros variable with help of using new object arrays
        String [] ros = new String[5];
//        we can also creat it directly.
        int[] rows = {1,34,45,5,6,4};
        System.out.println(Arrays.toString(ros));

//input arary
        Scanner input = new Scanner(System.in);
        String[] arr = new String[4];
        for (int i = 0; i < arr.length; i++) {
            arr[i]= input.next();
        }
        System.out.println(Arrays.toString(arr));
    }
}
