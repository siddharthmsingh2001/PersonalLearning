package Introduction;
// Packages help organise the classes into folders
import java.lang.*;


class Skeleton{                                     //Everything in Java is in the form of the class and name of the file and the name of the class is same 
    public static void main(String args[]){         //This is the main mehtod and is the starting/entry point of any program 
        System.out.println("Skeleton Program");
        if(args.length == 0){
            ;
        }
        else{
            System.out.println(args[0]);
        }
        
    }
}


//To run programs
// Java Compiler first converts the text file into byte code -> This byte code is then run by jre in a jvm
//Command ->
// -> javac path/file.java
// -> java path/file args[]


//The main method
//The main method in Java is always void
//The access modifier of the Parent main class should be public so that the jvm can aceess tha main method
//The main method is also static thus alowing us to access the main method of the class without creating object of the class
//The String args[] are also called Command Line Arguments we can pass n number of arguments thorugh terminal in order to use them in the main function

//The print
//The sout or System.out.println
//System is the name of class
//out is the object of the class
//println is the mehtod of the class