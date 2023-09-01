// 338. Counting Bits
// Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

var countBits = function(n) {
    const arr = new Array(n + 1)
    arr[0] = 0
    let backToOne = false
    let maxOnes = 0
    for (let i = 0; i <= n; i++) {
        if (backToOne) {
            arr[i] = 1
            backToOne = false
        } else if (i % 2 !== 0) {
            arr[i] = arr[i - 1] + 1
            if (arr[i] > maxOnes) {
                backToOne = true
                maxOnes = arr[i]
            }
        } else {
            arr[i] = countOnes(i)
        }
    }
    function countOnes(num) {
        let binary = num.toString(2)
        let oneCt = 0
        for (let num of binary) {
            if (num === '1') oneCt++
        }
        return oneCt
    }
    return arr
};

console.log(countBits(8))