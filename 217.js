// 217. Contains Duplicate
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

var containsDuplicate = function(nums) {
    const map = {}
    for (let num of nums) {
        if (map[num] !== undefined) {
            return true
        } else {
            map[num] = 1
        }
    }
    return false
};

console.log(containsDuplicate([1,2,3,1]))
console.log(containsDuplicate([1,2,3,4]))