// 2022. Convert 1D Array Into 2D Array
/*
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.
The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
*/

var construct2DArray = function(original, m, n) {
    if (m * n !== original.length) return []
    if (m === 1) return [original]
    const output = []
    let idx = 0
    for (let i = 0; i < m; i++) {
        const row = []
        for (let j = 0; j < n; j++) {
            row.push(original[idx++])
        }
        output.push(row)
    }
    return output
};

console.log(construct2DArray([1,2,3,4], 2, 2))
console.log(construct2DArray([1,1,1,2,2,2], 2, 3))