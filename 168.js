// 168. Excel Sheet Column Title
// Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

// Collaboration with sivaShilpa
var convertToTitle = function(columnNumber) {
    if (columnNumber <= 26) {
        return String.fromCharCode(columnNumber + 64)
    }
    let title = ''
    while (columnNumber > 26) {
        let timesThru = Math.floor(columnNumber / 26)
        let remainder = Math.floor(columnNumber % 26)
        if (remainder === 0) {
            timesThru--
            remainder = 26
        }
        if (timesThru <= 26) {
            return String.fromCharCode(timesThru + 64) + String.fromCharCode(remainder + 64) + title
        } else {
            title = String.fromCharCode(remainder + 64) + title
        }
        columnNumber = timesThru
    }
};

console.log(convertToTitle(943566))
console.log(convertToTitle(28))