
public class Computer {

	//Dichiaraziione
	private double prezzo;
	private double peso;
	private double larghezza;
	private double altezza;
	private double profondità;
	private String produttore;
	private Integer anno;
	
	public Computer(private double prezzo, 
			private double peso, 
			private double larghezza,
			private double altezza,
			private double profondità,
			private String produttore,
			private Integer anno,
			counter ++;)
		{
			this.peso = peso;
			this.altezza = altezza;
			this.prezzo = prezzo;
			this.larghezza = larghezza;
			this.altezza =profonodità;
			this.altezza 
		}
	
	//Getter e Setter
	public double getPrezzo() {
		return prezzo;
	}
	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}
	public double getPeso() {
		return peso;
	}
	public void setPeso(double peso) {
		this.peso = peso;
	}
	public double getLarghezza() {
		return larghezza;
	}
	public void setLarghezza(double larghezza) {
		this.larghezza = larghezza;
	}
	public double getAltezza() {
		return altezza;
	}
	public void setAltezza(double altezza) {
		this.altezza = altezza;
	}
	public double getProfondità() {
		return profondità;
	}
	public void setProfondità(double profondità) {
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
	
	
}
/*
 * realizzare una classe computer con i seguenti attributi:
 * prezzo
 * peso
 * dimnesioni (larghezza, altezza, profondità
 * produttore
 * anno di produzione
 * 
 * nel main creare degli oggetti di tipo computer
 * e stampare il loro contenuto 
 * 
 * NB: ricorda di utilizzare getter e setter e costruttore
 * generati da eclipse
 * 
 * Bonus: aggiungere un metodo alla classe computer 
 * che stampi quantyi oggetti sono stati creati
 */