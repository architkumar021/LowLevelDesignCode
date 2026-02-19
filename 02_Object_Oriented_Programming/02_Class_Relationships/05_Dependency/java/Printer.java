/**
 * Dependency — Printer class.
 *
 * Key concept: Document USES Printer temporarily (method parameter).
 * There is no permanent link — Printer is only needed during a specific operation.
 */
public class Printer {

    private String printerName;

    public Printer(String printerName) {
        this.printerName = printerName;
    }

    public String getPrinterName() {
        return printerName;
    }

    public void print(String message) {
        System.out.println("[" + printerName + "] Printing: " + message);
    }

    @Override
    public String toString() {
        return "Printer(" + printerName + ")";
    }
}
