// 70. Climbing Stairs
// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

var climbStairs = function(n) {
    let arr = [0, 1]
    for (let i = 1; i < n; i++) {
        arr.push(arr[i] + arr[i - 1])
    }
    return arr[arr.length - 1] + arr[arr.length - 2]
}

console.log(climbStairs(3))