// 20. Valid Parentheses
/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
*/

var isValid = function (s) {
    let stack = []
    for (bracket of s) {
        if (bracket === '(' || bracket === '[' || bracket === '{') {
            stack.push(bracket)
        }
        else if (
            bracket === ')' && stack[stack.length - 1] === '(' ||
            bracket === ']' && stack[stack.length - 1] === '[' ||
            bracket === '}' && stack[stack.length - 1] === '{'
        ) {
            stack.pop()
        }
        else {
            return false
        }
    }
    return stack.length ? false : true
};