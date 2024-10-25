public class main {

    public static void main(String[] args) {
        // Esempio di ciclo for semplice
        for (int i = 0; i < 10; i++) {
            System.out.println(i); // Stampa i numeri da 0 a 9
        }

        // Ciclo for che inizia con i1 = 20 e incrementa di 10, stampando solo se i1 < 25
        int i1 = 20;
        for (; i1 < 25; i1 += 10) {
            System.out.println(i1); // Stampa 20
        }

        // Ciclo for con una condizione impossibile (non viene eseguito)
        for (int i = 0; i < 1;) {
            System.out.println(i); // Questo ciclo non verrà mai eseguito
        }

        // Ciclo for per stampare i numeri pari da 2 a 20
        for (int i = 2; i <= 20; i += 2) {
            System.out.println(i); // Stampa i numeri pari da 2 a 20
        }

        // Ciclo for per stampare 10 numeri casuali
        for (int i = 0; i < 10; i++) {
            Double d = Math.random();
            System.out.println(d); // Stampa 10 numeri casuali
        }

        // Ciclo for per stampare numeri casuali con formattazione tramite printf
        for (int i = 1; i < 10; i++) {
            System.out.printf("%2d)\t%4.3g\n", i + 1, Math.random()); 
            // Stampa un numero da 1 a 9 e un numero casuale
        }

        // Esempio di printf: stampa di un intero
        int num = 42;
        System.out.printf("Numero intero: %d\n", num); // Stampa "Numero intero: 42"

        // Esempio di printf: stampa di un float con due decimali
        float floatNum = 3.14159f;
        System.out.printf("Float con due decimali: %.2f\n", floatNum); // Stampa "Float con due decimali: 3.14"

        // Esempio di printf: stampa di un char
        char letter = 'A';
        System.out.printf("Lettera: %c\n", letter); // Stampa "Lettera: A"

        // Esempio di printf: stampa di una stringa
        String text = "Hello, World!";
        System.out.printf("Stringa: %s\n", text); // Stampa "Stringa: Hello, World!"

        // Esempio di printf: stampa di un numero con padding a destra
        int numToPad = 7;
        System.out.printf("Numero con padding: |%5d|\n", numToPad); // Padding a destra
        System.out.printf("Numero con padding a sinistra: |%-5d|\n", numToPad); // Padding a sinistra

        // Esempio di printf: stampa di più variabili
        String name = "Alice";
        int age = 30;
        System.out.printf("%s ha %d anni.\n", name, age); // Stampa "Alice ha 30 anni."
    }
}
