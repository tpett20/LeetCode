// 2729. Check if The Number is Fascinating
/*
You are given an integer n that consists of exactly 3 digits.
We call the number n fascinating if, after the following modification, the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0's:
    Concatenate n with the numbers 2 * n and 3 * n.
Return true if n is fascinating, or false otherwise.
Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.
*/

var isFascinating = function(n) {
    const nums = n.toString() + (n * 2).toString() + (n * 3).toString()
    if (nums.length !== 9) return false
    const seen = new Set()
    for (const num of nums) {
        if (num === "0" || seen.has(num)) return false
        seen.add(num)
    }
    return true
};

console.log(isFascinating(192))
console.log(isFascinating(100))