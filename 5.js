// 5. Longest Palindromic Substring
// Given a string s, return the longest palindromic substring in s.

var longestPalindrome = function (s) {
    let maxLen = 0
    let idx = 0
    for (let i = 1; i < s.length; i++) {
      let front = i + 1
      let back = i - 1
      let length = 1
      while (s[front] === s[back] && s[front] && s[back]) {
        length += 2
        if (length > maxLen) {
          maxLen = length
          idx = i
        }
        front++
        back--
      }
      if (s[i] === s[i-1]) {
        front = i + 1
        back = i - 2
        length = 2
        if (length > maxLen) {
          maxLen = length
          idx = i
        }
        while (s[front] === s[back] && s[front] && s[back]) {
          length +=2
          if (length > maxLen) {
            maxLen = length
            idx = i
          }
          front++
          back--
        }
      }
    }
    if (maxLen === 0) return s[0]
    else if (maxLen % 2 === 0) {
      let steps = (maxLen - 2) / 2
      return s.slice(idx - steps - 1, idx + steps + 1)
    }
    else {
      let steps = (maxLen - 1) / 2
      return s.slice(idx - steps, idx + steps + 1)
    }
};

console.log(longestPalindrome('abba'))