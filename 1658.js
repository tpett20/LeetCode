// 1658. Minimum Operations to Reduce X to Zero
// 🚫 In Progress - Time Limit Exceeded 🚫
// You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
// Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

var minOperations = function(nums, x) {
    function getOps(arr, target, ops) {
        if (target === 0) return ops
        if (target < 0 || !arr.length) return Infinity
        return Math.min(
            getOps(arr.slice(1), target - arr[0], ops + 1),
            getOps(arr.slice(0, -1), target - arr.at(-1), ops + 1)
        )
    }
    const operations = getOps(nums, x, 0)
    return operations !== Infinity ? operations : -1
};

console.log(minOperations([1,1,4,2,3], 5))
console.log(minOperations([5,6,7,8,9], 4))
console.log(minOperations([3,2,20,1,1,3], 10))