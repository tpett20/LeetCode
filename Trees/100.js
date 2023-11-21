// 100. Same Tree
// Given the roots of two binary trees p and q, write a function to check if they are the same or not.
// Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

var isSameTree = function(p, q) {
    if (!p && !q) return true
    if (!p || !q) return false
    const stack = []
    let same = true
    
    function traverseLeftFirst(node) {
        stack.push(node.val)
        if (node.left) traverseLeftFirst(node.left)
        else stack.push(null)
        if (node.right) traverseLeftFirst(node.right)
        else stack.push(null)
    }
    traverseLeftFirst(p)

    function traverseRightFirst(node) {
        if (node.right) traverseRightFirst(node.right)
        else if (stack.pop() !== null) same = false
        if (node.left) traverseRightFirst(node.left)
        else if (stack.pop() !== null) same = false
        if (node.val !== stack.pop()) same = false
    }
    traverseRightFirst(q)
    
    return stack.length ? false : same
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase1 = new TreeNode(1)
testCase1.left = new TreeNode(2)
testCase1.right = new TreeNode(1)

const testCase2 = new TreeNode(1)
testCase2.left = new TreeNode(1)
testCase2.right = new TreeNode(2)

console.log(isSameTree(testCase1, testCase2))
console.log(isSameTree(testCase1, testCase1))
console.log(isSameTree(testCase2, testCase2))