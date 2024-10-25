import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Inizializza il contatore
        int contatore = 0;

        // Lista per memorizzare i computer generati
        List<Computer> computers = new ArrayList<>();

        // Aggiunta di computer a mano
        Computer com1 = new Computer();
        com1.setAltezza(1.5);
        com1.setAnno(2023);
        com1.setLarghezza(35.0);
        com1.setPeso(4.5);
        com1.setPrezzo(4500.);
        com1.setProduttore("S Management");
        com1.setProfondità(25.0);
        computers.add(com1); // Aggiungi a lista

        Computer com2 = new Computer(454., 7.2, 23., 4., 65., "S management", 1990);
        computers.add(com2); // Aggiungi a lista

        Computer com3 = new Computer(454., 7.2);
        com3.setAltezza(1.5);
        com3.setAnno(2023);
        com3.setLarghezza(35.0);
        com3.setPeso(4.5);
        com3.setPrezzo(4500.);
        com3.setProduttore("S Management");
        com3.setProfondità(25.0);
        computers.add(com3); // Aggiungi a lista

        // Genera e aggiungi 10 computer casuali
        for (int i = 0; i < 10; i++) {
            computers.add(Computer.creaComputerCasuale());
        }

        // Stampa i computer
        for (Computer computer : computers) {
            System.out.println(computer);
        }

        // Incrementa il contatore
        contatore++;

        System.out.println("Ciao");
    }
}
