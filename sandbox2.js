var longestPalindrome = function (s) {
    let longestPal = ''
    let testPal = ''
    let bigArr = []
    // for each letter in string, return all possible consecutive strings starting from that string to the end of the string. 
    // only return the string if it is a palindrome. 
    // compare all the returned strings and return the longest
    rAllStrings()
    function rAllStrings() {
        if (s.length === 0) {
            return
        }
        let string = ''
        let reverseString = ''
        let arr = []
        for (let j = 0; j < s.length; j++) {
            string += s[j]
            reverseString = string.split('').reverse().join('')
            if (string === reverseString) {
                arr.push(string)
            }
        }
        bigArr = bigArr.concat(arr)
        s = s.slice(1)
        rAllStrings()
    }
    for (let i = 0; i < bigArr.length; i++) {
        if (longestPal.length < bigArr[i].length) {
            longestPal = bigArr[i]
        }
    }
    console.log(longestPal)
    return longestPal
}

longestPalindrome('rotor')