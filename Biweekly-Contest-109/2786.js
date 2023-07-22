// 2786. Visit Array Positions to Maximize Score
// 🚫 INCOMPLETE - Biweekly Contest 109
/*
You are given a 0-indexed integer array nums and a positive integer x.
You are initially at position 0 in the array and you can visit other positions according to the following rules:
If you are currently in position i, then you can move to any position j such that i < j.
For each position i that you visit, you get a score of nums[i].
If you move from a position i to a position j and the parities of nums[i] and nums[j] differ, then you lose a score of x.
Return the maximum total score you can get.
Note that initially you have nums[0] points.
*/

var maxScore = function (nums, x) {
    let score = nums[0]
    let i = 1
    let lastEl = nums[0]
    let consSum = 0
    while (i < nums.length) {
        if (lastEl % 2 === nums[i] % 2) {
            score += nums[i]
            lastEl = nums[i]
            consSum = 0
        } else if (consSum + nums[i] > x) {
            score += consSum + nums[i]
            score -= x
            lastEl = nums[i]
            consSum = 0
        } else {
            consSum += nums[i]
        }
        i++
    }
    return score
};

console.log(maxScore([2,3,6,1,9,2], 5), 'Expected: 13')
console.log(maxScore([2,4,6,8], 3), 'Expected: 20')
let testCase173 = [38,92,23,30,25,96,6,71,78,77,33,23,71,48,87,77,53,28,6,20,90,83,42,21,64,95,84,29,22,21,33,36,53,51,85,25,80,56,71,69,5,21,4,84,28,16,65,7]
console.log(maxScore(testCase173, 52), 'Expected: 1545')