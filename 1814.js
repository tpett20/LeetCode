// 1814. Count Nice Pairs in an Array
/*
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:
    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 10^9 + 7.
*/

var countNicePairs = function(nums) {
    let pairs = 0
    const map = {}
    for (let num of nums) {
        const key = getKey(num)
        if (!map[key]) {
            map[key] = 1
        } else {
            pairs += map[key]
            map[key]++
        }
    }
    return pairs % (10 ** 9 + 7)

    function getKey(num) {
        return num - parseInt(num.toString().split('').reverse().join(''))
    }
};

console.log(countNicePairs([42, 11, 1, 97]))
console.log(countNicePairs([13, 10, 35, 24, 76]))