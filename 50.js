// 50. Pow(x, n)
// Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

var myPow = function(x, n) {
    if (x === 1) return 1
    else if (x === -1) {
        if (n % 2 === 0) return 1
        else return -1
    }
    let product = 1
    for (let i = 1; i <= Math.abs(n); i++) {
        product *= x
    }
    if (n >= 0) {
        return product 
    } else {
        return 1 / product
    }
};

console.log(myPow(2, 10))
console.log(myPow(2.1, 3))
console.log(myPow(2, -2))
console.log(myPow(-1, 2147483647))