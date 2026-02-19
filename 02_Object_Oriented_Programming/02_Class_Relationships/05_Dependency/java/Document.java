/**
 * Dependency — Document class.
 *
 * A Document depends on a Printer to perform printing,
 * but only uses it temporarily (as a method parameter).
 * It does NOT store a reference to the Printer.
 */
public class Document {

    private String title;
    private String content;

    public Document(String title, String content) {
        this.title = title;
        this.content = content;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    /**
     * Dependency: Document uses Printer to print its content.
     * Printer is passed in and used only here — no permanent link.
     */
    public void printDocument(Printer printer) {
        System.out.println("Document: " + title);
        printer.print(content);
    }

    @Override
    public String toString() {
        return "Document(" + title + ")";
    }
}
