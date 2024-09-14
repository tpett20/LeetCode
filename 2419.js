// 2419. Longest Subarray With Maximum Bitwise AND
/*
You are given an integer array nums of size n.
Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
- In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.
The bitwise AND of an array is the bitwise AND of all the numbers in it.
A subarray is a contiguous sequence of elements within an array.
*/

var longestSubarray = function(nums) {
    let count = 0, maxCount = 0
    let greatest = 0
    for (const num of nums) {
        if (num < greatest) {
            count = 0
        } else if (num > greatest) {
            count = 1
            maxCount = 1
            greatest = num
        } else {
            count++
        }
        maxCount = Math.max(count, maxCount)
    }
    return maxCount
};

console.log(longestSubarray([1, 2, 3, 3, 2, 2]))
console.log(longestSubarray([317824, 170330, 370216, 424297, 890759, 890759, 890759]))