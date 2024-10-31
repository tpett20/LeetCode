// 999. Available Captures for Rook
/*
You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.
A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.
Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.
Return the number of pawns the white rook is attacking.
*/

var numRookCaptures = function(board) {
    function findRook(grid) {
        for (let row = 0; row < grid.length; row++) {
            for (let col = 0; col < grid[0].length; col++) {
                if (grid[row][col] === "R") {
                    return [row, col]
                }
            }
        }
    }

    function checkPath(grid, start, rowChange, colChange) {
        let row = start[0]
        let col = start[1]
        while (
            row >= 0 && row < grid.length &&
            col >= 0 && col < grid[0].length
        ) {
            if (grid[row][col] === "p") {
                return 1
            } else if (grid[row][col] === "B") {
                return 0
            }
            row += rowChange
            col += colChange
        }
        return 0
    }

    const rookPos = findRook(board)
    let count = 0
    count += checkPath(board, rookPos, 1, 0)
    count += checkPath(board, rookPos, -1, 0)
    count += checkPath(board, rookPos, 0, 1)
    count += checkPath(board, rookPos, 0, -1)
    return count
};

const testCase = [
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    ["p","p",".","R",".","p","B","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","B",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."]
]

console.log(numRookCaptures(testCase))