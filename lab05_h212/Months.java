import java.util.HashMap;
import java.util.Scanner;
public class Months {
  public static void main(String[] args) {
    HashMap<Integer, String> months_map= new HashMap<Integer, String>();
    Scanner ollie;
    ollie = new Scanner(System.in);
    System.out.println("Enter month");
    String age = ollie.nextLine();
    int m = Integer.parseInt( age );
    months_map= .put(1, "January");
    months_map= .put(2, "February");
    months_map.put(3, "March");
    months_map.put(4, "April");
    months_map.put(5, "May");
    months_map.put(6, "June");
    months_map.put(7, "July");
    months_map.put(8, "August");
    months_map.put(9, "September");
    months_map.put(10, "October");
    months_map.put(11, "November");
    months_map.put(12, "December");
    System.out.println(months_map.get(m));
  }
}
