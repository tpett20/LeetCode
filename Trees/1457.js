// 1457. Pseudo-Palindromic Paths in a Binary Tree
// Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
// Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

var pseudoPalindromicPaths  = function(node, s = new Set()) {
    let count = 0
    if (s.has(node.val)) {
        s.delete(node.val)
    } else {
        s.add(node.val)
    }
    if (!node.left && !node.right) {
        count = (s.size <= 1) ? 1 : 0
    } else {
        if (node.left) {
            count += pseudoPalindromicPaths(node.left, new Set(s))
        }
        if (node.right) {
            count += pseudoPalindromicPaths(node.right, new Set(s))
        }
    }
    return count
}

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testcase = new TreeNode(2)
testcase.left = new TreeNode(3)
testcase.left.left = new TreeNode(3)
testcase.left.right = new TreeNode(1)
testcase.right = new TreeNode(1)
testcase.right.right = new TreeNode(1)

console.log(pseudoPalindromicPaths(testcase))