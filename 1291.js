// 1291. Sequential Digits
// An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
// Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

var sequentialDigits = function(low, high) {
    let lowNumDigits = low.toString().length
    let highNumDigits = high.toString().length
    const seqDigits = []
    for (let numDigits = lowNumDigits; numDigits <= highNumDigits; numDigits++) {
        let first = 1
        let last = 8 - (numDigits - 2)
        for (let topDigit = first; topDigit <= last; topDigit++) {
            let str = topDigit.toString()
            let int = topDigit
            for (let i = 0; i < numDigits - 1; i++) {
                int += 1
                str += int
            }
            int = parseInt(str)
            if (int <= high && int >= low) {
                seqDigits.push(int)
            } else if (int > high) {
                break
            }
        }
    }
    return seqDigits
};

console.log(sequentialDigits(10, 10000))