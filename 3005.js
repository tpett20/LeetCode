// 3005. Count Elements With Maximum Frequency
/*
You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.
*/

var maxFrequencyElements = function(nums) {
    let maxFreq = 0, qty = 0
    const freq = {}
    for (let num of nums) {
        freq[num] = freq[num] ? ++freq[num] : 1
        if (freq[num] === maxFreq) {
            qty++
        } else if (freq[num] > maxFreq) {
            qty = 1
            maxFreq = freq[num]
        }
    }
    return maxFreq * qty
};

console.log(maxFrequencyElements([1,2,2,3,1,4]))
console.log(maxFrequencyElements([1,2,3,4,5]))