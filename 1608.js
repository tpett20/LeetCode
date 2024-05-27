// 1608. Special Array With X Elements Greater Than or Equal X
/*
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
*/

var specialArray = function(nums) {
    const sorted = nums.toSorted((a, b) => a - b)
    if (sorted[0] >= nums.length) {
        return nums.length
    }
    for (let i = 1; i < sorted.length; i++) {
        const r = sorted.length - i
        if (sorted[i] >= r && sorted[i - 1] < r) {
            return r
        }
    }
    return -1
};

console.log(specialArray([3,5]))
console.log(specialArray([0,0]))
console.log(specialArray([0,4,3,0,4]))
console.log(specialArray([3,6,7,7,0]))
console.log(specialArray([1,3,9,5,11,2,11,0,4,2]))