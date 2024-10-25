/*
         * Realizzare una classe Computer con i seguenti attributi
         * - Prezzo
         * - Peso
         * - Dimensioni (larghezza, altezza, profondità)
         * - Produttore
         * - Anno di produzione
         * 
         * Nel main creare degli oggetti di tipo Computer
         * e stampare il loro contenuto
         * 
         * NB: ricordate di utilizzare getter, setter e costruttore
         * generati da eclipse
         * 
         * Bonus: aggiungere un metodo alla classe Computer 
         * che stampi quanti oggetti (di tipo Computer) sono stati creati
*/


public class Computer {

    // Attributi
    private double prezzo;
    private double peso;
    private double larghezza;
    private double altezza;
    private double profondita;
    private String produttore;
    private int annoProduzione;
    
    // Variabile statica per contare il numero di oggetti creati
    private static int conteggioComputer = 0;

    // Costruttore
    public Computer(double prezzo, double peso, double larghezza, double altezza, double profondita, String produttore, int annoProduzione) {
        this.prezzo = prezzo;
        this.peso = peso;
        this.larghezza = larghezza;
        this.altezza = altezza;
        this.profondita = profondita;
        this.produttore = produttore;
        this.annoProduzione = annoProduzione;
        
        // Incrementa il conteggio ogni volta che un nuovo oggetto è creato
        conteggioComputer++;
    }

    // Getter e Setter per ogni attributo
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

    public double getProfondita() {
        return profondita;
    }

    public void setProfondita(double profondita) {
        this.profondita = profondita;
    }

    public String getProduttore() {
        return produttore;
    }

    public void setProduttore(String produttore) {
        this.produttore = produttore;
    }

    public int getAnnoProduzione() {
        return annoProduzione;
    }

    public void setAnnoProduzione(int annoProduzione) {
        this.annoProduzione = annoProduzione;
    }

    // Metodo per stampare il numero di oggetti creati
    public static void stampaConteggioComputer() {
        System.out.println("Numero di computer creati: " + conteggioComputer);
    }

    // Metodo per stampare le informazioni del computer
    public void stampaInformazioni() {
        System.out.println("Computer: ");
        System.out.println("Prezzo: " + prezzo + " €");
        System.out.println("Peso: " + peso + " kg");
        System.out.println("Dimensioni: " + larghezza + " x " + altezza + " x " + profondita + " cm");
        System.out.println("Produttore: " + produttore);
        System.out.println("Anno di produzione: " + annoProduzione);
    }
}

public class Main {

    public static void main(String[] args) {
        // Creazione degli oggetti di tipo Computer
        Computer computer01 = new Computer(1200.50, 2.5, 35.0, 25.0, 2.0, "Dell", 2023);
        Computer computer02 = new Computer(950.75, 3.0, 36.0, 26.0, 2.2, "HP", 2022);
        Computer computer03 = new Computer(1800.00, 1.8, 32.0, 22.0, 1.8, "Apple", 2024);
        Computer computer04 = new Computer(1200.50, 2.5, 35.0, 25.0, 2.0, "Dell", 2023);
        Computer computer05 = new Computer(950.75, 3.0, 36.0, 26.0, 2.2, "HP", 2022);
        Computer computer06 = new Computer(1800.00, 1.8, 32.0, 22.0, 1.8, "Apple", 2024);
        Computer computer07 = new Computer(1200.50, 2.5, 35.0, 25.0, 2.0, "Dell", 2023);
        Computer computer08 = new Computer(950.75, 3.0, 36.0, 26.0, 2.2, "HP", 2022);
        Computer computer09 = new Computer(1800.00, 1.8, 32.0, 22.0, 1.8, "Apple", 2024);
        Computer computer10 = new Computer(1800.00, 1.8, 32.0, 22.0, 1.8, "Apple", 2024);
        
        // Stampa delle informazioni per ogni computer
        computer1.stampaInformazioni();
        System.out.println(); // Spazio tra le informazioni
        computer2.stampaInformazioni();
        System.out.println();
        computer3.stampaInformazioni();
        System.out.println();
        
        // Stampa il numero di computer creati
        Computer.stampaConteggioComputer();
    }
}

