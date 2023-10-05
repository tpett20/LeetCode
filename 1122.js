// 1122. Relative Sort Array
// Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
// Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

var relativeSortArray = function(arr1, arr2) {
    const map = {}
    for (let num of arr1) {
        map[num] = map[num] ? map[num] + 1 : 1
    }
    let i = 0
    for (let num of arr2) {
        for (let j = 0; j < map[num]; j++) {
            arr1[i] = num
            i++
        }
        delete map[num]
    }
    for (let key in map) {
        key = parseInt(key)
        for (let j = 0; j < map[key]; j++) {
            arr1[i] = key
            i++  
        }
    }
    return arr1
};

console.log(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
console.log(relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))