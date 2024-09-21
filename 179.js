// 179. Largest Number
// Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
// Since the result may be very large, so you need to return a string instead of an integer.

var largestNumber = function(nums) {
    const numStrs = []
    for (const num of nums) {
        numStrs.push(num.toString())
    }
    numStrs.sort((a, b) => {
        const opt1 = a + b
        const opt2 = b + a
        if (opt1 > opt2) return -1
        else if (opt2 > opt1) return 1
        else return 0
    })
    const output = numStrs.join("")
    if (output[0] === "0") return "0"
    return output
};

console.log(largestNumber([3, 30, 34, 5, 9]))