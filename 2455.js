// 2455. Average Value of Even Numbers That Are Divisible by Three
// Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
// Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

var averageValue = function(nums) {
    let sum = 0
    let count = 0
    for (const num of nums) {
        if (num % 6 === 0) {
            sum += num
            count++
        }
    }
    return count ? Math.floor(sum / count) : 0
};

console.log(averageValue([1, 3, 6, 9, 12, 15]))