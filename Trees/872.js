// 872. Leaf-Similar Trees
/*
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
*/

var leafSimilar = function(root1, root2) {
    const stack = []
    function leftFirstDFS(node) {
        if (!node.left && !node.right) stack.push(node.val)
        else {
            if (node.left) leftFirstDFS(node.left)
            if (node.right) leftFirstDFS(node.right)
        }
    }
    leftFirstDFS(root1)
    let similar = true
    function rightFirstDFS(node) {
        if (!node.right && !node.left) {
            if (node.val !== stack.pop()) similar = false
        } else {
            if (node.right) rightFirstDFS(node.right)
            if (node.left) rightFirstDFS(node.left)
        }
    }
    rightFirstDFS(root2)
    if (stack.length) return false
    return similar
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }

    // BST Insert Method
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

const tree1 = new TreeNode(5)
tree1.insert(3)
tree1.insert(7)
tree1.insert(1)
tree1.insert(4)

const tree2 = new TreeNode(5)
tree2.insert(3)
tree2.insert(6)
tree2.insert(2)
tree2.insert(4)
tree2.insert(7)
tree2.insert(1)

console.log(leafSimilar(tree1, tree2))