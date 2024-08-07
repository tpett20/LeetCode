// 2600. K Items With the Maximum Sum
/*
There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
The bag initially contains:
    numOnes items with 1s written on them.
    numZeroes items with 0s written on them.
    numNegOnes items with -1s written on them.
We want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the items.
*/

var kItemsWithMaximumSum = function(numOnes, numZeros, numNegOnes, k) {
    if (numOnes >= k) {
        return k
    } else if (numOnes + numZeros >= k) {
        return numOnes
    } else {
        const r = k - numOnes - numZeros
        return numOnes - r
    }
};

console.log(kItemsWithMaximumSum(3, 2, 0, 2))
console.log(kItemsWithMaximumSum(3, 2, 0, 4))