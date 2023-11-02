// 2265. Count Nodes Equal to Average of Subtree
/*
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
Note:
- The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
- A subtree of root is a tree consisting of root and all of its descendants.
*/

var averageOfSubtree = function(root) {
    let output = 0
    function traverse(node) {
        let sum = node.val
        let count = 1
        if (node.left) {
            const leftData = traverse(node.left)
            sum += leftData[0]
            count += leftData[1]
        }
        if (node.right) {
            const rightData = traverse(node.right)
            sum += rightData[0]
            count += rightData[1]
        }
        const avg = Math.floor(sum / count)
        if (avg === node.val) output++
        return [sum, count]
    }
    traverse(root)
    return output
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(4)
testCase.left = new TreeNode(8)
testCase.right = new TreeNode(5)
testCase.left.left = new TreeNode(0)
testCase.left.right = new TreeNode(1)
testCase.right.right = new TreeNode(6)

console.log(averageOfSubtree(testCase))