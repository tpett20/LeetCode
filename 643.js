// 643. Maximum Average Subarray I
/*
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
*/

var findMaxAverage = function (nums, k) {
    let maxAvg
    let i = 0
    while (i <= nums.length - k) {
        let window = nums.slice(i, k + i)
        let avg = window.reduce((acc, num) => {
            return acc + num
        }) / k
        if (maxAvg === undefined) {
            maxAvg = avg
        } else if (avg > maxAvg) {
            maxAvg = avg
        }
        i++
    }
    return maxAvg
};

console.log(findMaxAverage([1, 12, -5, -6, 50, 3], 4))