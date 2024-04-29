// 3128. Right Triangles - INCOMPLETE, TIME LIMIT EXCEEDED
/*
You are given a 2D boolean matrix grid.
Return an integer that is the number of right triangles that can be made with the 3 elements of grid such that all of them have a value of 1.
Note:
- A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element and in the same column with the third element. The 3 elements do not have to be next to each other.
*/

var numberOfRightTriangles = function(grid) {
    let count = 0
    const cMap = {}
    const rMap = {}
    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col]) {
                cMap[col] = cMap[col] ? ++cMap[col] : 1
                if (rMap[row]) rMap[row].push(col)
                else rMap[row] = [col]
            }
        }
    }
    for (const row in rMap) {
        const oneCols = rMap[row]
        for (let i = 0; i < oneCols.length - 1; i++) {
            for (let j = i + 1; j < oneCols.length; j++) {
                count += (cMap[oneCols[i]] - 1)
                count += (cMap[oneCols[j]] - 1)
            }
        }
    }
    return count
};

console.log(numberOfRightTriangles([[1,0,1], [1,0,0], [1,0,0]]))