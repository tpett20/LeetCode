// 1337. The K Weakest Rows in a Matrix
/*
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
- The number of soldiers in row i is less than the number of soldiers in row j.
- Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
*/

var kWeakestRows = function(mat, k) {
    const obj = {}
    for (let i = 0; i < mat.length; i++) {
        let row = mat[i]
        let soldiers = 0
        let j = 0
        while (row[j] === 1) {
            soldiers++
            j++
        }
        obj[i] = soldiers
        mat[i] = i
    }
    mat.sort((a, b) => obj[a] - obj[b])
    return mat.slice(0, k)
};

console.log(kWeakestRows([
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
], 3))

console.log(kWeakestRows([
    [1,0,0,0],
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,0]
], 2))

console.log(kWeakestRows([
    [1,1], 
    [1,1], 
    [1,0]
], 1))