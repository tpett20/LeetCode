// 78. Subsets
// Given an integer array nums of unique elements, return all possible subsets (the power set).
// The solution set must not contain duplicate subsets. Return the solution in any order.

var subsets = function(nums) {
    const output = [[]]
    function traverse(currArr, remArr) {
        output.push(currArr)
        for (let i = 0; i < remArr.length; i++) {
            traverse([...currArr, remArr[i]], remArr.slice(i + 1, remArr.length))
        }
    }

    for (let i = 0; i < nums.length; i++) {
        traverse([nums[i]], nums.slice(i + 1, nums.length))
    }
    return output
};

console.log(subsets([1,2,3]))
console.log(subsets([0]))