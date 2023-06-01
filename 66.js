function plusOne(digits) {
    let i = digits.length - 1
    if (digits[i] !== 9) {
        digits[i]++
        return digits
    }
    while (digits[i] === 9) {
        digits[i] = 0
        if (i === 0) {
            digits[i] = 1
            digits.push(0)
            return digits
        } else if (digits[i-1] !== 9) {
            digits[i-1]++
            return digits
        }
        i--
    }
}

plusOne([9, 9, 9])