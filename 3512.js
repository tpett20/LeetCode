// 3512. Minimum Operations to Make Array Sum Divisible by K
// You are given an integer array nums and an integer k. You can perform the following operation any number of times:
    // Select an index i and replace nums[i] with nums[i] - 1.
// Return the minimum number of operations required to make the sum of the array divisible by k.

var minOperations = function(nums, k) {
    if (k === 1) return 0
    let sum = 0
    for (const num of nums) {
        sum += num
    }
    return sum % k
};

console.log(minOperations([3, 9, 7], 5))