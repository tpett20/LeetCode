// 1749. Maximum Absolute Sum of Any Subarray
/*
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.
Note that abs(x) is defined as follows:
    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.
*/

var maxAbsoluteSum = function(nums) {
    let sum = nums[0]
    let posSum = sum
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < 0 && -nums[i] >= posSum) {
            sum = (i < nums.length - 1) ? nums[i + 1] : nums[i]
            i++
        } else if (sum < 0 && nums[i] > 0) {
            sum = nums[i]
        } else {
            sum += nums[i]
        }
        posSum = Math.max(posSum, sum)
    }
    sum = nums[0]
    let negSum = sum
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > 0 && -nums[i] <= negSum) {
            sum = (i < nums.length - 1) ? nums[i + 1] : nums[i]
            i++
        } else if (sum > 0 && nums[i] < 0) {
            sum = nums[i]
        } else {
            sum += nums[i]
        }
        negSum = Math.min(negSum, sum)
    }
    return Math.max(posSum, -negSum)
};

console.log(maxAbsoluteSum([16, -1, -2, -3, -4, -5, 100]))
console.log(maxAbsoluteSum([-16, 15, -100]))