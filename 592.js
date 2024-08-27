// 592. Fraction Addition and Subtraction
// Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
// The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

var fractionAddition = function(expression) {
    const fractions = []
    let fraction = expression[0]
    for (let i = 1; i < expression.length; i++) {
        const char = expression[i]
        if (char === "+" || char === "-") {
            fractions.push(fraction)
            fraction = ""
        }
        fraction += char
    }
    fractions.push(fraction)
    if (expression[0] !== "-") {
        fractions[0] = "+" + fractions[0]
    }
    const denoms = new Set()
    for (const fraction of fractions) {
        const parts = fraction.split("/")
        const denom = parseInt(parts[1])
        denoms.add(denom)
    }
    let denominator = 1
    for (const denom of denoms) {
        denominator *= denom
    }
    let numerator = 0
    for (const fraction of fractions) {
        const parts = fraction.split("/")
        const sign = parts[0][0]
        const denom = parseInt(parts[1])
        const multiplier = Math.floor(denominator / denom)
        const numer = parseInt(parts[0].slice(1)) * multiplier
        if (sign === "+") {
            numerator += numer
        } else {
            numerator -= numer
        }
    }
    let i = 2
    let ceil = Math.min(Math.abs(numerator), Math.abs(denominator))
    while (i <= ceil) {
        if (Math.abs(numerator % i) === 0 && Math.abs(denominator % i) === 0) {
            numerator = Math.floor(numerator / i)
            denominator = Math.floor(denominator / i)
            i = 2
            ceil = Math.min(Math.abs(numerator), Math.abs(denominator))
        } else {
            i++
        }
    }
    if (numerator === 0) {
        denominator = 1
    }
    return `${numerator}/${denominator}`
};

console.log(fractionAddition("-1/2+1/2+1/3"))
console.log(fractionAddition("1/3-1/2"))