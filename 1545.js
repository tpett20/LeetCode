// 1545. Find Kth Bit in Nth Binary String
/*
Given two positive integers n and k, the binary string Sn is formed as follows: 
    S1 = "0"
    Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
For example, the first four strings in the above sequence are:
    S1 = "0"
    S2 = "011"
    S3 = "0111001"
    S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
*/

var findKthBit = function(n, k) {
    function invert(string) {
        let output = ""
        for (let bit of string) {
            if (bit === "0") {
                output += "1"
            } else {
                output += "0"
            }
        }
        return output
    }

    function reverse(string) {
        let output = ""
        for (let i = string.length - 1; i >= 0; i--) {
            output += string[i]
        }
        return output
    }

    let s = "0"
    for (let i = 1; i < n; i++) {
        s = s + "1" + reverse(invert(s))
    }
    return s[k - 1]
};

console.log(findKthBit(3, 1))
console.log(findKthBit(4, 11))