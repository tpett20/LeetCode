// 67. Add Binary
// Given two binary strings a and b, return their sum as a binary string.

var addBinary = function(a, b) {
    let sum = ''
    let i = a.length > b.length ? a.length : b.length
    let aDiff = i - a.length
    let bDiff = i - b.length
    a = '0'.repeat(aDiff) + a
    b = '0'.repeat(bDiff) + b
    i--
    let remainder = 0
    while (i >= 0) {
        if (a[i] === '0' && b[i] === '0') {
            if (remainder) {
                sum = '1' + sum
                remainder = 0
            }
            else sum = '0' + sum
        } else if (a[i] === '1' && b[i] === '1') {
            if (remainder) sum = '1' + sum
            else {
                sum = '0' + sum
                remainder = 1
            }
        } else {
            if (remainder) sum = '0' + sum
            else sum = '1' + sum
        }
        i--
    }
    if (remainder) sum = '1' + sum
    return sum
};

let num1 = '1011'
let num2 = '101'
let sum = addBinary(num1, num2)
console.log(`${num1} + ${num2} = ${sum}`)

let int1 = parseInt(num1, 2)
let int2 = parseInt(num2, 2)
let intSum = int1 + int2
console.log(`(${int1} + ${int2} = ${intSum})`)