// 129. Sum Root to Leaf Numbers
/*
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
- For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.
*/

var sumNumbers = function(node, num = "") {
    num += node.val.toString()
    if (!node.left && !node.right) {
        return parseInt(num)
    }
    let sum = 0
    if (node.left) {
        sum += sumNumbers(node.left, num)
    }
    if (node.right) {
        sum += sumNumbers(node.right, num)
    }
    return sum
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(4)
testCase.left = new TreeNode(9)
testCase.left.left = new TreeNode(5)
testCase.left.right = new TreeNode(1)
testCase.right = new TreeNode(0)
console.log(sumNumbers(testCase))