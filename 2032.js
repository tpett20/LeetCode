// 2032. Two Out of Three
// Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

var twoOutOfThree = function(nums1, nums2, nums3) {
    const map = {}
    const output = []
    for (let num of nums1) {
        map[num] = 'A'
    }
    for (let num of nums2) {
        if (!map[num]) {
            map[num] = 'B'
        } else if (map[num] === 'A') {
            map[num] += 'B'
            output.push(num)
        }
    }
    for (let num of nums3) {
        if (map[num] && map[num].length === 1) {
            map[num] += 'C'
            output.push(num)
        }
    }
    return output
};

console.log(twoOutOfThree([1,1,3,2], [2,3], [3]))

console.log(twoOutOfThree(
    [2,15,10,11,14,12,14,11,9,1],
    [8,9,13,2,11,8],
    [13,5,15,7,12,7,8,3,13,15]
))