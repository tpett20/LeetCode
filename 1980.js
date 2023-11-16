// 1980. Find Unique Binary String
// Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

var findDifferentBinaryString = function(nums) {
    const map = {}
    for (let num of nums) {
        map[num] = true
    }
    let i = 0
    while (true) {
        let num = i.toString(2)
        num = '0'.repeat(nums.length - num.length) + num
        if (!map[num]) return num
        i++
    }
};

console.log(findDifferentBinaryString(["01", "10"]))
console.log(findDifferentBinaryString(["00", "01"]))
console.log(findDifferentBinaryString(["111", "011", "001"]))