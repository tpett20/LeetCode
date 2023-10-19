// 844. Backspace String Compare
// Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
// Note that after backspacing an empty text, the text will continue empty.

var backspaceCompare = function(s, t) {
    let typedS = ''
    let backspaces = 0
    for (let i = s.length - 1; i >= 0; i--) {
        let char = s[i]
        if (char === '#') {
            backspaces++
        } else if (backspaces) {
            backspaces--
        } else {
            typedS += char
        }
        if (backspaces >= i) break
    }
    let typedT = ''
    backspaces = 0
    for (let i = t.length - 1; i >= 0; i--) {
        let char = t[i]
        if (char === '#') {
            backspaces++
        } else if (backspaces) {
            backspaces--
        } else {
            typedT += char
        }
        if (backspaces >= i) break
    }
    return typedS === typedT
};

console.log(backspaceCompare("ab#c", "ad#c"))
console.log(backspaceCompare("ab##", "c#d#"))
console.log(backspaceCompare("a#c", "b"))