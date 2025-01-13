// 3223. Minimum Length of String After Operations
/*
You are given a string s.
You can perform the following process on s any number of times:
    Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
    Delete the closest character to the left of index i that is equal to s[i].
    Delete the closest character to the right of index i that is equal to s[i].
Return the minimum length of the final string s that you can achieve.
*/

var minimumLength = function(s) {
    const freq = {}
    let minLen = 0
    for (const char of s) {
        freq[char] = freq[char] ? freq[char] + 1 : 1
    }
    for (const char in freq) {
        const count = freq[char]
        if (count < 3) {
            minLen += count
        } else if (count % 2 === 0) {
            minLen += 2
        } else {
            minLen += 1
        }
    }
    return minLen
};

console.log(minimumLength("abaacbcbb"))