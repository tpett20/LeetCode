// 2623. Memoize
/*
Given a function fn, return a memoized version of that function.
A memoized function is a function that will never be called twice with the same inputs. Instead it will return a cached value.
You can assume there are 3 possible input functions: sum, fib, and factorial.
- sum accepts two integers a and b and returns a + b.
- fib accepts a single integer n and returns 1 if n <= 1 or fib(n - 1) + fib(n - 2) otherwise.
- factorial accepts a single integer n and returns 1 if n <= 1 or factorial(n - 1) * n otherwise.
*/

// Cache as Hashmap Solution
function memoize(fn) {
    const cache = new Map()
    return function(...args) {
        let key = args.toString()
        if (cache.has(key)) {
            return cache.get(key)
        } else {
            let result = fn(...args)
            cache.set(key, result)
            return result
        }
    }
}
// Cache as Object Solution
// function memoize(fn) {
//     const cache = {}
//     return function(...args) {
//         if (cache[args] !== undefined) {
//             return cache[args]
//         } else {
//             let result = fn(...args)
//             cache[args] = result
//             return result
//         }
//     }
// }

let callCount = 0
const memoizedFn = memoize(function (a, b) {
    callCount += 1
    return a + b
})
console.log(memoizedFn(2, 3))
console.log(memoizedFn(2, 3))
console.log(callCount)