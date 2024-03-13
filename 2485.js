// 2485. Find the Pivot Integer
/*
Given a positive integer n, find the pivot integer x such that:
The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
*/

var pivotInteger = function(n) {
    getPrefixSum = num => num * (num + 1) / 2

    const nSum = getPrefixSum(n)
    let left = 1
    let right = n
    while (left <= right) {
        let pivot = Math.floor((left + right) / 2)
        let leftSum = getPrefixSum(pivot)
        let rightSum = nSum - (leftSum - pivot)
        if (leftSum === rightSum) return pivot
        if (leftSum < rightSum) left = pivot + 1
        else right = pivot - 1
    }
    return -1
};

console.log(pivotInteger(8))
console.log(pivotInteger(1))
console.log(pivotInteger(4))