// 209. Minimum Size Subarray Sum
// Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

var minSubArrayLen = function(target, nums) {
    let first = 0
    let second = 0
    let tempSum = nums[first]
    let len = 1
    let minLen = nums.length + 1
    while (second < nums.length) {
        if (tempSum > target) {
            if (len < minLen) minLen = len
            tempSum -= nums[first]
            first++
            len--
        } else if (tempSum < target) {
            second++
            tempSum += nums[second]
            len++
        } else {
            if (len < minLen) minLen = len
            tempSum -= nums[first]
            first++
            second++
            tempSum += nums[second]
        }
    }
    return minLen < nums.length + 1 ? minLen : 0
};

console.log(minSubArrayLen(7, [2,3,1,2,4,3]))
console.log(minSubArrayLen(15, [1,2,3,4,5]))