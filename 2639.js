// 2639. Find the Width of Columns of a Grid
/*
You are given a 0-indexed m x n integer matrix grid. The width of a column is the maximum length of its integers.
    For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
Return an integer array ans of size n where ans[i] is the width of the ith column.
The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.
*/

var findColumnWidth = function(grid) {
    function checkWidth(num) {
        if (num === 0) return 1
        let len = (num < 0) ? 1 : 0
        let n = Math.abs(num)
        while (n >= 1) {
            n = Math.floor(n / 10)
            len++
        }
        return len
    }

    const colWidths = []
    for (let col = 0; col < grid[0].length; col++) {
        let maxLen = 0
        for (let row = 0; row < grid.length; row++) {
            let len = checkWidth(grid[row][col])
            maxLen = Math.max(len, maxLen)
        }
        colWidths.push(maxLen)
    }
    return colWidths
};

console.log(findColumnWidth([[-15,1,3], [15,7,12], [5,6,-2]]))