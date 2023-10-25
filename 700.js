// 700. Search in a Binary Search Tree
// You are given the root of a binary search tree (BST) and an integer val.
// Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

var searchBST = function(root, val) {
    let node = root
    while (true) {
        if (val === node.val) return node
        if (val < node.val) {
            if (!node.left) return null
            node = node.left
        } else {
            if (!node.right) return null
            node = node.right
        }
    }
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }

    insert(val) {
        const newNode = new TreeNode(val)
        let walker = this
        while (true) {
            if (val < walker.val) {
                if (!walker.left) {
                    walker.left = newNode
                    return this
                }
                walker = walker.left
            } else if (val > walker.val) {
                if (!walker.right) {
                    walker.right = newNode
                    return this
                }
                walker = walker.right
            } else return this
        }
    }
}

const tree = new TreeNode(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)

const testCase1 = searchBST(tree, 2)
console.log(testCase1)
const testCase2 = searchBST(tree, 5)
console.log(testCase2)