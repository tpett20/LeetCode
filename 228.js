// 228. Summary Ranges
/*
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b
*/

var summaryRanges = function(nums) {
    if (nums[0] === undefined) return nums
    const ranges = []
    let range = [nums[0]]
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1] + 1) {
            range[1] = nums[i] 
        } else {
            ranges.push(range[1] === undefined ? `${range[0]}` : `${range[0]}->${range[1]}`)
            range = [nums[i]]
        }
    }
    ranges.push(range[1] === undefined ? `${range[0]}` : `${range[0]}->${range[1]}`)
    return ranges
};

console.log(summaryRanges([0,2,3,4,6,8,9]))


// With Preplanned Pseudocode
var pseudocode = function(nums) {
    if (nums[0] === undefined) return nums
    // create an output array to store all the ranges
    const ranges = []
    // create a sub array to hold each range that will fill the output array
    // initialize it with the first value of nums
    let range = [nums[0]]
    // iterate over each number in nums, starting with the second
    for (let i = 1; i < nums.length; i++) {
        // if the current number is equal to the previous number + 1, set the second value of the sub array (range[1]) equal to the current number, making it the closing paramater of the range
        if (nums[i] === nums[i - 1] + 1) {
            range[1] = nums[i] 
        // else (if the current number is not equal to previous + 1), push the values of the current sub array to the output array as a string in the specified format 
        } else {
            ranges.push(range[1] === undefined ? `${range[0]}` : `${range[0]}->${range[1]}`)
            // reset the sub array to hold the current number 
            range = [nums[i]]
        }
    }
    // push the last sub array to the output array
    ranges.push(range[1] === undefined ? `${range[0]}` : `${range[0]}->${range[1]}`)
    // return the output array
    return ranges
};