// 200. Number of Islands
// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

var numIslands = function(grid) {
    const visited = new Set()
    function dfs(r, c) {
        visited.add(`${r}.${c}`)
        if (r > 0 && grid[r - 1][c] === '1' && !visited.has(`${r - 1}.${c}`)) {
            dfs(r - 1, c)
        }
        if (r < grid.length - 1 && grid[r + 1][c] === '1' && !visited.has(`${r + 1}.${c}`)) {
            dfs(r + 1, c)
        }
        if (grid[r][c - 1] === '1' && !visited.has(`${r}.${c - 1}`)) {
            dfs(r, c - 1)
        }
        if (grid[r][c + 1] === '1' && !visited.has(`${r}.${c + 1}`)) {
            dfs(r, c + 1)
        }
    }

    let count = 0
    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col] === '1' && !visited.has(`${row}.${col}`)) {
                count++
                dfs(row, col)
            }
        }
    }
    return count
};

console.log(numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
console.log(numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))