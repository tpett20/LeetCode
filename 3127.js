// 3127. Make a Square with the Same Color
/*
You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents the white color, and character 'B' represents the black color.
Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the same color.
Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.
*/

var canMakeSquare = function(grid) {
    function checkCells(vals) {
        let wht = 0, blk = 0
        for (const val of vals) {
            if (val === "W") wht++
            else blk++
        }
        return wht >= 3 || blk >= 3
    }

    for (let row = 0; row < grid.length - 1; row++) {
        for (let col = 0; col < grid[0].length - 1; col++) {
            const mostlySame = checkCells([
                grid[row][col],
                grid[row + 1][col],
                grid[row][col + 1],
                grid[row + 1][col + 1]
            ])
            if (mostlySame) return true
        }
    }
    return false
};

console.log(canMakeSquare([[
    "B","W","B"], 
    ["B","W","W"], 
    ["B","W","B"]
]))