// 791. Custom Sort String
/*
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.
*/

var customSortString = function(order, s) {
    const positions = {}
    for (let i = 0; i < order.length; i++) {
        positions[order[i]] = i
    }
    const arr = s.split("")
    arr.sort((a, b) => {
        const aVal = positions[a] !== undefined ? positions[a] : 26
        const bVal = positions[b] !== undefined ? positions[b] : 26
        return aVal - bVal
    })
    return arr.join("")
};

console.log(customSortString("cba", "abcd"))
console.log(customSortString("bcafg", "abcd"))