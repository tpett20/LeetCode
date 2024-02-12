// 169. Majority Element
// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

var majorityElement = function(nums) {
    const maj = Math.floor(nums.length / 2)
    let majEl = nums[0]
    let count = 0
    for (let num of nums) {
        if (num === majEl) count++
        else count--
        if (count === 0) {
            majEl = num
            count++
        }
        if (count > maj) return majEl
    }
    return majEl
};

console.log(majorityElement([3, 2, 3]))
console.log(majorityElement([2, 2, 1, 1, 1, 2, 2]))