// 501. Find Mode in Binary Search Tree
/*
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.
*/

var findMode = function(root) {
    if (!root.left && !root.right) return [root.val]
    const map = {}
    let nodeCount = 0
    function traverse(node) {
        map[node.val] = map[node.val] ? map[node.val] + 1 : 1
        nodeCount++
        if (node.left) traverse(node.left)
        if (node.right) traverse(node.right)
    }
    traverse(root)

    const half = nodeCount / 2
    let highFreq = [0, null]
    let multipleModes = false
    for (let key in map) {
        key = Number(key)
        if (map[key] > half) return [key]
        if (map[key] > highFreq[0]) {
            highFreq[0] = map[key]
            highFreq[1] = key
            multipleModes = false
        } else if (map[key] === highFreq[0]) {
            multipleModes = true
        }
    }
    if (!multipleModes) return [highFreq[1]]
    const modes = []
    for (let key in map) {
        if (map[key] === highFreq[0]) {
            modes.push(Number(key))
        }
    }
    return modes
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const tree = new TreeNode(1)
tree.left = new TreeNode(1)
tree.right = new TreeNode(2)
tree.right.left = new TreeNode(2)

console.log(findMode(tree))