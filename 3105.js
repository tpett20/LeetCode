// 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
// You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

var longestMonotonicSubarray = function(nums) {
    let inc = nums[1] > nums[0]
    let maxLen = 1
    let len = 1
    for (let i = 1; i < nums.length; i++) {
        if (
            nums[i] > nums[i - 1] && inc ||
            nums[i] < nums[i - 1] && !inc
        ) {
            len += 1
            maxLen = Math.max(len, maxLen)
        } else if (nums[i] === nums[i - 1]) {
            len = 1
        } else {
            len = 2
            maxLen = Math.max(len, maxLen)
            inc = (nums[i] > nums[i - 1]) ? true : false
        }
    }
    return maxLen
};

console.log(longestMonotonicSubarray([1, 4, 3, 3, 2]))
console.log(longestMonotonicSubarray([1, 1, 5]))