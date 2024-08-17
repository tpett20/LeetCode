// 1539. Kth Missing Positive Number
// Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
// Return the kth positive integer that is missing from this array.

var findKthPositive = function(arr, k) {
    let flr = 0
    let ceil = arr.length - 1
    while (flr <= ceil) {
        const mid = Math.floor((flr + ceil) / 2)
        const diff = arr[mid] - (mid + 1)
        if (diff < k) {
            flr = mid + 1
        } else {
            ceil = mid - 1
        } 
    }
    if (flr === 0) {
        return k
    }
    flr -= 1
    const flrDiff = arr[flr] - (flr + 1)
    const kDiff = k - flrDiff
    return arr[flr] + kDiff
};

console.log(findKthPositive([2,3,4,7,11], 5))
console.log(findKthPositive([1,2,3,4], 2))
console.log(findKthPositive([5,6,7,8], 2))