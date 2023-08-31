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