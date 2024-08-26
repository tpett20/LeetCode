// 590. N-ary Tree Postorder Traversal
// Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

var postorder = function(root) {
    if (!root) return []
    const visited = []
    if (root.children) {
        for (const child of root.children) {
            visited.push(...postorder(child))
        }
    }
    visited.push(root.val)
    return visited
};

class _Node {
    constructor(val, children) {
        this.val = val
        this.children = children
    }
}

const node5 = new _Node(5)
const node6 = new _Node(6)
const node2 = new _Node(3, [node5, node6])
const node3 = new _Node(2)
const node4 = new _Node(4)
const testCase = new _Node(1, [node2, node3, node4])

console.log(postorder(testCase))