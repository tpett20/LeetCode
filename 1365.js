// 1365. How Many Numbers Are Smaller Than the Current Number
/*
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
*/

var smallerNumbersThanCurrent = function(nums) {
    const copy = [...nums]
    const output = []
    nums.sort((a, b) => a - b)
    for (let i = 0; i < nums.length; i++) {
        output.push(nums.indexOf(copy[i]))
    }
    return output
};

console.log(smallerNumbersThanCurrent([8,1,2,2,3]))