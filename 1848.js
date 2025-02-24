// 1848. Minimum Distance to the Target Element
/*
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.
Return abs(i - start).
It is guaranteed that target exists in nums.
*/

var getMinDistance = function(nums, target, start) {
    const n = nums.length
    let l = start
    let r = start
    while (true) {
        if (nums[l] === target) {
            return start - l
        }
        if (nums[r] === target) {
            return r - start
        }
        l = (l > 0) ? l - 1 : l
        r = (r < n - 1) ? r + 1 : r
    }
};

console.log(getMinDistance([1, 2, 3, 4, 3, 2, 1], 1, 3))