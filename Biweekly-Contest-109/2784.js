// 2784. Check if Array is Good
// 🏆 Biweekly Contest 109
/*
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
Return true if the given array is good, otherwise return false.
Note: A permutation of integers represents an arrangement of these numbers.
*/

var isGood = function(nums) {
    let n = Math.max(...nums)
    let nCount = 0
    if (nums.length !== n + 1) return false
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === n) {
            nCount++
        }
    }
    if (nCount !== 2) return false
    for (let i = 1; i < n; i++) {
        if (!nums.includes(i)) {
            return false
        }
    }
    return true
};

console.log(isGood([2,1,3]))
console.log(isGood([1,3,3,2]))
console.log(isGood([1,1]))
console.log(isGood([3,4,4,1,2,1]))