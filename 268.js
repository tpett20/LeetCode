// 268. Missing Number
// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

var missingNumber = function(nums) {
    const map = {}
    for (let num of nums) {
        map[num] = true
    }
    for (let i = 0; i <= nums.length; i++) {
        if (map[i] === undefined) {
            return i
        }
    }
};

console.log(missingNumber([3,0,1]))
console.log(missingNumber([0,1]))
console.log(missingNumber([9,6,4,2,3,5,7,0,1]))

// Alt Solution with Better Memory, but Worse Runtime
/*
var missingNumber = function(nums) {
    for (let i = 0; i <= nums.length; i++) {
        if (!nums.includes(i)) {
            return i
        }
    }
};
*/