// 2352. Equal Row and Column Pairs
/*
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
*/

var equalPairs = function (grid) {
    let pairs = 0
    let map = {}
    for (let i = 0; i < grid.length; i++) {
        let key = grid[i].toString()
        if (map[key] !== undefined) {
            map[key]++
        } else {
            map[key] = 1
        }
    }
    for (let i = 0; i < grid[0].length; i++) {
        let key = ''
        for (let j = 0; j < grid.length; j++) {
            if (j < grid.length - 1) {
                key += (grid[j][i] + ',')
            } else {
                key += grid[j][i]
            }
        }
        if (map[key]) {
            pairs += map[key]
        }
    }
    return pairs
};

console.log(equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]), 'Expected: 1')
console.log(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]), 'Expected: 3')