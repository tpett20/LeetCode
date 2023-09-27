// 238. Product of Array Except Self
/*
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
*/

var productExceptSelf = function(nums) {
    let product = 1
    const output = new Array(nums.length)
    output[0] = 1
    for (let i = 1; i < nums.length; i++) {
        product *= nums[i - 1]
        output[i] = product
    }
    product = 1
    for (let i = nums.length - 2; i >= 0; i--) {
        product *= nums[i + 1]
        output[i] *= product
    }
    return output
};

console.log(productExceptSelf([1, 2, 3, 4]))
console.log(productExceptSelf([-1, 1, 0, -3, 3]))