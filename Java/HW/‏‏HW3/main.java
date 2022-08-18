
public class main 
{

	public static void main(String[] args) 
	{
		// b1 (Question 4-1)
		Subscriber b1 = new Subscriber(200, 5);
		System.out.println(b1.calcCost());
		System.out.println(b1.calcRefund(2));
		b1.print();
		
		// Creating services (Question 4-2) 
		Service pool = new Service("pool", 50, false);
		Service locker = new Service("locker", 10, true);
		Service playroom = new Service("playroom", 25, true);
		
		// ad1 (Question 4-3)
		Advanced ad1 = new Advanced(160, 2);
		ad1.addService(pool);
		ad1.addService(locker);
		System.out.println(ad1.calcCost());
		ad1.print();
		
		// ad2 (Question 4-4)
		Advanced ad2 = new Advanced(180, 2);
		ad2.addService(pool);
		ad2.calcCost();
		System.out.println(ad2.serviceExist("spinning"));
		ad2.addService(pool);
		
		// fam1 (Question 4-5)
		Family fam1 = new Family(190, 11, 3, 2);
		fam1.addService(playroom);
		fam1.addService(pool);
		System.out.println(fam1.calcCost());
		System.out.println(fam1.calcRefund(3));
		fam1.print();

//		// testing
//		
//		
//		Advanced ad = new Advanced(120, 1);
//		Service pool = new Service("pool", 15, false);
//		Service locker = new Service("locker", 10, true);		
//		
////		ad.addService(pool);
////		ad.addService(locker);
////		
////		ad.print();
////		System.out.println(ad.calcCost());
////		System.out.println(ad.calcRefund(4));
//		
////		System.out.println(ad.serviceExist("spinning"));
////		ad.addService(pool);
////		
//		Service poolRefund = new Service("pool", 20, true);
//		Family fam1 = new Family(100, 1, 2, 2);
//		fam1.addService(poolRefund);
//		
//		fam1.print();
//		System.out.println(fam1.calcCost());
//		System.out.println(fam1.calcRefund(7));
	}
}
