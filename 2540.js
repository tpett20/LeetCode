// 2540. Minimum Common Value
/*
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
*/

var getCommon = function(nums1, nums2) {
    for (let i = 0; i < nums2.length; i++) {
        if (nums1.includes(nums2[i])) {
            return nums2[i]
        }
    } 
    return -1
};

console.log(getCommon([1,2,3], [2,4]))