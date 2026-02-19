/**
 * Realization — UpiPayment in JavaScript.
 */

class UpiPayment {
  #upiId;

  constructor(upiId) {
    this.#upiId = upiId;
  }

  get paymentMethod() {
    return "UPI";
  }

  pay(amount) {
    console.log(`Paid $${amount} via UPI (${this.#upiId}).`);
  }
}

module.exports = UpiPayment;
