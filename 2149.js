// 2149. Rearrange Array Elements by Sign
/*
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should rearrange the elements of nums such that the modified array follows the given conditions:
- Every consecutive pair of integers have opposite signs.
- For all integers with the same sign, the order in which they were present in nums is preserved.
- The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
*/

var rearrangeArray = function(nums) {
    const posNums = []
    const negNums = []
    const output = []
    for (let num of nums) {
        if (num > 0) posNums.push(num)
        else negNums.push(num)
    }
    for (let i = 0; i < nums.length / 2; i++) {
        output.push(posNums[i])
        output.push(negNums[i])
    }
    return output
};

console.log(rearrangeArray([3,1,-2,-5,2,-4]))