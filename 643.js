// 643. Maximum Average Subarray I
/*
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
*/

var findMaxAverage = function (nums, k) {
    let sum = nums.slice(0, k).reduce((acc, num) => {
        return acc + num
    })
    let maxAvg = sum / k
    let start = 0
    for (let i = k; i < nums.length; i++) {
        sum -= nums[start]
        sum += nums[i]
        let avg = sum / k
        if (avg > maxAvg) {
            maxAvg = avg
        }
        start++
    }
    return maxAvg
};

console.log(findMaxAverage([1, 12, -5, -6, 50, 3], 4))