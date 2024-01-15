// 2225. Find Players With Zero or One Losses
/*
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
Return a list answer of size 2 where:
- answer[0] is a list of all players that have not lost any matches.
- answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.
Note:
- You should only consider the players that have played at least one match.
- The testcases will be generated such that no two matches will have the same outcome.
*/

var findWinners = function(matches) {
    const losses = {}
    for (let match of matches) {
        const winner = match[0]
        const loser = match[1]
        losses[loser] = losses[loser] ? ++losses[loser] : 1
        if (!losses[winner]) {
            losses[winner] = 0
        }
    }
    const output = [[], []]
    for (let player in losses) {
        player = parseInt(player)
        if (!losses[player]) {
            output[0].push(player)
        } else if(losses[player] === 1) {
            output[1].push(player)
        }
    }
    return output
};

console.log(findWinners([[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]))