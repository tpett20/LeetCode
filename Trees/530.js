// 530. Minimum Absolute Difference in BST
// Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

var getMinimumDifference = function(root) {
    function checkInOrder(node) {
        if (!node) return
        checkInOrder(node.left)
        if (lastVal !== undefined) {
            let diff = node.val - lastVal
            minDiff = Math.min(diff, minDiff)
        }
        lastVal = node.val
        checkInOrder(node.right)
    }
    
    let minDiff = Infinity
    let lastVal
    checkInOrder(root)
    return minDiff
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
tree.insert(6)
tree.insert(1)
tree.insert(3)

console.log(getMinimumDifference(tree))