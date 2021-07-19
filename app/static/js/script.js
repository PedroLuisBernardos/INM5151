/* JS général de l'application */

function calculationTax() {
    let amount = document.getElementById("amount").value;
    let tax = document.getElementById("tax").value;
    tax = tax / 100;
    let priceWithTax = amount * tax;
    let total = parseFloat(amount) + parseFloat(priceWithTax);
    document.getElementById("amount").value = total;
}