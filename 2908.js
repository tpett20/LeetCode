// 2908. Minimum Sum of Mountain Triplets I
/*
You are given a 0-indexed array nums of integers.
A triplet of indices (i, j, k) is a mountain if:
    i < j < k
    nums[i] < nums[j] and nums[k] < nums[j]
Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
*/

var minimumSum = function(nums) {
    let minSum = Infinity
    let leftMin = nums[0]
    for (let i = 1; i < nums.length - 1; i++) {
        const mid = nums[i]
        let rightMin = Infinity
        for (let j = i + 1; j < nums.length; j++) {
            rightMin = Math.min(rightMin, nums[j])
        }
        if (leftMin < mid && mid > rightMin) {
            minSum = Math.min(minSum, leftMin + mid + rightMin)
        } else {
            leftMin = Math.min(leftMin, mid)
        }
    }
    return (minSum === Infinity) ? -1 : minSum
};

console.log(minimumSum([8, 9, 10, 1, 3, 2, 5]))
console.log(minimumSum([5, 4, 3, 4, 5]))