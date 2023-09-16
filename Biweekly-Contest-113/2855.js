// 2855. Minimum Right Shifts to Sort the Array
// 🏆 Biweekly Contest 113
// You are given a 0-indexed array nums of length n containing distinct positive integers. Return the minimum number of right shifts required to sort nums and -1 if this is not possible.
// A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.

var minimumRightShifts = function(nums) {
    let max = nums[0]
    let rest = []
    let shifts = 0
    for (let i = 1; i < nums.length; i++) {
        let num = nums[i]
        if (num >= max) {
            max = num
        } else {
            rest = nums.splice(i)
            break
        }
    }
    shifts = rest.length
    const newArr = rest.concat(nums)
    for (let i = 1; i < newArr.length; i++) {
        let num = newArr[i]
        if (newArr[i - 1] > num) {
            return -1
        }
    }
    return shifts
};

console.log(minimumRightShifts([3,4,5,1,2]))
console.log(minimumRightShifts([1,3,5]))
console.log(minimumRightShifts([2,1,4]))