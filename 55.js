// 55. Jump Game
/*
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
*/

var canJump = function(nums) {
    if (nums[0] >= nums.length - 1) return true
    let i = nums.length - 1
    let j = nums.length - 2
    while (j >= 0) {
        if (nums[j] >= i - j) {
            i = j
        }
        j--
    }
    if (i === 0) return true
    else return false
};

console.log(canJump([2,3,1,1,4]))
console.log(canJump([3,2,1,0,4]))