// 2038. Remove Colored Pieces if Both Neighbors are the Same Color
/*
There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.
Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.
- Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
- Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
- Alice and Bob cannot remove pieces from the edge of the line.
- If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.
*/

var winnerOfGame = function(colors) {
    let aTurns = 0
    let aCount = 0
    let bTurns = 0
    let bCount = 0
    for (let color of colors) {
        if (color === 'A') {
            aCount++
            bCount = 0
        } else {
            bCount++
            aCount = 0
        }
        if (aCount >= 3) {
            aTurns++
        } else if (bCount >= 3) {
            bTurns++
        }
    }
    return aTurns > bTurns ? true : false
};

console.log(winnerOfGame('AAABABB'))
console.log(winnerOfGame('AAABBB'))
console.log(winnerOfGame('AA'))
console.log(winnerOfGame('ABBBBBBBAAA'))