/**
 * Realization — CreditCardPayment in JavaScript.
 *
 * JavaScript has no formal interfaces, so we use duck-typing.
 * Each "realization" class must implement pay(amount) and paymentMethod getter.
 */

class CreditCardPayment {
  #cardNumber;

  constructor(cardNumber) {
    this.#cardNumber = cardNumber;
  }

  get paymentMethod() {
    return "Credit Card";
  }

  pay(amount) {
    const masked = "****-" + this.#cardNumber.slice(-4);
    console.log(`Paid $${amount} using Credit Card (${masked}).`);
  }
}

module.exports = CreditCardPayment;
