// 2161. Partition Array According to Given Pivot
/*
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
    Every element less than pivot appears before every element greater than pivot.
    Every element equal to pivot appears in between the elements less than and greater than pivot.
    The relative order of the elements less than pivot and the elements greater than pivot is maintained.
        More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement.
*/

var pivotArray = function(nums, pivot) {
    const arr1 = []
    const arr2 = []
    const arr3 = []
    for (const num of nums) {
        if (num < pivot) {
            arr1.push(num)
        } else if (num === pivot) {
            arr2.push(num)
        } else {
            arr3.push(num)
        }
    }
    return [...arr1, ...arr2, ...arr3]
};

console.log(pivotArray([9, 12, 5, 10, 14, 3, 10], 10))