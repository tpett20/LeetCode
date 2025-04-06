// 1863. Sum of All Subset XOR Totals
/*
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
    For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 
Note: Subsets with the same elements should be counted multiple times.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
*/

var subsetXORSum = function(nums) {
    const xorTotals = []
    function traverse(total, idx) {
        while (idx < nums.length) {
            const currTotal = total ^ nums[idx]
            xorTotals.push(currTotal)
            traverse(currTotal, idx + 1)
            idx++
        }
    }
    traverse(0, 0)
    let xorTotalsSum = 0
    for (const xorTotal of xorTotals) {
        xorTotalsSum += xorTotal
    }
    return xorTotalsSum
};

console.log(subsetXORSum([3, 4, 5, 6, 7, 8]))