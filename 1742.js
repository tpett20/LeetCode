// 1742. Maximum Number of Balls in a Box
/*
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.
Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
*/

var countBalls = function(lowLimit, highLimit) {
    function getBox(num) {
        let str = num.toString()
        let box = 0
        for (let char of str) {
            box += parseInt(char)
        }
        return box
    }
    const map = {}
    let max = 0
    for (let i = lowLimit; i <= highLimit; i++) {
        let box = getBox(i)
        if (map[box]) {
            map[box]++
        } else {
            map[box] = 1
        }
        if (map[box] > max) {
            max = map[box]
        }
    }
    return max
};

console.log(countBalls(5, 15))