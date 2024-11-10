// 3133. Minimum Array End
/*
You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.
Return the minimum possible value of nums[n - 1].
*/

var minEnd = function(n, x) {
    if (n === 1) return x
    const xBin = x.toString(2)
    const nBin = (n - 1).toString(2)
    let output = ""
    let xIdx = xBin.length - 1
    let nIdx = nBin.length - 1
    while (nIdx >= 0 || xIdx >= 0) {
        if (nIdx < 0) {
            output = xBin[xIdx] + output
        } else if (xIdx < 0 || xBin[xIdx] === "0") {
            output = nBin[nIdx] + output
            nIdx -= 1
        } else {
            output = "1" + output
        }
        xIdx -= 1
    }
    return parseInt(output, 2)
};

console.log(minEnd(3, 4))
console.log(minEnd(1969, 1986))