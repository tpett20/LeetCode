// 2264. Largest 3-Same-Digit Number in String
/*
You are given a string num representing a large integer. An integer is good if it meets the following conditions:
- It is a substring of num with length 3.
- It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.
Note:
- A substring is a contiguous sequence of characters within a string.
- There may be leading zeroes in num or a good integer.
*/

var largestGoodInteger = function(num) {
    let count = 1
    let max = "-1"
    let lastNum = num[0]
    for (let i = 1; i < num.length; i++) {
        if (num[i] === lastNum) {
            count++
            if (count === 3) {
                if (parseInt(num[i]) > parseInt(max)) {
                    max = num[i]
                }
            }
        } else count = 1
        lastNum = num[i]
    }
    return max === "-1" ? "" : max.repeat(3)
};

console.log(largestGoodInteger("6777133339"))
console.log(largestGoodInteger("2300019"))
console.log(largestGoodInteger("42352338"))