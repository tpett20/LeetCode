var minDepth = function(root) {
    let minDepth = Infinity
    function traverse(node, visited) {
        visited += 1
        if (visited >= minDepth) return
        if (node.left) {
            traverse(node.left, visited)
        }
        if (node.right) {
            traverse(node.right, visited)
        }
        if (!node.left && !node.right) {
            minDepth = Math.min(minDepth, visited)
        }
    }

    if (!root) return 0
    traverse(root, 0)
    return minDepth
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(3)
testCase.left = new TreeNode(9)
testCase.right = new TreeNode(20)
testCase.right.left = new TreeNode(15)
testCase.right.right = new TreeNode(7)

console.log(minDepth(testCase))