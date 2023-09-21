// 2705. Compact Object
// Given an object or array obj, return a compact object. A compact object is the same as the original object, except with keys containing falsy values removed. This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys. A value is considered falsy when Boolean(value) returns false.
// You may assume the obj is the output of JSON.parse. In other words, it is valid JSON.

var compactObject = function(obj) {
    const objIsArray = Array.isArray(obj) ? true : false
    const newObj = objIsArray ? [] : {}
    for (let key in obj) {
        if (obj[key] !== null && typeof obj[key] === 'object') {
            if (objIsArray) newObj.push(compactObject(obj[key]))
            else newObj[key] = compactObject(obj[key])
        } else if (obj[key]) {
            if (objIsArray) newObj.push(obj[key])
            else newObj[key] = obj[key]
        }
    }
    return newObj
};

console.log(compactObject([null, 0, false, 1]))
console.log(compactObject({"a": null, "b": [false, 1]}))
console.log(compactObject([null, 0, 5, [0], [false, 16]]))