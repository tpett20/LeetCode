// 2385. Amount of Time for Binary Tree to Be Infected
/*
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
Each minute, a node becomes infected if:
- The node is currently uninfected.
- The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.
*/

var amountOfTime = function(root, start) {
    const leafPaths = []
    let startPath = ""
    function traverse(node, target, path) {
        if (node.val === target) {
            startPath = path
        }
        if (!node.left && !node.right) {
            leafPaths.push(path)
        }
        if (node.left) {
            traverse(node.left, target, path + 'L')
        }
        if (node.right) {
            traverse(node.right, target, path + 'R')
        }
    }
    traverse(root, start, "")

    function getDist(sPath, lPath) {
        let i = 0
        while (i < lPath.length && lPath[i] === sPath[i]) {
            i++
        }
        const dist = (sPath.length - i) + (lPath.length - i)
        return dist
    }
    let maxTime = startPath.length
    for (let leafPath of leafPaths) {
        maxTime = Math.max(maxTime, getDist(startPath, leafPath))
    }
    return maxTime
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(1)
testCase.left = new TreeNode(5)
testCase.right = new TreeNode(3)
testCase.left.right = new TreeNode(4)
testCase.left.right.left = new TreeNode(9)
testCase.left.right.right = new TreeNode(2)
testCase.right.left = new TreeNode(10)
testCase.right.right = new TreeNode(6)

console.log(amountOfTime(testCase, 3))