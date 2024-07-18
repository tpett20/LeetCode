// 1530. Number of Good Leaf Nodes Pairs
// You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
// Return the number of good leaf node pairs in the tree.

var countPairs = function(root, distance) {
    function dfs(node) {
        let count = 0
        let leftArr = []
        let rightArr = []
        if (!node.left && !node.right) {
            return [count, [0]]
        }
        if (node.left) {
            const leftData = dfs(node.left)
            count += leftData[0]
            leftArr = leftData[1]
        }
        if (node.right) {
            const rightData = dfs(node.right)
            count += rightData[0]
            rightArr = rightData[1]
        }
        const newLeftArr = []
        for (let i = 0; i < leftArr.length; i++) {
            leftArr[i] += 1
            if (leftArr[i] < distance) {
                newLeftArr.push(leftArr[i])
            }
        }
        const newRightArr = []
        for (let i = 0; i < rightArr.length; i++) {
            rightArr[i] += 1
            if (rightArr[i] < distance) {
                newRightArr.push(rightArr[i])
            }
        }
        for (const leftDist of newLeftArr) {
            for (const rightDist of newRightArr) {
                if (leftDist + rightDist <= distance) {
                    count++
                }
            }
        }
        return [count, newLeftArr.concat(newRightArr)]
    }

    return dfs(root)[0]
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(1)
testCase.left = new TreeNode(2)
testCase.right = new TreeNode(3)
testCase.left.right = new TreeNode(4)

console.log(countPairs(testCase, 3))