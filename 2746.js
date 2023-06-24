// 2746. Decremental String Concatenation
/*
You are given a 0-indexed array words containing n strings.
Let's define a join operation join(x, y) between two strings x and y as concatenating them into xy. However, if the last character of x is equal to the first character of y, one of them is deleted.
For example join("ab", "ba") = "aba" and join("ab", "cde") = "abcde".
You are to perform n - 1 join operations. Let str0 = words[0]. Starting from i = 1 up to i = n - 1, for the ith operation, you can do one of the following:
Make stri = join(stri - 1, words[i])
Make stri = join(words[i], stri - 1)
Your task is to minimize the length of strn - 1.
Return an integer denoting the minimum possible length of strn - 1.
*/

var minimizeConcatenatedLength = function (words) {
    let length = words[0].length
    let stackA = {
        'first': words[0][0],
        'last': words[0][words[0].length - 1]
    }
    let stackB = {
        'first': words[0][0],
        'last': words[0][words[0].length - 1]
    }
    for (let i = 1; i < words.length; i++) {
        console.log('before', stackA, stackB)
        console.log(words[i])
        let firstLtr = words[i][0]
        let lastLtr = words[i][words[i].length - 1]
        if (firstLtr === stackA.last) {
            length += words[i].length - 1
            stackA.last = lastLtr
            stackB.first = stackA.first
            stackB.last = stackA.last
        } else if (lastLtr === stackA.first) {
            length += words[i].length - 1
            stackA.first = firstLtr
            stackB.first = stackA.first
            stackB.last = stackA.last
        } else if (firstLtr === stackB.last) {
            length += words[i].length - 1
            stackB.last = lastLtr
            stackA.first = stackB.first
            stackA.last = stackB.last
        } else if (lastLtr === stackB.first) {
            length += words[i].length - 1
            stackB.first = firstLtr
            stackA.first = stackB.first
            stackA.last = stackB.last
        } else {
            console.log('hit else', words[i], firstLtr, lastLtr)
            length += words[i].length
            stackA.first = firstLtr
            stackB.last = lastLtr
        }
        console.log('after', stackA, stackB)
    }
    return length
};

// console.log(minimizeConcatenatedLength(["aa","ab","bc"]))
// console.log(minimizeConcatenatedLength(["aa","bc","bb"]))
// console.log(minimizeConcatenatedLength(["ab","b"]))
// console.log(minimizeConcatenatedLength(["aaa","c","aba"]))
// console.log(minimizeConcatenatedLength(["aa","bc","bb"]))
// console.log(minimizeConcatenatedLength(["aab", "abc", "aac", "b"]))
// console.log(minimizeConcatenatedLength(["abc", "cab", "tree", "fall"]))
// console.log(minimizeConcatenatedLength(["ccb","bac","cc"]))
// console.log(minimizeConcatenatedLength(["a", "c", "ab", "bb"]))
// console.log(minimizeConcatenatedLength(["a","c","bbc","cac"]))
console.log(minimizeConcatenatedLength(["ab","cc","bc","b"]))