// 2248. Intersection of Multiple Arrays
// Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

var intersection = function(nums) {
    let output = new Set(nums[0])
    for (let i = 1; i < nums.length; i++) {
        const newOutput = new Set()
        for (const num of nums[i]) {
            if (output.has(num)) {
                newOutput.add(num)
            }
        }
        output = newOutput
    }
    return Array.from(output).sort((a, b) => a - b)
};

console.log(intersection([[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]))
console.log(intersection([[7,34,45,10,12,27,13], [27,21,45,10,12,13]]))