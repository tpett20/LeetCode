// 118. Pascal's Triangle
// Given an integer numRows, return the first numRows of Pascal's triangle.
// In Pascal's triangle, each number is the sum of the two numbers directly above it.

var generate = function(numRows) {
    const triangle = [[1]]
    for (let i = 1; i < numRows; i++) {
        const prev = triangle[i - 1]
        const curr = []
        for (let j = 0; j <= prev.length; j++) {
            if (j === 0 || j=== prev.length) {
                curr.push(1)
            } else {
                const lt = prev[j - 1]
                const rt = prev[j]
                curr.push(lt + rt)
            }
        }
        triangle.push(curr)
    }
    return triangle
};

const testCase = generate(30)
console.log(testCase)