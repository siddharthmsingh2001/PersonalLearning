package Basics;

class PrintingClass{
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        System.out.println("Sum of " +a+" + " + b+ " is: " + (a+b));
    }
}


//Understaing the printing statement
/*
 * Java provides buildin class called System which provide various system related properties and methods which are used for interacting with the system environments, accessing system properties. like Garbage Collection, Environment Variables, Array copy, Current Time, System Properties or input/output stream
 * 
 * .out is a static field *in* System class from java.lang packagae *but* this static field(.out) is an instance of the PrintStream class(which is a subclass of OutStream Class) from java.io package
 * 
 * .println/printf/print/format is a method that belongs to PrintStream class and is used to print duhh! All these methods are overloaded meaning a single "function name" can be used have different functions based on parameters e.g println(String s) and println(int i) are different functions with same name
 * 
 * 
 */