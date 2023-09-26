// 1652. Defuse the Bomb
/*
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
- If k > 0, replace the ith number with the sum of the next k numbers.
- If k < 0, replace the ith number with the sum of the previous k numbers.
- If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
*/

var decrypt = function(code, k) {
    if (k === 0) return code.fill(0)
    let front = 1
    let back = Math.abs(k)
    let sum = 0
    const output = new Array(code.length)
    for (let i = front; i <= back; i++) {
        sum += code[i]
    }
    let floor
    let ceil
    if (k > 0) {
        floor = 0
        ceil = code.length
    } else {
        floor = Math.abs(k) + 1
        ceil = code.length + floor
    }
    for (let i = floor; i < ceil; i++) {
        let idx = i % code.length
        output[idx] = sum
        sum -= code[front]
        front = (front + 1) % code.length
        back = (back + 1) % code.length
        sum += code[back]
    } 
    return output
};

console.log(decrypt([5,7,1,4], 3))
console.log(decrypt([1,2,3,4], 0))
console.log(decrypt([2,4,9,3], -2))