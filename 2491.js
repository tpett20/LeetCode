// 2491. Divide Players Into Teams of Equal Skill
/*
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
The chemistry of a team is equal to the product of the skills of the players on that team.
Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
*/

var dividePlayers = function(skill) {
    const skills = skill.toSorted((a, b) => a - b)
    let l = 0, r = skill.length - 1
    const targetSkill = skills[l] + skills[r]
    let output = 0
    while (l < r) {
        const p1 = skills[l++]
        const p2 = skills[r--]
        if (p1 + p2 !== targetSkill) {
            return -1
        }
        output += (p1 * p2)
    }
    return output
};

console.log(dividePlayers([3, 2, 5, 1, 3, 4]))
console.log(dividePlayers([3, 4]))
console.log(dividePlayers([1, 9, 6, 9]))