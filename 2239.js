// 2239. Find Closest Number to Zero
// Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

var findClosestNumber = function(nums) {
    let minDiff = Infinity
    for (let num of nums) {
        let absNum = Math.abs(num)
        let absMinDiff = Math.abs(minDiff)
        if (absNum < absMinDiff) {
            minDiff = num
        } else if (absNum === absMinDiff && num > 0) {
            minDiff = absNum
        }
    }
    return minDiff
};

console.log(findClosestNumber([-4, -2, 1, 4, 8]))
console.log(findClosestNumber([2, -1, 1]))