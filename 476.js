// 476. Number Complement
/*
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
- For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
*/

var findComplement = function(num) {
    let string = ""
    let x = num
    while (x >= 1) {
        const r = x % 2
        if (r === 1) {
            string = "0" + string
        } else {
            string = "1" + string
        }
        x = Math.floor(x / 2)
    }
    return parseInt(string, 2)
};

console.log(findComplement(5))
console.log(findComplement(1))