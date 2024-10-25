
public class Computer {

	//Dichiaraziione variabili con classi wrapper
	private Double prezzo;
	private Double peso;
	private Double larghezza;
	private Double altezza;
	private Double profondità;
	private String produttore;
	private Integer anno;
	
	// Getter e Setter
	public Double getPrezzo() {
		return prezzo;
	}
	public void setPrezzo(Double prezzo) {
		this.prezzo = prezzo;
	}
	public Double getPeso() {
		return peso;
	}
	public void setPeso(Double peso) {
		this.peso = peso;
	}
	public Double getLarghezza() {
		return larghezza;
	}
	public void setLarghezza(Double larghezza) {
		this.larghezza = larghezza;
	}
	public Double getAltezza() {
		return altezza;
	}
	public void setAltezza(Double altezza) {
		this.altezza = altezza;
	}
	public Double getProfondità() {
		return profondità;
	}
	public void setProfondità(Double profondità) {
		this.profondità = profondità;
	}
	public String getProduttore() {
		return produttore;
	}
	public void setProduttore(String produttore) {
		this.produttore = produttore;
	}
	public Integer getAnno() {
		return anno;
	}
	public void setAnno(Integer anno) {
		this.anno = anno;
	}
	
	//costruttori
	public Computer(Double prezzo, Double peso, Double larghezza, Double altezza, Double profondità, String produttore,
			Integer anno) {
		//super();
		this.prezzo = prezzo;
		this.peso = peso;
		this.larghezza = larghezza;
		this.altezza = altezza;
		this.profondità = profondità;
		this.produttore = produttore;
		this.anno = anno;
	}
	
	public Computer () {
		
	}
	
	public Computer (Double prezzo, Double peso) {
		this.prezzo = prezzo;
		this.peso = peso;
	}
	
	public static Computer creaComputerCasuale() {
        Random rand = new Random();
        String[] produttori = {"S Management", "TechCorp", "ByteLabs", "Innovatech"};
        
        return new Computer(
            1000 + (5000 - 1000) * rand.nextDouble(), // Prezzo tra 1000 e 5000
            2 + (10 - 2) * rand.nextDouble(),          // Peso tra 2 e 10
            20 + (50 - 20) * rand.nextDouble(),       // Larghezza tra 20 e 50
            1 + (5 - 1) * rand.nextDouble(),          // Altezza tra 1 e 5
            10 + (50 - 10) * rand.nextDouble(),       // Profondità tra 10 e 50
            produttori[rand.nextInt(produttori.length)], // Produttore casuale
            1980 + rand.nextInt(44)                    // Anno tra 1980 e 2023
        );
    }
	
	@Override
	public String toString() {
		return "Computer [prezzo=" + prezzo + ", peso=" + peso + ", larghezza=" + larghezza + ", altezza=" + altezza
				+ ", profondità=" + profondità + ", produttore=" + produttore + ", anno=" + anno + "]";
	}
	
	
}