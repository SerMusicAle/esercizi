
public class Pitagora {

	public static void main(String[] args) {
		//Triangolo
		double c1 = 45.3;
		double c2 = 67.2;
		 
		//Triangolo
		double ipo = Math.sqrt(Math.pow(c1, 2) + Math.pow(c2,  2));
		double per = c1 + c2 + ipo;
		double area = (c1 * c2) /2;
	
		//Cerchio
		double r = (ipo/4)*3;
		double areaC = (r * r) * 3.14;
		double perC = 2*(3.14*r);
		
		//Triangolo

        System.out.println("La lunghezza dell'ipotenusa è: " + ipo);
        System.out.println("Il perimetro del triangolo è: " + per);
        System.out.println("L'area del triangolo è " + area);
        
		//Cerchio
        System.out.println("Il raggio del cerchio è: " + r);
        System.out.println("Il perimetro del cerchio è: " + perC);
        System.out.println("L'area del cerchio è " + areaC);
	}

}

