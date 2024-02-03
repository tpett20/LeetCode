// 693. Binary Number with Alternating Bits
// Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

var hasAlternatingBits = function(n) {
    let lastBit = -1
    while (n > 0) {
        let r = n % 2
        if (r === lastBit) return false
        lastBit = r
        n = Math.floor(n / 2)
    }
    return true
};

console.log(hasAlternatingBits(5))
console.log(hasAlternatingBits(7))
console.log(hasAlternatingBits(11))