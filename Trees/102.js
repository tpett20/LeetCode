// 102. Binary Tree Level Order Traversal
// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

var levelOrder = function(root) {
    if (!root) return []
    const queue = [root]
    const output = []
    while (queue.length) {
        const level = []
        const qLen = queue.length
        for (let i = 0; i < qLen; i++) {
            const node = queue.shift()
            level.push(node.val)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        output.push(level)
    }
    return output
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(3)
testCase.left = new TreeNode(9)
testCase.right = new TreeNode(20)
testCase.right.left = new TreeNode(15)
testCase.right.right = new TreeNode(7)

console.log(levelOrder(testCase))