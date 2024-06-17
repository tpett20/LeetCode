// 633. Sum of Square Numbers
// Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.

var judgeSquareSum = function(c) {
    let flr = 0
    let ceil = Math.floor(Math.sqrt(c))
    while (flr <= ceil) {
        const sqSum = flr * flr + ceil * ceil
        if (sqSum < c) {
            flr++
        } else if (sqSum > c) {
            ceil--
        } else {
            return true
        }
    }
    return false
};

console.log(judgeSquareSum(5))
console.log(judgeSquareSum(3))