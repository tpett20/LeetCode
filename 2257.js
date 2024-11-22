// 2257. Count Unguarded Cells in the Grid
/*
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
Return the number of unoccupied cells that are not guarded.
*/

var countUnguarded = function(m, n, guards, walls) {
    const grid = []
    for (let row = 0; row < m; row++) {
        const newRow = []
        for (let col = 0; col < n; col++) {
            newRow.push("_")
        }
        grid.push(newRow)
    }
    for (const guard of guards) {
        const row = guard[0]
        const col = guard[1]
        grid[row][col] = "G"
    }
    for (const wall of walls) {
        const row = wall[0]
        const col = wall[1]
        grid[row][col] = "W"
    }
    let count = 0
    const unguardedHoriz = new Set()
    for (let row = 0; row < m; row++) {
        const fwdClear = new Set()
        let isClear = true
        for (let col = 0; col < n; col++) {
            const cell = grid[row][col]
            if (cell === "G") isClear = false
            else if (cell === "W") isClear = true
            else if (isClear) fwdClear.add(col)
        }
        isClear = true
        for (let col = n - 1; col >= 0; col--) {
            const cell = grid[row][col]
            if (cell === "G") isClear = false
            else if (cell === "W") isClear = true
            else if (isClear && fwdClear.has(col)) {
                unguardedHoriz.add(row.toString() + "-" + col.toString())
            }
        }
    }
    for (let col = 0; col < n; col++) {
        const fwdClear = new Set()
        let isClear = true
        for (let row = 0; row < m; row++) {
            const cell = grid[row][col]
            if (cell === "G") isClear = false
            else if (cell === "W") isClear = true
            else if (isClear) fwdClear.add(row)
        }
        isClear = true
        for (let row = m - 1; row >= 0; row--) {
            const cell = grid[row][col]
            if (cell === "G") isClear = false
            else if (cell === "W") isClear = true
            else if (isClear && fwdClear.has(row)) {
                const key = row.toString() + "-" + col.toString()
                if (unguardedHoriz.has(key)) {
                    count++
                }
            }
        }
    }
    return count
};

const testGuards = [[0, 0], [1, 1], [2, 3]]
const testWalls = [[0, 1], [2, 2], [1, 4]]

console.log(countUnguarded(4, 6, testGuards, testWalls))