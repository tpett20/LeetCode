// 2096. Step-By-Step Directions From a Binary Tree Node to Another
/*
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
- 'L' means to go from a node to its left child node.
- 'R' means to go from a node to its right child node.
- 'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
*/

var getDirections = function(root, startValue, destValue) {
    let startPath = ""
    let destPath = ""

    function dfs(node, path) {
        if (node.val === startValue) {
            startPath = path
        } else if (node.val === destValue) {
            destPath = path
        }
        if (startPath && destPath) return
        if (node.left) {
            dfs(node.left, path + "L")
        }
        if (node.right) {
            dfs(node.right, path + "R")
        }
    }
    dfs(root, "")

    let minPathLen = (startPath.length < destPath.length) ? startPath.length : destPath.length
    let i = 0
    while (i < minPathLen && startPath[i] === destPath[i]) {
        i += 1
    }
    startPath = "U".repeat(startPath.length - i)
    destPath = destPath.slice(i)
    return startPath + destPath
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(5)
testCase.left = new TreeNode(1)
testCase.right = new TreeNode(2)
testCase.left.left = new TreeNode(3)
testCase.right.left = new TreeNode(6)
testCase.right.right = new TreeNode(4)

console.log(getDirections(testCase, 3, 6))