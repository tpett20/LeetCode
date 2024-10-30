// 2938. Separate Black and White Balls
/*
There are n balls on a table, each ball has a color black or white.
You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.
In each step, you can choose two adjacent balls and swap them.
Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.
*/

var minimumSteps = function(s) {
    let oneCount = 0
    let steps = 0
    for (const bit of s) {
        if (bit === "1") {
            oneCount++
        } else {
            steps += oneCount
        }
    }
    return steps
};

console.log(minimumSteps("101"))