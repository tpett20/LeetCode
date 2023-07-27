// 128. Longest Consecutive Sequence
// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
// You must write an algorithm that runs in O(n) time.

var longestConsecutive = function (nums) {
    if (!nums.length) return 0
    const map1 = {}
    const map2 = {}
    for (let num of nums) {
        if (num >= 0) {
            map1[num] = true
        } else {
            map2[Math.abs(num)] = true
        }
    }
    let count = 1
    let highCount = 0
    let borderCount = 0
    let border = false
    for (let key in map2) {
        if (key === '1') {
            border = true
            borderCount = 1
        }
        if (map2[key] && map2[parseInt(key) + 1]) {
            count++
            if (border) borderCount++
        } else {
            count = 1
            border = false
        }
        if (count > highCount) {
            highCount = count
        }
    }
    count = 1
    border = false
    for (let key in map1) {
        if (key === '0') {
            border = true
            borderCount++
        }
        if (map1[key] && map1[parseInt(key) + 1]) {
            count++
            if (border) borderCount++
        } else {
            count = 1
            border = false
        }
        if (count > highCount) {
            highCount = count
        }
    }
    return highCount > borderCount ? highCount : borderCount
};

let testCase = [100,4,200,1,3,2]
console.log(longestConsecutive(testCase), 'Expected: 4')
testCase = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
console.log(longestConsecutive(testCase), 'Expected: 5')