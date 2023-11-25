// 1685. Sum of Absolute Differences in a Sorted Array
/*
You are given an integer array nums sorted in non-decreasing order.
Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
*/

var getSumAbsoluteDifferences = function(nums) {
    const output = []
    let sum = 0
    for (let i = 0; i < nums.length; i++) {
        output.push((nums[i] * i) - sum)
        sum += nums[i]
    }
    sum = 0
    for (let i = nums.length - 1; i >= 0; i--) {
        output[i] += sum - (nums[i] * (nums.length - 1 - i))
        sum += nums[i]
    }
    return output
};

console.log(getSumAbsoluteDifferences([2, 3, 5]))
console.log(getSumAbsoluteDifferences([1, 4, 6, 8, 10]))