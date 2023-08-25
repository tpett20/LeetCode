// 349. Intersection of Two Arrays
// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

var intersection = function(nums1, nums2) {
    const map = {}
    const arr = []
    for (let num of nums1) {
        map[num] = true
    }
    for (let num of nums2) {
        if (map[num]) {
            arr.push(num)
            map[num] = false
        }
    }
    return arr
};

console.log(intersection([4,9,5], [9,4,9,8,4]))