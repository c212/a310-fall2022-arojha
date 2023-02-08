import java.util.Scanner;
import static java.lang.Math.sqrt;
import java.lang.Math;
public class eva {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter number to take the square root of: ");
        double number = Double.parseDouble(scanner.nextLine());
        double original = sqrt(number);
        System.out.println("The original square root is: " + original);
        //System.out.println(squareRoot(original, number));
        double first_guess = ((number/2)+2)/2;
        System.out.println(sqrtt(number/2,first_guess,number));
    }
        public static double sqrtt(double prev,double next,double orig){
                if(Math.abs(prev-next)<0.05 ){
                        return next;
                }
                else{  
                        return sqrtt(next,(next+(orig/next))/2,orig);
                }
}
    public static String squareRoot(double original, double number) {
        if ((Math.abs(original - number)) < 0.001) {
            return "The calculated square root is: " + number;
        }
        else {
            double newNumber = ((number / (number * 0.5)) + (number * 0.5)) / 2;
            return squareRoot(original, newNumber);
        }
    }
}
