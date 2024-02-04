// 1822. Sign of the Product of an Array
/*
There is a function signFunc(x) that returns:
    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).
*/

var arraySign = function(nums) {
    let oddNeg = false
    for (let num of nums) {
        if (num < 0) oddNeg = !oddNeg
        else if (num === 0) return 0
    }
    return oddNeg ? -1 : 1
};

console.log(arraySign([-1, -2, -3, -4, 3, 2, 1]))
console.log(arraySign([1, 5, 0, 2, -3]))
console.log(arraySign([-1, 1, -1, 1, -1]))