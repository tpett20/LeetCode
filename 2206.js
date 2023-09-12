// 2206. Divide Array Into Equal Pairs
/*
You are given an integer array nums consisting of 2 * n integers.
You need to divide nums into n pairs such that:
- Each element belongs to exactly one pair.
- The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
*/

var divideArray = function(nums) {
    if (nums.length % 2 !== 0) return false
    const map = {}
    for (let num of nums) {
        map[num] = map[num] ? map[num] + 1 : 1
    }
    for (let num in map) {
        if (map[num] % 2 !== 0) return false
    }
    return true
};

console.log(divideArray([3,2,3,2,2,2]))
console.log(divideArray([1,2,3,4]))