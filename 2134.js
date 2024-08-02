// 2134. Minimum Swaps to Group All 1's Together II
/*
A swap is defined as taking two distinct positions in an array and swapping the values in them.
A circular array is defined as an array where we consider the first element and the last element to be adjacent.
Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.
*/

var minSwaps = function(nums) {
    let ones = 0
    for (const num of nums) {
        ones += num
    }
    if (ones === nums.length) return 0
    let l = 0, r = 0
    let currOnes = 0
    while (r < ones) {
        currOnes += nums[r]
        r++
    }
    let maxOnes = currOnes
    while (l < nums.length - 1) {
        currOnes -= nums[l]
        currOnes += nums[r]
        maxOnes = Math.max(currOnes, maxOnes)
        l++
        r++
        if (r === nums.length) {
            r = 0
        }
    }
    return ones - maxOnes
};

console.log(minSwaps([0,1,0,1,1,0,0]))
console.log(minSwaps([0,1,1,1,0,0,1,1,0]))
console.log(minSwaps([1,1,0,0,1]))