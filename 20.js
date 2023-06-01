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