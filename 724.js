// 724. Find Pivot Index
/*
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
*/

var pivotIndex = function(nums) {
    let sum = nums.reduce((acc, num) => {
        return acc + num
    })
    sum -= nums[0]
    if (sum === 0) return 0
    let leftSum = 0
    for (let i = 1; i < nums.length; i++) {
        leftSum += nums[i - 1]
        sum -= nums[i]
        if (leftSum === sum) {
            return i
        }
    }
    return -1
};

console.log(pivotIndex([1,7,3,6,5,6]), 'Expected: 3')