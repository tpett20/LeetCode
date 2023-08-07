// 2540. Minimum Common Value
/*
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
*/

var getCommon = function(nums1, nums2) {
    let i = 0
    const map1 = {}
    const map2 = {}
    while (i < nums1.length && i < nums2.length) {
        map1[nums1[i]] = true
        map2[nums2[i]] = true
        if (map1[nums2[i]]) {
            return nums2[i]
        } else if (map2[nums1[i]]) {
            return nums1[i]
        }
        i++
    }
    while (i < nums1.length) {
        if (map2[nums1[i]]) {
            return nums1[i]
        }
        i++
    }
    while (i < nums2.length) {
        if (map1[nums2[i]]) {
            return nums2[i]
        }
        i++
    }
    return -1
};

console.log(getCommon([1,2,3], [2,4]))