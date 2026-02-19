/**
 * Driver — demonstrates Dependency (USES-A temporarily).
 *
 * A Document uses a Printer only when printing.
 * Different printers can be used each time.
 */
public class DependencyDemo {

    public static void main(String[] args) {
        Document doc = new Document("Report", "Hello, World!");
        Printer officePrinter = new Printer("Office HP");
        Printer homePrinter = new Printer("Home Canon");

        // Same document, different printers — dependency is temporary
        doc.printDocument(officePrinter);
        System.out.println();
        doc.printDocument(homePrinter);
    }
}

/*
Expected Output:
Document: Report
[Office HP] Printing: Hello, World!

Document: Report
[Home Canon] Printing: Hello, World!
*/
