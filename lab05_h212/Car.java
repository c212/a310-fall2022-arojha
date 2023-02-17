public class Car{
	double gas =0;
	double mileage;
	public Car(double m){
		this.mileage=m;
	}
	public double getGas(){
		System.out.println("Gas is "+this.gas);
		return this.gas;
	}
	public void drive(double distance){
		double d = distance/mileage;
		this.gas-=d;
	}
	public void setGas(double g){
		this.gas=g;
	}
}
