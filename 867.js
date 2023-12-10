// 867. Transpose Matrix
// Given a 2D integer array matrix, return the transpose of matrix.
// The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

var transpose = function(matrix) {
    const output = []
    for (let row of matrix) {
        for (let i = 0; i < row.length; i++) {
            output[i] ? output[i].push(row[i]) : output[i] = [row[i]]
        }
    }
    return output
};

console.log(transpose([[1,2,3],[4,5,6],[7,8,9]]))
console.log(transpose([[1,2,3],[4,5,6]]))
console.log(transpose([[1,2,3],[4,5],[6]]))