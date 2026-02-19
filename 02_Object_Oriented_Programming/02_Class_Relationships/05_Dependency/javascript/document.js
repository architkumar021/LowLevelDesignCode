/**
 * Dependency — Document class in JavaScript.
 *
 * A Document depends on a Printer only during the printDocument() call.
 */

class Document {
  #title;
  #content;

  constructor(title, content) {
    this.#title = title;
    this.#content = content;
  }

  get title() {
    return this.#title;
  }

  get content() {
    return this.#content;
  }

  /**
   * Dependency: Printer is passed in and used only here — no permanent link.
   */
  printDocument(printer) {
    console.log(`Document: ${this.#title}`);
    printer.print(this.#content);
  }

  toString() {
    return `Document(${this.#title})`;
  }
}

module.exports = Document;
