// 1544. Make The String Great
/*
Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.
*/

var makeGood = function(s) {
    const stack = []
    for (const char of s) {
        if (!stack.length) {
            stack.push(char)
        } else {
            const code1 = char.charCodeAt()
            const code2 = stack.at(-1).charCodeAt()
            const diff = Math.abs(code2 - code1)
            if (diff === 32) {
                stack.pop()
            } else {
                stack.push(char)
            }
        }
    }
    return stack.join("")
};

console.log(makeGood("leEeetcode"))
console.log(makeGood("abBAcC"))
console.log(makeGood("s"))