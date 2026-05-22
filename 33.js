// 33. Search in Rotated Sorted Array
// There is an integer array nums sorted in ascending order (with distinct values).
// Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
// Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
// You must write an algorithm with O(log n) runtime complexity.

var search = function(nums, target) {
    let flr = 0
    let ceil = nums.length - 1
    while (flr <= ceil) {
        const midIdx = Math.floor((ceil + flr) / 2)
        const lt = nums[flr]
        const md = nums[midIdx]
        const rt = nums[ceil]
        if (lt === target) return flr
        if (md === target) return midIdx
        if (rt === target) return ceil
        if (rt < target && lt > target) return -1
        if (lt < md) {
            if (lt < target && target < md) {
                ceil = midIdx - 1
            } else {
                flr = midIdx + 1
            }
        } else {
            if (md < target && target < rt) {
                flr = midIdx + 1
            } else {
                ceil = midIdx - 1
            }
        }
    }
    return -1
};

console.log(search([4, 5, 6, 7, 0, 1, 2], 0))
console.log(search([4, 5, 6, 7, 0, 1, 2], 3))
console.log(search([4, 6, 7, 8, 0, 1, 2, 3], 5))