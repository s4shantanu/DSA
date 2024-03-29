package com.shantanu;
//Basically floor means gretest number <= target
public class Floor {
    public static void main(String[] args) {
            int[] arr = {2, 3, 4, 15, 16, 18, 22, 45, 89};
            int target = 1;
            int ans = floor(arr, target);
            System.out.println(ans);
        }
        // return the index
        // return -1 if it does not exis t
        static int floor(int[] arr, int target) {
            int start = 0;
            int end = arr.length - 1;

            while(start <= end) {
                // find the middle element
//            int mid = (start + end) / 2; // might be possible that (start + end) exceeds the range of int in java
                int mid = start + (end - start) / 2;

                if (target < arr[mid]) {
                    end = mid - 1;
                } else if (target > arr[mid]) {
                    start = mid + 1;
                } else {
                    // ans found
                    return mid;
                }
            }
            return end;
        }
    }
