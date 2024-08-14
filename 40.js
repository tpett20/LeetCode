// 40. Combination Sum II
/*
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
*/

var combinationSum2 = function(candidates, target) {
    const nums = candidates.toSorted((a, b) => a - b)
    const visited = new Set()
    const combos = []
    function checkCombos(combo, idx, sum) {
        if (sum > target) return
        const stamp = combo.join(",")
        if (visited.has(stamp)) return
        visited.add(stamp)
        if (sum === target) {
            combos.push(combo)
        }
        for (let i = idx + 1; i < nums.length; i++) {
            checkCombos([...combo, nums[i]], i, sum + nums[i])
        }
    }

    for (let i = 0; i < nums.length; i++) {
        checkCombos([nums[i]], i, nums[i])
    }
    return combos
};

console.log(combinationSum2([10,1,2,7,6,1,5], 8))
console.log(combinationSum2([2,5,2,1,2], 5))