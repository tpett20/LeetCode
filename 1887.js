// 1887. Reduction Operations to Make the Array Elements Equal
/*
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:
Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.
*/

var reductionOperations = function(nums) {
    nums.sort((a, b) => a - b)
    let operations = 0
    let ceil = nums[0]
    let i = 1
    while (nums[i] === ceil) {
        i++
    }
    let levels = 0
    for (i; i < nums.length; i++) {
        let num = nums[i]
        if (num !== ceil) {
            ceil = num
            levels++
        }
        operations += levels
    }
    return operations
};

console.log(reductionOperations([5, 1, 3]))
console.log(reductionOperations([1, 1, 1]))
console.log(reductionOperations([1, 1, 2, 2, 3]))