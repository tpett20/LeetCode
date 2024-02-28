// 1394. Find Lucky Integer in an Array
// Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
// Return the largest lucky integer in the array. If there is no lucky integer return -1.

var findLucky = function(arr) {
    let luckyNum = -1
    const freq = {}
    for (let num of arr) {
        freq[num] = freq[num] ? ++freq[num] : 1
    }
    for (let num in freq) {
        num = parseInt(num)
        if (num === freq[num]) {
            luckyNum = Math.max(num, luckyNum)
        }
    }
    return luckyNum
};

console.log(findLucky([2,2,3,4]))
console.log(findLucky([1,2,2,3,3,3]))
console.log(findLucky([2,2,2,3,3]))