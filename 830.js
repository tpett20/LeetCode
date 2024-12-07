// 830. Positions of Large Groups
/*
In a string s of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.
*/

var largeGroupPositions = function(s) {
    const output = []
    let start = 0
    let currChar = s[0]
    let count = 1
    for (let i = 1; i < s.length; i++) {
        if (s[i] === currChar) {
            count++
        } else {
            if (count >= 3) {
                output.push([start, i - 1])
            }
            start = i
            currChar = s[i]
            count = 1
        }
    }
    if (count >= 3) {
        output.push([start, s.length - 1])
    }
    return output
};

console.log(largeGroupPositions("lgm"))
console.log(largeGroupPositions("lgggggggm"))
console.log(largeGroupPositions("lllgggmmm"))