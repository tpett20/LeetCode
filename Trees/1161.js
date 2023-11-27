// 1161. Maximum Level Sum of a Binary Tree
// Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
// Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

var maxLevelSum = function(root) {
    const map = {}
    let level = 1
    const queue = [[root, level]]
    while (queue.length) {
        let data = queue.shift()
        let node = data[0]
        level = data[1]
        map[level] = map[level] ? map[level] + node.val : node.val
        if (node.left) queue.push([node.left, level + 1])
        if (node.right) queue.push([node.right, level + 1])
    }
    let maxSum = -Infinity
    let maxLvl = ''
    for (let lvl in map) {
        if (map[lvl] > maxSum) {
            maxSum = map[lvl]
            maxLvl = lvl
        }
    }
    return parseInt(maxLvl)
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(1)
testCase.left = new TreeNode(7)
testCase.right = new TreeNode(0)
testCase.left.left = new TreeNode(7)
testCase.left.right = new TreeNode(-8)

console.log(maxLevelSum(testCase))