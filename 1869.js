// 1869. Longer Contiguous Segments of Ones than Zeros
/*
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.
- For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.
*/

var checkZeroOnes = function(s) {
    let oneCt = 0
    let maxOneCt = 0
    let zeroCt = 0
    let maxZeroCt = 0
    let ones
    for (let bit of s) {
        if (ones) {
            if (bit === '1') {
                oneCt++
            } else {
                ones = false
                oneCt = 0
                zeroCt++
            }
        } else {
            if (bit === '0') {
                zeroCt++
            } else {
                ones = true
                zeroCt = 0
                oneCt++
            }
        }
        if (oneCt > maxOneCt) maxOneCt = oneCt
        else if (zeroCt > maxZeroCt) maxZeroCt = zeroCt
    }
    return maxOneCt > maxZeroCt ? true : false
};

console.log(checkZeroOnes("110100010"))