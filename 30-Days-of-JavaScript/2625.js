// 2625. Flatten Deeply Nested Array
/*
Given a multi-dimensional array arr and a depth n, return a flattened version of that array.
A multi-dimensional array is a recursive data structure that contains integers or other multi-dimensional arrays.
A flattened array is a version of that array with some or all of the sub-arrays removed and replaced with the actual elements in that sub-array. This flattening operation should only be done if the current depth of nesting is less than n. The depth of the elements in the first array are considered to be 0.
Please solve it without the built-in Array.flat method.
*/

var flat = function (arr, n) {
    let output = []
    while (n > 0) {
        for (let i = 0; i < arr.length; i++) {
            if (Array.isArray(arr[i])) {
                for (let item of arr[i]) {
                    output.push(item)
                }
            } else {
                output.push(arr[i])
            }
        }
        n--
        arr = output
        output = []
    }
    return arr
};

let arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
let n = 1
console.log(flat(arr, n))
arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 2
console.log(flat(arr, n))