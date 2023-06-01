var climbStairs = function(n) {
    let arr = [0, 1]
    for (let i = 1; i < n; i++) {
        arr.push(arr[i] + arr[i-1])
    }
    return arr[arr.length-1] + arr[arr.length-2]
}