// 1460. Make Two Arrays Equal by Reversing Subarrays
// You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.
// Return true if you can make arr equal to target or false otherwise.

var canBeEqual = function(target, arr) {
    const targetMap = {}
    for (const num of target) {
        targetMap[num] = targetMap[num] ? ++targetMap[num] : 1
    }
    for (const num of arr) {
        if (targetMap[num]) {
            targetMap[num]--
        } else {
            return false
        }
    }
    return true
};

console.log(canBeEqual([1,2,3,4], [2,4,1,3]))
console.log(canBeEqual([3,7,9], [3,7,11]))