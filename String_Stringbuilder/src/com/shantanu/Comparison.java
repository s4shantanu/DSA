package com.shantanu;

public class Comparison {
    public static void main(String[] args) {
        String a = "Shantanu";
        String b = "Shantanu";
        String c = a;
//        System.out.println(c == a);
        // ==
//        System.out.println(a == b);

        String name1 = new String("Shantanu");
        String name2 = new String("Shantanu");

        System.out.println(name1 == name2);

        System.out.println(name1.equals(name2));

    }
}