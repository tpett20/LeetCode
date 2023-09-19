// 287. Find the Duplicate Number
/*
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
*/

// 🧠 Inspiration for Code Logic:
// https://youtu.be/pKO9UjSeLew?si=Pk9QdasCy_T2g1Bw

var findDuplicate = function (nums) {
    let slow = 0
    let fast = 0
    while (true) {
        slow = nums[slow]
        fast = nums[nums[fast]]
        if (slow === fast) {
            break
        }
    }
    let tracer = 0
    while (tracer !== slow) {
        slow = nums[slow]
        tracer = nums[tracer]
    }
    return tracer
};

console.log(findDuplicate([1, 3, 4, 2, 2]))
console.log(findDuplicate([3, 1, 3, 4, 2]))
console.log(findDuplicate([4, 1, 2, 3, 3]))