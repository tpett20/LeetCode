// 1861. Rotating the Box
/*
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.
*/

var rotateTheBox = function(box) {
    const m = box.length
    const n = box[0].length
    const rotated = []
    for (let row = 0; row < n; row++) {
        const newRow = []
        for (let col = 0; col < m; col++) {
            newRow.push(box[m - 1 - col][row])
        }
        rotated.push(newRow)
    }
    for (let col = 0; col < m; col++) {
        let emptyIdx = 0
        for (let row = n - 1; row >= 0; row--) {
            if (rotated[row][col] === "." && !emptyIdx) {
                emptyIdx = row
            } else if (rotated[row][col] === "#" && emptyIdx) {
                rotated[row][col] = "."
                rotated[emptyIdx][col] = "#"
                emptyIdx--
            } else if (rotated[row][col] === "*") {
                emptyIdx = 0
            }
        }
    }
    return rotated
};

const testCase = [
    ["#","#","*",".","*","."],
    ["#","#","#","*",".","."],
    ["#","#","#",".","#","."]
]

console.log(rotateTheBox(testCase))