
public class Main {

	public static void main(String[] args) {

		Integer [] vint;
		double [] vdou;
		
		vint = new Integer [100];
		vdou = new double[100];
		
		System.out.println(vint);
		System.out.println(vdou);
		
		
		for (Integer i=0; i<100; i++) 
		{
			vint[i]=i+1;
		}
		
		for (Integer i=100; i>=0; i--) 
		{
			vint[100-i]=i;
		}
		
		StampaVint(vint);
		
		for (Integer i=0; i<100; i++) 
		{
			vint[i]=(i+1)*2;
		
		}
		for (Integer i=0; i<100; i++) 
		{
			vint[i]=(i+1)*2-1;
		}
		
		for (Integer i=0; i<100; i++) 
		{
			vdou[i]=1.0/(i+1.0);
		}
		vint[0]=1;
		vint[1]=1;
		
		for (Integer i=0; i<100; i++) 
		{
			vint[i]=vint[i-1]+vint[i-2];
		}	
		System.out.println(Fattoriale(15));
		System.out.println(Fact(15));
		
		for (int i=0; i<100; i++) 
		{
			vdou[i] = 1.0/Math.pow(2, 1);
		}
		StampaVdou(vdou);
		
		for (int i=0; i<100; i++) 
		{
			double dueallai = 1;
			for (int j = 1; j<i; j++)
			{
				dueallai *=2;
			}
			vdou[i] = 1.0/dueallai;
		}
		StampaVdou(vdou);

	}
	
	private static void StampaVdou(double[] vdou)
	{
		for (double v : vdou)
		{
			System.out.print(v + " ");
		}
		System.out.println();
	}
	
	//Soluzione iterativa
	private static Integer Fattoriale(Integer N) 
	{
		Integer p = 1;
		
		for (Integer i=2; i<N; i++)
		{
			p = p * 1;
		}
		return p;
	}
	
	//Soluzione ricorsiva
	private static Integer Fact (Integer N)
	{
		if (N==0)
		{
			return 1;
		}
		else 
		{
			return N * Fact(N-1);
		}
	}
	
	//crivello di eratostene
	private static void Eratostene (Integer N) 
	{

		boolean [] v = new boolean [1000000000];
		for (Integer i=2; i<v.length; i++) 
		{
			if (v[i]==true) 
			{
				System.out.println(i + "è un numero primo");
			
				for (Integer k=i+1; k<v.length; k+=1) 
				{
					v[k] = false;
				}
			}
		}
	
	}
		
	private static void StampaVint(Integer [] vint) 
	{

		for (int v:vint)
		{
			System.out.println(v + " ");
		}
		System.out.println();
	}	
	

}




