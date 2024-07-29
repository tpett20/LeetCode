// 3226. Number of Bit Changes to Make Two Integers Equal
/*
You are given two positive integers n and k.
You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.
Return the number of changes needed to make n equal to k. If it is impossible, return -1.
*/

var minChanges = function(n, k) {
    const bN = n.toString(2)
    const bK = k.toString(2)
    let count = 0
    const lenDiff = bN.length - bK.length
    if (lenDiff < 0) return -1
    for (let i = 0; i < lenDiff; i++) {
        if (bN[i] === "1") {
            count++
        }
    }
    for (let i = 0; i < bK.length; i++) {
        const j = lenDiff + i
        if (bN[j] === "1" && bK[i] === "0") {
            count++
        } else if (bN[j] === "0" && bK[i] === "1") {
            return -1
        }
    }
    return count
};

console.log(minChanges(13, 4))
console.log(minChanges(1986, 1986))
console.log(minChanges(14, 13))