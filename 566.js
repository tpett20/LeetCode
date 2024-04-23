// 566. Reshape the Matrix
/*
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
*/

var matrixReshape = function(mat, r, c) {
    const oldR = mat.length
    const oldC = mat[0].length
    if (oldR * oldC !== r * c) {
        return mat
    }
    const newMat = [[]]
    for (let row = 0; row < oldR; row++) {
        for (let col = 0; col < oldC; col++) {
            if (newMat.at(-1).length === c) {
                newMat.push([])
            }
            newMat[newMat.length - 1].push(mat[row][col])
        }
    }
    return newMat
};

console.log(matrixReshape([[1,2], [3,4]], 1, 4))
console.log(matrixReshape([[1,2], [3,4]], 4, 1))