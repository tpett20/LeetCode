// 1331. Rank Transform of an Array
/*
Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
- Rank should be as small as possible.
*/

var arrayRankTransform = function(arr) {
    const sortedArr = arr.toSorted((a, b) => a - b)
    let rank = 1
    const rankRef = {}
    for (const num of sortedArr) {
        if (rankRef[num] === undefined) {
            rankRef[num] = rank++
        }
    }
    const ranks = []
    for (const num of arr) {
        ranks.push(rankRef[num])
    }
    return ranks
};

console.log(arrayRankTransform([40, 10, 20, 30]))
console.log(arrayRankTransform([100, 100, 100]))
console.log(arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))