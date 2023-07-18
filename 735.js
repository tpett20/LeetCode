// 735. Asteroid Collision
/*
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
*/

var asteroidCollision = function (asteroids) {
    const stack = []
    for (let i = 0; i < asteroids.length; i++) {
        let topOfStack = stack[stack.length - 1]
        if (stack.length === 0 || topOfStack < 0 || asteroids[i] > 0) {
            stack.push(asteroids[i])
        } else {
            let right = Math.abs(asteroids[i])
            if (topOfStack === right) {
                stack.pop()
            } else if (topOfStack < right) {
                stack.pop()
                i--
            }
        }
    }
    return stack
};

console.log('Input:', [-1,-2,5,10,-5])
console.log('Output:', asteroidCollision([-1,-2,5,10,-5]))
console.log('Input:', [8,-8])
console.log('Output:', asteroidCollision([8,-8]))
console.log('Input:', [10, 2, -5])
console.log('Output:', asteroidCollision([10, 2, -5]))
// console.log(asteroidCollision([-1,2,-1,2,1,-5]))
// console.log(asteroidCollision([-1,5]))
// console.log(asteroidCollision([5,-1]))
// console.log(asteroidCollision([1,-3,-10,1]))