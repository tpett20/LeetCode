// 1550. Three Consecutive Odds
// Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

var threeConsecutiveOdds = function(arr) {
    let oddCt = 0
    for (let int of arr) {
        if (int % 2 !== 0) {
            oddCt++
        } else {
            oddCt = 0
        }
        if (oddCt === 3) {
            return true
        }
    }
    return false
};

console.log(threeConsecutiveOdds([2,6,4,1]))
console.log(threeConsecutiveOdds([2,6,4,1,3,5]))