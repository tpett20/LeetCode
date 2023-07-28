// 128. Longest Consecutive Sequence
// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
// You must write an algorithm that runs in O(n) time.

var longestConsecutive = function (nums) {
    if (!nums.length) return 0
    const posMap = {}
    const negMap = {}
    for (let num of nums) {
        if (num >= 0) {
            posMap[num] = true
        } else {
            negMap[Math.abs(num)] = true
        }
    }
    function getCounts(map, borderNum) {
        let count = 1
        let highCount = 0
        let borderCount = 0
        let border = false
        for (let key in map) {
            if (key === borderNum.toString()) {
                border = true
                borderCount = 1
            }
            if (map[key] && map[parseInt(key) + 1]) {
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
        return [highCount, borderCount]
    }
    let posCounts = getCounts(posMap, 0)
    let negCounts = getCounts(negMap, 1)
    let highCount = posCounts[0] > negCounts[0] ? posCounts[0] : negCounts[0]
    let borderCount = posCounts[1] + negCounts[1]
    return highCount > borderCount ? highCount : borderCount
};

let testCase = [100,4,200,1,3,2]
console.log(longestConsecutive(testCase), 'Expected: 4')
testCase = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
console.log(longestConsecutive(testCase), 'Expected: 5')