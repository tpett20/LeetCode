// 3402. Minimum Operations to Make Columns Strictly Increasing
/*
You are given a m x n matrix grid consisting of non-negative integers.
In one operation, you can increment the value of any grid[i][j] by 1.
Return the minimum number of operations needed to make all columns of grid strictly increasing.
*/

var minimumOperations = function(grid) {
    const m = grid.length
    const n = grid[0].length
    let count = 0
    for (let col = 0; col < n; col++) {
        for (let row = 1; row < m; row++) {
            const curr = grid[row][col]
            const prev = grid[row - 1][col]
            if (curr <= prev) {
                count += prev - curr + 1
                grid[row][col] = prev + 1
            }
        }
    }
    return count
};

const grid = [
    [3, 2],
    [1, 3],
    [3, 4],
    [0, 1]
]
console.log(minimumOperations(grid))