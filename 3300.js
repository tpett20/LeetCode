// 3300. Minimum Element After Replacement With Digit Sum
/*
You are given an integer array nums.
You replace each element in nums with the sum of its digits.
Return the minimum element in nums after all replacements.
*/

var minElement = function(nums) {
    let minSum = Infinity
    for (const num of nums) {
        let sum = 0
        if (num < 10) {
            sum = num
        } else {
            const numStr = num.toString()
            for (const digit of numStr) {
                sum += parseInt(digit)
            }
        }
        minSum = Math.min(sum, minSum)
    }
    return minSum
};

console.log(minElement([10, 12, 13, 14]))
console.log(minElement([999, 19, 199]))