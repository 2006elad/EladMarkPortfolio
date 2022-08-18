//Lior hazoom 205972078	
// Elad mark 316293638

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;
public class Main {

	public static void totalClaims(ArrayList<PropertyInsurance> allPropWithInsurance)
	{
		int AmountOfDamage;
		for(PropertyInsurance pi: allPropWithInsurance)
		{
			AmountOfDamage = ThreadLocalRandom.current().nextInt(1000, 100001);
			pi.insuranceClaim(AmountOfDamage);
		}
	}
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		String streetName, type;
		char smb;
		String ownerName = null, ownerId= null;
		int ownerNumber;
		int streetNum, aptNum, size, householdSize;
		boolean isPubIsValid = false, isResIsValid = false, isComIsValid = false;
		Public PublicProp = null;
		Residential ResidentialProp = null;
		Commercial CommercialProp = null;
		while(!isPubIsValid)
		{
			try
			{
					System.out.println("Please insert Public Property Street name: ");
					streetName = input.nextLine();
					System.out.println("Please insert Public Property Street num: ");
					streetNum = input.nextInt();
					System.out.println("Please insert Public Property apt num: ");
					aptNum = input.nextInt();
					System.out.println("Please insert Public Property size: ");
					size = input.nextInt();
					System.out.println("Please insert Public Property type ");
					type = input.nextLine();
					System.out.println("Please insert owner Name");
					ownerName = input.nextLine();
					System.out.println("Please insert owner id");
					ownerId = input.nextLine();
					System.out.println("Please insert owner id");
					ownerNumber = input.nextInt();
					PublicProp = new Public(streetName, streetNum, aptNum,size, type, ownerName, ownerId, ownerNumber);
					isPubIsValid = true;
			}
			
			catch(Exception e)
			{
				System.out.println(e.getMessage());
			}
			
		}
		while(!isResIsValid)
		{
			try
			{
					System.out.println("Please insert Residential Property Street name: ");
					streetName = input.nextLine();
					System.out.println("Please insert Residential Property Street num: ");
					streetNum = input.nextInt();
					System.out.println("Please insert Residential Property apt num: ");
					aptNum = input.nextInt();
					System.out.println("Please insert Residential Property size: ");
					size = input.nextInt();
					System.out.println("Please insert Residential How much People live in house: ");
					householdSize = input.nextInt();
					System.out.println("Please insert owner Name");
					ownerName = input.nextLine();
					System.out.println("Please insert owner id");
					ownerId = input.nextLine();
					System.out.println("Please insert owner id");
					ownerNumber = input.nextInt();
					ResidentialProp = new Residential(streetName, streetNum, aptNum,size, householdSize, ownerName, ownerId, ownerNumber);
					isResIsValid = true;
			}
			
			catch(Exception e)
			{
				System.out.println(e.getMessage());
			}
			
		}
		while(!isComIsValid)
		{
			try
			{
					System.out.println("Please insert Commercial Property Street name: ");
					streetName = input.nextLine();
					System.out.println("Please insert Commercial Property Street num: ");
					streetNum = input.nextInt();
					System.out.println("Please insert Commercial Property apt num: ");
					aptNum = input.nextInt();
					System.out.println("Please insert Commercial Property size: ");
					size = input.nextInt();
					System.out.println("Please insert Commercial Property Business size(S,M,L): ");
					smb = input.next().charAt(0);
					System.out.println("Please insert owner Name");
					ownerName = input.nextLine();
					System.out.println("Please insert owner id");
					ownerId = input.nextLine();
					System.out.println("Please insert owner id");
					ownerNumber = input.nextInt();
					CommercialProp = new Commercial(streetName, streetNum, aptNum, size, smb, ownerName, ownerId, ownerNumber);
					isComIsValid = true;
			}
			catch(Exception e)
			{
				System.out.println(e.getMessage());
			}
		}
//		Public PublicProp;
//		Residential ResidentialProp;
//		Commercial CommercialProp;
		ArrayList<Property>allPropInCity = new ArrayList<Property>();
		ArrayList<PropertyInsurance> allPropWithInsurance = new ArrayList<PropertyInsurance>();
		ArrayList<PropertyTaxes> allPropWithTaxes = new ArrayList<PropertyTaxes>();
		allPropInCity.add(PublicProp);
		allPropInCity.add(ResidentialProp);
		allPropInCity.add(CommercialProp);
		allPropWithTaxes.add(PublicProp);
		allPropWithTaxes.add(CommercialProp);
		allPropWithTaxes.add(ResidentialProp);
		allPropWithInsurance.add(PublicProp);
		allPropWithInsurance.add(CommercialProp);
		
		for(Property p: allPropInCity)
		{
			System.out.println(p);
		}
		for(PropertyTaxes pt: allPropWithTaxes)
		{
			pt.ownershipDetails();
			System.out.println("His Taxes are: " + pt.calcPropertyTax() );
		}
		input.close();	
	}

}
