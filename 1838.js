// 1838. Frequency of the Most Frequent Element
/*
The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.
*/

var maxFrequency = function(nums, k) {
    nums.sort((a, b) => a - b)
    let count = 1
    let maxCount = 1
    let ceil = nums[0]
    let floorIdx = 0
    let prevDiff = 0
    for (let i = 1; i < nums.length; i++) {
        let num = nums[i]
        let diff = (num - ceil) * count + prevDiff
        while (diff > k) {
            prevDiff -= (ceil - nums[floorIdx])
            count--
            floorIdx++
            diff = (num - ceil) * count + prevDiff
        }
        count++
        maxCount = Math.max(count, maxCount)
        prevDiff = diff
        ceil = num
    }
    return maxCount
};

console.log(maxFrequency([1,2,4], 5))
console.log(maxFrequency([1,4,8,13], 5))
console.log(maxFrequency([3,9,6], 2))