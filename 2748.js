// 2748. Number of Beautiful Pairs
/*
You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.
Return the total number of beautiful pairs in nums.
Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.
*/

var countBeautifulPairs = function(nums) {
    function getGCD(num1, num2) {
        const low = num1 < num2 ? num1 : num2
        const hi = num1 < num2 ? num2 : num1
        let divisor = low
        while (true) {
            if (low % divisor === 0 && hi % divisor === 0) {
                return divisor
            }
            divisor--
        }
    }
    let count = 0
    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            const iFirstDigit = parseInt(nums[i].toString()[0])
            const jLastDigit = parseInt(nums[j].toString().at(-1))
            if (getGCD(iFirstDigit, jLastDigit) === 1) {
                count++
            }
        }
    }
    return count
};

console.log(countBeautifulPairs([2,5,1,4]))
console.log(countBeautifulPairs([11,21,12]))