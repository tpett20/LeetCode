// 2848. Points That Intersect With Cars
// You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.
// Return the number of integer points on the line that are covered with any part of a car.

var numberOfPoints = function(nums) {
    let points = 0
    nums.sort((a,b) => a[0] - b[0])
    let high = nums[0][1]
    points += high - nums[0][0] + 1
    for (let i = 1; i < nums.length; i++) {
        let num = nums[i]
        if (num[0] > high) {
            points += num[1] - num[0] + 1
            high = num[1]
        } else if (num[1] > high) {
            points += num[1] - high
            high = num[1]
        }
    }
    return points
};

console.log(numberOfPoints([[3,6], [1,5], [4,7]]))
console.log(numberOfPoints([[1,3], [5,8]]))