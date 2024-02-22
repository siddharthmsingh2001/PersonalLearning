package Introduction;
import java.lang.System;
import java.util.Scanner;

public class InputTest {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        int a,b;
        System.out.println("Enter two numbers");
        a = input.nextInt();
        b = input.nextInt();
        System.out.println("Sum is: "+ (a+b));
    }
}


// Here in the input section
// Scanner is a class that belongs to util package it is used to take input stream 
// Scanner input = new Scanner(System.in)
// The first "Scanner" is declaring the input type of variable which is scanner type
// The "input" is just a variable to which we are going to pass a reference
// The new indicates we are going to create a new instane of the Scanner class which will be assigned to "input"
// The second "Scanner" is calling the Constructor of the Scanner class
// The "System.in" represents standard input system meaning:
// The "System" is a low level class in java which consists of static field ".in" which is used to take low level inputs like bytes
// However taking input in form bytes and operating is not easy so we need a higher level interpretation of these bytes which we get thorugh Scanner Class
