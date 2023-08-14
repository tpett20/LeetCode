// 215. Kth Largest Element in an Array
/*
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
*/

var findKthLargest = function(nums, k) {
    const posMap = {}
    const negMap = {}
    for (let num of nums) {
        if (num < 0) {
            num += 10001
            if (negMap[num]) {
                negMap[num]++
            } else {
                negMap[num] = 1
            }
        } else {
            if (posMap[num]) {
                posMap[num]++
            } else {
                posMap[num] = 1
            }
        }
    }
    let count = 0
    let target = (nums.length - k) + 1
    for (let num in negMap) {
        count += negMap[num]
        if (count >= target) {
            num = parseInt(num)
            num -= 10001
            return num
        }
    }
    for (let num in posMap) {
        count += posMap[num]
        if (count >= target) {
            return parseInt(num)
        }
    }
};

console.log(findKthLargest([-1000, -999, 15, 23, 23, -10000], 4))