// 2482. Difference Between Ones and Zeros in Row and Column
/*
You are given a 0-indexed m x n binary matrix grid.
A 0-indexed m x n difference matrix diff is created with the following procedure:
- Let the number of ones in the ith row be onesRowi.
- Let the number of ones in the jth column be onesColj.
- Let the number of zeros in the ith row be zerosRowi.
- Let the number of zeros in the jth column be zerosColj.
- diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.
*/

var onesMinusZeros = function(grid) {
    const rowDiffs = []
    const colDiffs = []
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === 1) {
                rowDiffs[i] = rowDiffs[i] ? ++rowDiffs[i] : 1
                colDiffs[j] = colDiffs[j] ? ++colDiffs[j] : 1
            } else {
                rowDiffs[i] = rowDiffs[i] ? --rowDiffs[i] : -1
                colDiffs[j] = colDiffs[j] ? --colDiffs[j] : -1
            }
        }
    }
    const output = []
    for (let i = 0; i < grid.length; i++) {
        output[i] = []
        for (let j = 0; j < grid[i].length; j++) {
            output[i][j] = rowDiffs[i] + colDiffs[j]
        }
    }
    return output
};

console.log(onesMinusZeros([[0,1,1], [1,0,1], [0,0,1]]))
console.log(onesMinusZeros([[1,1,1], [1,1,1]]))