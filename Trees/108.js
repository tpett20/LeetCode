// 108. Convert Sorted Array to Binary Search Tree
// Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

var sortedArrayToBST = function(nums) {
    if (nums.length === 0) return null
    const midIdx = Math.floor((nums.length - 1) / 2)
    const newNode = new TreeNode(nums[midIdx])
    newNode.left = sortedArrayToBST(nums.slice(0, midIdx))
    newNode.right = sortedArrayToBST(nums.slice(midIdx + 1, nums.length))
    return newNode
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

console.log(sortedArrayToBST([-20, -10, -3, 0, 4, 5, 9]))