// 1502. Can Make Arithmetic Progression From Sequence
// A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
// Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

var canMakeArithmeticProgression = function(arr) {
    arr.sort((a, b) => a - b)
    let diff = arr[1] - arr[0]
    for (let i = 2; i < arr.length; i++) {
        if (arr[i] - arr[i - 1] !== diff) {
            return false
        }
    }
    return true
};

console.log(canMakeArithmeticProgression([3,5,1]))
console.log(canMakeArithmeticProgression([2,4,1]))