// 3010. Divide an Array Into Subarrays With Minimum Cost I
// You are given an array of integers nums of length n.
// The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.
// You need to divide nums into 3 disjoint contiguous subarrays.
// Return the minimum possible sum of the cost of these subarrays.

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumCost = function(nums) {
    let low1 = Infinity
    let low2 = Infinity
    for (let i = 1; i < nums.length; i++) {
        const curr = nums[i]
        if (curr < low1) {
            low2 = low1
            low1 = curr
        } else if (curr < low2) {
            low2 = curr
        }
    }
    return nums[0] + low1 + low2
};

console.log(minimumCost([10, 3, 1, 1]))