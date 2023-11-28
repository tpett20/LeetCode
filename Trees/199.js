// 199. Binary Tree Right Side View
// Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

var rightSideView = function(root) {
    if (!root) return []
    if (!root.left && !root.right) return [root.val]
    const output = []
    const queue = [root]
    while (queue.length) {
        output.push(queue[0].val)
        const qLen = queue.length
        for (let i = 0; i < qLen; i++) {
            let node = queue.shift()
            if (node.right) queue.push(node.right)
            if (node.left) queue.push(node.left)
        }
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

const testCase = new TreeNode(1)
testCase.left = new TreeNode(2)
testCase.right = new TreeNode(3)
testCase.left.left = new TreeNode(4)
testCase.left.right = new TreeNode(5)

console.log(rightSideView(testCase))