// 2614. Prime In Diagonal
/*
You are given a 0-indexed two-dimensional integer array nums.
Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.
Note that:
An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.
*/

var diagonalPrime = function(nums) {
    function isPrime(num, seen) {
        if (seen[num] !== undefined) {
            return seen[num]
        }
        const ceil = Math.floor(num / 2)
        for (let i = 2; i <= ceil; i++) {
            if (num % i === 0) {
                seen[num] = false
                return false
            }
        }
        seen[num] = true
        return true
    }

    const n = nums.length
    let maxPrime = 0
    const checked = { 1: false }
    for (let i = 0; i < n; i++) {
        const num1 = nums[i][i]
        const num2 = nums[i][n - i - 1]
        if (num1 > maxPrime && isPrime(num1, checked)) {
            maxPrime = num1
        }
        if (num2 > maxPrime && isPrime(num2, checked)) {
            maxPrime = num2
        }
    }
    return maxPrime
};

const testCase = [
    [1, 2, 3],
    [5, 6, 7],
    [113, 10, 11]
]
console.log(diagonalPrime(testCase))