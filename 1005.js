// 1005. Maximize Sum Of Array After K Negations
/*
Given an integer array nums and an integer k, modify the array in the following way:
- choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.
Return the largest possible sum of the array after modifying it in this way.
*/

var largestSumAfterKNegations = function (nums, k) {
    nums.sort((a, b) => a - b)
    let i = 0
    let kCache = k
    while (i < kCache && nums[i] < 0) {
        nums[i] = Math.abs(nums[i])
        k--
        i++
    }
    if (k === 0 || nums[i] === 0 || k % 2 === 0) {
        return getSum(nums)
    }
    nums.sort((a, b) => a - b)
    nums[0] = -Math.abs(nums[0])
    return getSum(nums)

    function getSum(arr) {
        let sum = 0
        for (let num of arr) {
            sum += num
        }
        return sum
    }
};

console.log(largestSumAfterKNegations([4,2,3], 1))
console.log(largestSumAfterKNegations([3,-1,0,2], 3))
console.log(largestSumAfterKNegations([2,-3,-1,5,-4], 2))