// 3184. Count Pairs That Form a Complete Day I
/*
Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.
A complete day is defined as a time duration that is an exact multiple of 24 hours.
For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.
*/

var countCompleteDayPairs = function(hours) {
    let pairs = 0
    const tally = {}
    for (const hour of hours) {
        const r = hour % 24
        if (r === 0) {
            if (tally[0]) {
                pairs += tally[0]
                tally[0]++
            } else {
                tally[0] = 1
            }
        } else {
            const other = 24 - r
            if (tally[other]) {
                pairs += tally[other]
            }
            tally[r] = tally[r] ? ++tally[r] : 1
        }
    }
    return pairs
};

console.log(countCompleteDayPairs([12, 12, 30, 24, 24]))
console.log(countCompleteDayPairs([72, 48, 24, 3, 21]))