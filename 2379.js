// 2379. Minimum Recolors to Get K Consecutive Black Blocks
/*
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
*/

var minimumRecolors = function(blocks, k) {
    let n = blocks.length
    let maxBs = 0
    for (let i = 0; i < k; i++) {
        if (blocks[i] == "B") {
            maxBs += 1
        }
    }
    let currBs = maxBs
    for (let i = k; i < n; i++) {
        currBs -= (blocks[i - k] === "B") ? 1 : 0
        currBs += (blocks[i] === "B") ? 1 : 0
        maxBs = Math.max(maxBs, currBs)
    }
    return k - maxBs
};

const testCase = "WBWWBBWBBBWWWWBBBBBWWBWBWWBBBBBBWWWWWBBWWWBBWBBBWWBBWWBWWWBWBWWBWWBWWBWBWBBWBWBBWBBWWBBBWWBBBWBBWBWW"
console.log(minimumRecolors(testCase, 7))