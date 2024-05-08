// 2643. Row With Maximum Ones
/*
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.
In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.
Return an array containing the index of the row, and the number of ones in it.
*/

var rowAndMaximumOnes = function(mat) {
    const output = [0, 0]
    for (let i = 0; i < mat.length; i++) {
        let sum = 0
        for (let j = 0; j < mat[i].length; j++) {
            sum += mat[i][j]
        }
        if (sum > output[1]) {
            output[0] = i
            output[1] = sum
        }
    }
    return output
};

console.log(rowAndMaximumOnes([[0,1], [1,0]]))
console.log(rowAndMaximumOnes([[0,0,0], [0,1,1]]))
console.log(rowAndMaximumOnes([[0,0], [1,1], [0,0]]))