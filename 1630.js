// 1630. Arithmetic Subarrays
/*
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.
For example, these are arithmetic sequences:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
The following sequence is not arithmetic:
    1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.
Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
*/

var checkArithmeticSubarrays = function(nums, l, r) {
    const output = []
    for (let i = 0; i < l.length; i++) {
        if (r[i] - l[i] === 1) {
            output.push(true)
        } else {
            output.push(checkArith(nums.slice(l[i], r[i] + 1)))
        }
    }
    return output
    
    function checkArith(arr) {
        const map = {}
        let low = Infinity
        let secLow = Infinity
        for (let num of arr) {
            map[num] = map[num] ? ++map[num] : 1
            if (num < low) {
                secLow = low
                low = num
            } else if (num < secLow) {
                secLow = num
            }
        }
        const pattern = secLow - low
        let next = low
        for (let i = 0; i < arr.length; i++) {
            if (!map[next]) return false
            else map[next]--
            next += pattern
        }
        return true
    }
};

console.log(checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))
console.log(checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]))