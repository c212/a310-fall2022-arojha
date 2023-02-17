public class CounterTester{
	public static void main(String[] args){
		Counter c = new Counter();
		c.click();
		c.click();
		System.out.println("Value should be 2");
		System.out.println(c.getValue());
	}
}
