// 119. Pascal's Triangle II
// Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
// In Pascal's triangle, each number is the sum of the two numbers directly above it.

var getRow = function(rowIndex, idx = 0, row = [1]) {
    if (rowIndex === idx) return row
    const newRow = [row[0]]
    for (let i = 1; i < row.length; i++) {
        newRow.push(row[i] + row[i - 1])
    }
    newRow.push(row[row.length - 1])
    return getRow(rowIndex, idx + 1, newRow)
};

console.log(getRow(0))
console.log(getRow(1))
console.log(getRow(2))
console.log(getRow(3))
console.log(getRow(4))