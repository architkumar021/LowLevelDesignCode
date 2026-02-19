/**
 * Driver — demonstrates Realization (interface implementation via duck-typing).
 * Run: node main.js
 */

const CreditCardPayment = require("./creditCardPayment");
const CashPayment = require("./cashPayment");
const UpiPayment = require("./upiPayment");

function processPayment(payment, amount) {
  process.stdout.write(`[${payment.paymentMethod}] `);
  payment.pay(amount);
}

const creditCard = new CreditCardPayment("4111111111111234");
const cash = new CashPayment();
const upi = new UpiPayment("alice@upi");

processPayment(creditCard, 99.99);
processPayment(cash, 25.0);
processPayment(upi, 150.5);

/*
Expected Output:
[Credit Card] Paid $99.99 using Credit Card (****-1234).
[Cash] Paid $25 using Cash.
[UPI] Paid $150.5 via UPI (alice@upi).
*/
