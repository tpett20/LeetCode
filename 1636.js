// 1636. Sort Array by Increasing Frequency
// Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
// Return the sorted array.

var frequencySort = function(nums) {
    const freq = {}
    for (const num of nums) {
        freq[num] = freq[num] ? ++freq[num] : 1
    }
    return nums.toSorted((a, b) => {
        const diff = freq[a] - freq[b]
        if (diff === 0) {
            return b - a
        }
        return diff
    })
};

console.log(frequencySort([1,1,2,2,2,3]))
console.log(frequencySort([2,3,1,3,2]))
console.log(frequencySort([-1,1,-6,4,5,-6,1,4,1]))