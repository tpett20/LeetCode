// 3075. Maximize Happiness of Selected Children
/*
You are given an array happiness of length n, and a positive integer k.
There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.
In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.
Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.
*/

var maximumHappinessSum = function(happiness, k) {
    let maxSum = 0
    let rounds = 0
    const children = happiness.toSorted((a, b) => a - b)
    while (k > 0) {
        const happyAdd = Math.max(children.pop() - rounds, 0)
        if (happyAdd === 0) break
        maxSum += happyAdd
        k--
        rounds++
    }
    return maxSum
};

console.log(maximumHappinessSum([12, 25, 25], 2))