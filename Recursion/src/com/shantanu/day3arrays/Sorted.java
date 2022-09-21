package com.shantanu.day3arrays;

public class Sorted {
    public static void main(String[] args) {
        int[] arr1 = {2,3,6,9,12,17,23,25,32,96};
        System.out.println(sorted(arr1,0));
    }
    static boolean sorted(int[] arr,int index){
//        base condition
        if(index==arr.length-1){
            return true;
        }
//        recursion we used sorted function after the return function
        return arr[index] < arr[index+1] && sorted(arr,index+1);
    }
}
