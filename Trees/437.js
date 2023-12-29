// 437. Path Sum III
// Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
// The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

var pathSum = function(node, targetSum, path = []) {
    if (!node) return 0
    path.push(node.val)
    let count = 0
    let sum = 0
    for (let i = path.length - 1; i >= 0; i--) {
        sum += path[i]
        if (sum === targetSum) {
            count++
        }
    }
    if (node.left) {
        count += pathSum(node.left, targetSum, [...path])
    }
    if (node.right) {
        count += pathSum(node.right, targetSum, [...path])
    }
    return count
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testcase = new TreeNode(10)
testcase.left = new TreeNode(5)
testcase.left.left = new TreeNode(3)
testcase.left.left.left = new TreeNode(3)
testcase.left.left.right = new TreeNode(-2)
testcase.left.right = new TreeNode(2)
testcase.left.right.right = new TreeNode(1)
testcase.right = new TreeNode(-3)
testcase.right.right = new TreeNode(11)
const target = 8

console.log(pathSum(testcase, target))