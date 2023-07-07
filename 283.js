// 283. Move Zeroes
/*
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
*/

var moveZeroes = function(nums) {
    let count = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            nums[count] = nums[i]
            count++
        }
    }
    for (let i = count; i < nums.length; i++) {
        nums[i] = 0
    }
};

const nums = [0,1,0,3,12]
console.log(nums, '= Input')
moveZeroes(nums)
console.log(nums, '= Output')