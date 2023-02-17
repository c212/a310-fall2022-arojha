import java.util.Scanner;
public class Military{
	public static void main(String[] args){
		int t1=0;
		int t2=0;
		Scanner ollie;
    		ollie = new Scanner(System.in);
		System.out.println("Enter time1 ");
		String age1 = ollie.nextLine();
		t1 = Integer.parseInt(age1);
		System.out.println("Enter time 2");
		String age2 = ollie.nextLine();
                t2 = Integer.parseInt(age2);
		int mindiff = (t2/100)*60+(t2%100) - (t1/100)*60 -(t1%100);
		int adjusted_diff = ((24*60)+mindiff)%(24*60);
		int hours = adjusted_diff/60;
		int mins = adjusted_diff%60;
		System.out.println("Time diff is "+hours+" hours "+mins+" mins" );
	}
}
