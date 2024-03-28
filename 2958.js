// 2958. Length of Longest Subarray With at Most K Frequency
/*
You are given an integer array nums and an integer k.
The frequency of an element x is the number of times it occurs in an array.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
*/

var maxSubarrayLength = function(nums, k) {
    let i = 0
    let maxLen = 1
    const freq = {[nums[0]]: 1}
    for (let j = 1; j < nums.length; j++) {
        freq[nums[j]] = freq[nums[j]] ? ++freq[nums[j]] : 1
        while (freq[nums[j]] > k) {
            freq[nums[i]]--
            i++
        }
        let len = j - i + 1
        if (len > maxLen) {
            maxLen = len
        }
    }
    return maxLen
};

console.log(maxSubarrayLength([1,2,3,1,2,3,1,2], 2))
console.log(maxSubarrayLength([1,2,1,2,1,2,1,2], 1))
console.log(maxSubarrayLength([5,5,5,5,5,5,5], 4))