// 1424. Diagonal Traverse II
// Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

var findDiagonalOrder = function(nums) {
    const output = []
    const map = {}
    for (let row = nums.length - 1; row >= 0; row--) {
        for (let col = nums[row].length - 1; col >= 0; col--) {
            let key = row + col
            let val = nums[row][col]
            if (map[key]) map[key].push(val)
            else map[key] = [val]
        }
    }
    for (let key in map) {
        output.push(...map[key])
    }
    return output
};

console.log(findDiagonalOrder([[1,2,3], [4,5,6], [7,8,9]]))
console.log(findDiagonalOrder([[1,2,3,4,5], [6,7], [8], [9,10,11], [12,13,14,15,16]]))