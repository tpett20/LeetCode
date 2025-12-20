// 944. Delete Columns to Make Sorted
/*
You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid.
For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
    abc
    bce
    cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
Return the number of columns that you will delete.
*/

var minDeletionSize = function(strs) {
    let count = 0
    const m = strs.length
    const n = strs[0].length
    for (let col = 0; col < n; col++) {
        let row = 0
        let prev = "a"
        while (row < m && strs[row][col] >= prev) {
            prev = strs[row][col]
            row++
        }
        count += (row === m) ? 0 : 1
    }
    return count
};

const testCase = [
    "cba", 
    "daf", 
    "ghi"
]
console.log(minDeletionSize(testCase))