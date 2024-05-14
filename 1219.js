// 1219. Path with Maximum Gold
/*
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:
- Every time you are located in a cell you will collect all the gold in that cell.
- From your position, you can walk one step to the left, right, up, or down.
- You can't visit the same cell more than once.
- Never visit a cell with 0 gold.
- You can start and stop collecting gold from any position in the grid that has some gold.
*/

var getMaximumGold = function(grid) {
    function dfs(r, c, sum) {
        if (!grid[r] || !grid[r][c]) {
            return sum
        }
        const val = grid[r][c]
        sum += val
        grid[r][c] = 0
        const up = dfs(r-1, c, sum)
        const dn = dfs(r+1, c, sum)
        const lt = dfs(r, c-1, sum)
        const rt = dfs(r, c+1, sum)
        grid[r][c] = val
        return Math.max(up, dn, lt, rt)
    }
    let maxSum = 0
    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            maxSum = Math.max(maxSum, dfs(row, col, 0))
        }
    }
    return maxSum
};

console.log(getMaximumGold([
    [0,6,0],
    [5,8,7],
    [0,9,0]
]))
console.log(getMaximumGold([
    [1,0,7],
    [2,0,6],
    [3,4,5],
    [0,3,0],
    [9,0,20]
]))