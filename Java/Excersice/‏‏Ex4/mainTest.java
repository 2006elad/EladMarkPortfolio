package ex4;

public class mainTest {

	public static void main(String[] args) 
	{
//		DrivingInstructor instructor = new DrivingInstructor();
//		instructor.setName("David");
//		instructor.setPrice(40.5);
//		instructor.setAutomatic(true);
//		System.out.println(instructor.withinPrice(1000, 100));
		
		
//		Car newCar = new Car();
//		newCar.setCompanyName("Audi");
//		newCar.setCurrentSpeed(80);
//		newCar.setMaxSpeed(150);
//		newCar.accelerate(2);
//		System.out.println(newCar.getCurrentSpeed());
		
		RealNum num = new RealNum();
		num.setIntNum(10);
		num.setRemainder(0.5);
		System.out.println(num.getFullNum());
		System.out.println(num.samePart(10.37));
	}

}
