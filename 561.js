// 561. Array Partition
// Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

var arrayPairSum = function(nums) {
    const arr = nums.toSorted((a, b) => a - b)
    let sum = 0
    for (let i = 0; i < arr.length; i += 2) {
        sum += arr[i]
    }
    return sum
};

console.log(arrayPairSum([1,4,3,2]))
console.log(arrayPairSum([6,2,6,5,1,2]))