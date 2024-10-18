public class TriangoloRettangolo {
    // Dichiarazione di attributi/variabili
    private double cat1;
    private double cat2;
    private double ipo;
    private double area;
    private double perim;

    // Costruttore
    public TriangoloRettangolo(double cat1, double cat2) {
        this.cat1 = cat1;
        this.cat2 = cat2;
        this.ipo = Math.sqrt(Math.pow(cat1, 2) + Math.pow(cat2, 2));
        this.area = (cat1 * cat2) / 2; // Area di un triangolo rettangolo è cat1 * cat2 / 2
        this.perim = cat1 + cat2 + ipo;

        // Calcolo del raggio e della circonferenza
        double raggio = ipo * 3.0 / 4.0; // Raggio per la circonferenza
        double circonferenza = 2.0 * raggio * Math.PI;
        double areac = Math.PI * Math.pow(raggio, 2);

        System.out.println("Trigonometria");
        double a = Math.sin(Math.toRadians(45)); // Convertire in radianti
        System.out.println("sin(45°): " + a);
        double b = Math.sin(Math.PI / 4); // Questo è già corretto
        System.out.println("sin(π/4): " + b);
    }

    // Metodi getter
    public double getCat1() {
        this.cat1 = cat1;
        UpdateFunctionalRelations();
    }

    private void UpdateFunctionalRelations() {
        ipo = Math.sqrt(Math.pow(cat1, 2) + Math.pow(cat2, 2));
        area = (cat1 * cat2) / 2; 
        perim = cat1 + cat2 + ipo;
    }

	public double getCat2() {
        return cat2;
    }

	public void setCat1(double cat1) {
		this.cat1 = cat1;
		UpdateFunctionalRelations();
	}
	
	public void setCat2(double cat2) {
		this.cat2 = cat2;
		UpdateFunctionalRelations();
	}
    public double getIpo() {
        return ipo;
    }

    public double getArea() {
        return area; // Aggiunto per restituire l'area
    }

    public double getPerim() {
        return perim; // Aggiunto per restituire il perimetro
    }

    public static void main(String[] args) {
        // Creazione di un oggetto TriangoloRettangolo
        TriangoloRettangolo tr = new TriangoloRettangolo(3, 4);
        
        // Stampa dei risultati
        System.out.println("Ipotenusa: " + tr.getIpo());
        System.out.println("Area: " + tr.getArea());
        System.out.println("Perimetro: " + tr.getPerim());
        
        tr.setCat1(6);
        System.out.println("Ipotenusa: " + tr.getIpo());
        System.out.println("Area: " + tr.getArea());
        
        TriangoloRettangolo tr1 = new TriangoloRettangolo (900, 0.2);
        tr1.setCat2(9876);
    }
}
