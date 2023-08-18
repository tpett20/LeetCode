// 9. Palindrome Number
// Given an integer x, return true if x is a palindrome, and false otherwise. 

var isPalindrome = function(x) {
    x = x.toString()
    let y = ''
    for (let i = x.length - 1; i >= 0; i--) {
        y += x[i]
    }
    return x === y ? true : false
};

// TEST CASE
console.log(isPalindrome(121))
console.log(isPalindrome(10))