// 2913. Subarrays Distinct Element Sum of Squares I
/*
You are given a 0-indexed integer array nums.
The distinct count of a subarray of nums is defined as:
- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
*/

var sumCounts = function(nums) {
    let output = 0
    for (let i = 0; i < nums.length; i++) {
        output += 1
        for (let j = i + 1; j < nums.length; j++) {
            const subArr = nums.slice(i, j + 1)
            const subSet = new Set(subArr)
            output += subSet.size ** 2
        }
    }
    return output
};

console.log(sumCounts([1,2,1]))
console.log(sumCounts([1,1]))