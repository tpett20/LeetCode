// 1207. Unique Number of Occurrences
// Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

var uniqueOccurrences = function(arr) {
    let map = {}
    for (let num of arr) {
        if (map[num] !== undefined) {
            map[num]++
        } else {
            map[num] = 1
        }
    }
    let map2 = {}
    for (let key in map) {
        let freq = map[key]
        if (map2[freq] === true) {
            return false
        } else {
            map2[freq] = true
        }
    }
    return true
};

console.log(uniqueOccurrences([1,2,2,1,1,3]), 'Expected: true')
console.log(uniqueOccurrences([1,2]), 'Expected: false')
console.log(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]), 'Expected: true')