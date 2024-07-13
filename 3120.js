// 3210. Find the Encrypted String
/*
You are given a string s and an integer k. Encrypt the string using the following algorithm:
- For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
Return the encrypted string.
*/

var getEncryptedString = function(s, k) {
    let output = ""
    for (let i = 0; i < s.length; i++) {
        let kthIdx = (i + k) % s.length
        output += s[kthIdx]
    }
    return output
};

console.log(getEncryptedString("dart", 47))