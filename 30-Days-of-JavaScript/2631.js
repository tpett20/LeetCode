// 2631. Group By
/*
Write code that enhances all arrays such that you can call the array.groupBy(fn) method on any array and it will return a grouped version of the array.
A grouped array is an object where each key is the output of fn(arr[i]) and each value is an array containing all items in the original array with that key.
The provided callback fn will accept an item in the array and return a string key.
The order of each value list should be the order the items appear in the array. Any order of keys is acceptable.
Please solve it without lodash's _.groupBy function.
*/

Array.prototype.groupBy = function(fn) {
    const map = {}
    for (let i = 0; i < this.length; i++) {
        let key = fn(this[i])
        if (map[key] !== undefined) {
            map[key].push(this[i])
        } else {
            map[key] = [this[i]]
        }
    }
    return map
};

let arr = [1,2,3]
console.log(arr.groupBy(String))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(arr.groupBy((n) => String(n > 5)))