// 2483. Minimum Penalty for a Shop
/*
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
- if the ith character is 'Y', it means that customers come at the ith hour
- whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
- For every hour when the shop is open and no customers come, the penalty increases by 1.
- For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.
Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
*/

var bestClosingTime = function(customers) {
    let minPenalty
    let minPenaltyIdx
    const penalties = []
    let penaltyTally = 0
    for (let i = 0; i <= customers.length; i++) {
        penalties.push(penaltyTally)
        if (customers[i] === 'N') {
            penaltyTally++
        }
    }
    minPenalty = penalties[customers.length]
    minPenaltyIdx = customers.length
    penaltyTally = 0
    for (let i = customers.length - 1; i >= 0; i--) {
        if (customers[i] === 'Y') {
            penaltyTally++
        } 
        penalties[i] += penaltyTally
        if (penalties[i] <= minPenalty) {
            minPenalty = penalties[i]
            minPenaltyIdx = i
        }
    }
    return minPenaltyIdx
};

console.log(bestClosingTime('YYNY'))