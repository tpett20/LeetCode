// 6. Zigzag Conversion
/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 

  P   A   H   N
  A P L S I I G
  Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
  string convert(string s, int numRows);
*/

var convert = function (s, numRows) {
    if (numRows === 1) return s
    const matrix = []
    for (let i = 0; i < numRows; i++) {
        matrix.push([])
    }
    let i = 0
    let row = 0
    let col = 0
    let colIndicator = 0
    while (i < s.length) {
        colIndicator = col % (numRows - 1)
        if (colIndicator === 0) {
            matrix[row].push(s[i])
            i++
            row++
        } else if (colIndicator !== 0) {
            if (row === (numRows - 1) - colIndicator) {
                matrix[row].push(s[i])
                i++
            }
            row++
        }
        if (row === numRows) {
            row = 0
            col++
        }
    }
    let string = ''
    for (let i = 0; i < matrix.length; i++) {
        matrix[i] = matrix[i].reduce((acc, char) => {
            return acc + char
        })
    }
    for (let i = 0; i < matrix.length; i++) {
        string += matrix[i]
    }
    return string
}

console.log(convert('PAYPALISHIRING', 3), 'Expected: PAHNAPLSIIGYIR')
console.log(convert('PAYPALISHIRING', 4), 'Expected: PINALSIGYAHRPI')