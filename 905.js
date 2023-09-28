// 905. Sort Array By Parity
// Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
// Return any array that satisfies this condition.

var sortArrayByParity = function(nums) {
    const odds = []
    let i = 0
    for (let num of nums) {
        if (num % 2 === 0) {
            nums[i] = num
            i++
        } else {
            odds.push(num)
        }
    }
    for (let num of odds) {
        nums[i] = num
        i++
    }
    return nums
};

console.log(sortArrayByParity([3,1,2,4]))