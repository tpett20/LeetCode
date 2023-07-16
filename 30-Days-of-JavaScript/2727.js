// 2727. Is Object Empty
/*
Given an object or an array, return if it is empty.
- An empty object contains no key-value pairs.
- An empty array contains no elements.
You may assume the object or array is the output of JSON.parse.
*/

var isEmpty = function(obj) {
    for (prop in obj) {
        if (prop !== undefined) {
            return false
        }
    }
    return true
};

console.log(isEmpty({"x": 5, "y": 42}))
console.log(isEmpty({}))
console.log(isEmpty([null, false, 0]))
console.log(isEmpty([]))