// 191. Number of 1 Bits
// Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

var hammingWeight = function(n) {
    let oneBits = 0
    while (n > 0) {
        if (n % 2 === 1) oneBits++
        n = Math.floor(n / 2)
    }
    return oneBits
};