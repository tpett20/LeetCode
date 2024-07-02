// 350. Intersection of Two Arrays II
// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

var intersect = function(nums1, nums2) {
    const smallNums = nums1.length < nums2.length ? nums1 : nums2
    const bigNums = nums1.length < nums2.length ? nums2 : nums1
    const map = {}
    let len = 0
    for (const num of smallNums) {
        if (map[num]) {
            map[num]++
        } else {
            map[num] = 1
            len++
        }
    }
    const output = []
    for (const num of bigNums) {
        if (map[num]) {
            output.push(num)
            map[num]--
            if (map[num] === 0) {
                len--
                if (len === 0) {
                    return output
                }
            }
        }
    }
    return output
};

console.log(intersect([1,2,2,1], [2,2]))
console.log(intersect([4,9,5], [9,4,9,8,4]))