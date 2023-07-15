// 2634. Filter Elements from Array
/*
Given an integer array arr and a filtering function fn, return a filtered array filteredArr.
The fn function takes one or two arguments:
    arr[i] - number from the arr
    i - index of arr[i]
filteredArr should only contain the elements from the arr for which the expression fn(arr[i], i) evaluates to a truthy value. A truthy value is a value where Boolean(value) returns true.
Please solve it without the built-in Array.filter method.
*/

var filter = function(arr, fn) {
    let newArr = []
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            newArr.push(arr[i])
        }
    }
    return newArr
};

console.log(filter([0,10,20,30], function greaterThan10(n) { return n > 10; }))
console.log(filter([1,2,3], function firstIndex(n, i) { return i === 0; }))
console.log(filter([-2,-1,0,1,2], function plusOne(n) { return n + 1 }))