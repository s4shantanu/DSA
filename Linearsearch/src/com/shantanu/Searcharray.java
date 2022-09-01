package com.shantanu;

public class Searcharray {
    public static void main(String[] args) {
        int[] num = {23,34,5,54,4,3,23,42};
        int target = 34;
        int ans = linearsearchindex(num,target);
        int ans1 = linearsearchelement(num,target);
        boolean ans3 = linearsearchbool(num,target);
        System.out.println(ans);
        System.out.println(ans1);
        System.out.println(ans3);

    }

//    for return the boolean value of array the target was present or not
    static boolean linearsearchbool(int[] arr, int target){
        if(arr.length == 0){
            return false;
        }
        for(int element : arr){
            if(element == target){
                return true;
            }
        }
//        Target not found
        return false;
    }
    static int linearsearchelement(int[] arr, int target){
        if (arr.length==0){
            return -1;
        }
//        for return the element of that array
        for(int element : arr){
            if (element == target) {
                return element;
            }
        }
        return Integer.MAX_VALUE;

    }

//    Linear seach for the index value of the target
    static int linearsearchindex(int[] arr, int target){
        if (arr.length == 0){
            return -1;
        }
//        Runs a for loop for searching the value
        for (int i = 0; i < arr.length; i++) {
            int element = arr[i];
            if (element == target) {
                return i;

            }
        }
//        If target is not found then return -1 is print
        return -1;
    }
}
