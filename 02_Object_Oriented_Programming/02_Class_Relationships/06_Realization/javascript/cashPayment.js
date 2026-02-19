/**
 * Realization — CashPayment in JavaScript.
 */

class CashPayment {
  get paymentMethod() {
    return "Cash";
  }

  pay(amount) {
    console.log(`Paid $${amount} using Cash.`);
  }
}

module.exports = CashPayment;
