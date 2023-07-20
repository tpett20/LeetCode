// 80. Remove Duplicates from Sorted Array II
/*
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
*/

var removeDuplicates = function (nums) {
    let count
    let i = 1
    while (i < nums.length) {
        count = 1
        while (nums[i] === nums[i - 1]) {
            count++
            i++
        }
        if (count > 2) {
            let diff = count - 2
            nums.splice(i - count, diff)
            i -= diff
        }
        i++
    }
    return nums.length
};

let nums = [1,1,1,2,2,3]
console.log(removeDuplicates(nums))
nums = [0,0,1,1,1,1,2,3,3]
console.log(removeDuplicates(nums))