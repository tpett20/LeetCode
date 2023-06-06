// 69. Sqrt(x)
/*
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
*/

var mySqrt = function(x) {
    if (x <= 1) return x
    let max = x
    let min = 0
    const avg = (min, max) => Math.floor((min + max) / 2)
    let i = avg(min, max)
    while (i * i !== x) {
        if (i * i < x && (i + 1) * (i + 1) > x) {
            return i
        } else if (i * i > x) {
            max = i
            i = avg(min, max)
        } else if (i * i < x) {
            min = i
            i = avg(min, max)
        }
    }
    return i
};

console.log(mySqrt(2))