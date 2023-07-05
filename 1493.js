// 1493. Longest Subarray of 1's After Deleting One Element
/*
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
*/

var longestSubarray = function(nums) {
    let count1 = 0
    let count2 = 0
    let highCount = 0
    let inclZero = false
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            count2++
        } else {
            inclZero = true
            count1 = count2
            count2 = 0
        }
        if (count1 + count2 > highCount) {
            highCount = count1 + count2
        }
    }
    if (!inclZero) return highCount - 1
    return highCount
};

const result = longestSubarray([0,1,1,1,0,1,1,0,1])
console.log(`Output: ${result}, Expected: 5`)