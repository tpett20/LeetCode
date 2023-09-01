// 338. Counting Bits
// Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

var countBits = function(n) {
    const arr = new Array(n + 1)
    arr[0] = 0
    let backToOne = false
    let maxOnes = 0
    for (let i = 1; i <= n; i++) {
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
        let oneCount = 0
        while (num !== 0) {
            let remainder = num % 2
            oneCount += remainder
            num = Math.floor(num / 2)
        }
        return oneCount
    }
    return arr
};

console.log(countBits(8))