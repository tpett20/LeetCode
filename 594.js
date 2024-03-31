// 594. Longest Harmonious Subsequence
/*
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
*/

var findLHS = function(nums) {
    const freq = {}
    for (let num of nums) {
        freq[num] = freq[num] ? ++freq[num] : 1
    }
    let vals = new Set(nums)
    vals = Array.from(vals)
    vals.sort((a, b) => a - b)
    let maxLen = 0
    for (let i = 1; i < vals.length; i++) {
        let curr = vals[i]
        let prev = vals[i - 1]
        if (curr - prev === 1) {
            let len = freq[curr] + freq[prev]
            if (len > maxLen) {
                maxLen = len
            }
        }
    }
    return maxLen
};

console.log(findLHS([1,3,2,2,5,2,3,7]))