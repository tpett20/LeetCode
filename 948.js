// 948. Bag of Tokens
/*
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.
Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):
- Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
- Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.
*/

var bagOfTokensScore = function(tokens, power) {
    const s_tokens = tokens.toSorted((a, b) => a - b)
    let score = 0
    let up = 0
    let dn = tokens.length - 1
    while (power >= s_tokens[up]) {
        while (power >= s_tokens[up]) {
            power -= s_tokens[up]
            score++
            up++
        }
        if (up + 1 < dn) {
            power += s_tokens[dn]
            score--
            dn--
        }
    }
    return score
};

console.log(bagOfTokensScore([100], 50))
console.log(bagOfTokensScore([200, 100], 150))
console.log(bagOfTokensScore([100, 200, 300, 400], 200))
console.log(bagOfTokensScore([59, 0, 15, 33, 79, 72, 34, 62, 4, 16], 99))