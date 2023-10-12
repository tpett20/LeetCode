// 1030. Matrix Cells in Distance Order
/*
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).
Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.
The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
*/

var allCellsDistOrder = function(rows, cols, rCenter, cCenter) {
    const cells = []
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            let dist = Math.abs(rCenter - row) + Math.abs(cCenter - col)
            cells.push({
                r: row,
                c: col,
                d: dist
            })
        }
    }
    cells.sort((a, b) => a.d - b.d)
    return cells.map(cell => [cell.r, cell.c])
};

console.log(allCellsDistOrder(1, 2, 0, 0))
console.log(allCellsDistOrder(2, 2, 0, 1))
console.log(allCellsDistOrder(2, 3, 1, 2))