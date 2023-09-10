//2496. Maximum Value of a String in an Array
/*
The value of an alphanumeric string can be defined as:
- The numeric representation of the string in base 10, if it comprises of digits only.
- The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
*/

var maximumValue = function(strs) {
    let maxVal = 0
    for (let str of strs) {
        let dec = Number(str)
        if (isNaN(dec)) {
            if (str.length > maxVal) maxVal = str.length
        } else {
            if (dec > maxVal) maxVal = dec
        }
    }
    return maxVal
};

console.log(maximumValue(["alic3","bob","3","4","00000","1temCase"]))