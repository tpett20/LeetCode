// 1578. Minimum Time to Make Rope Colorful
/*
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
Return the minimum time Bob needs to make the rope colorful.
*/

var minCost = function(colors, neededTime) {
    let minTime = 0
    let i = 1
    while (i < colors.length) {
        const rule = colors[i - 1]
        let maxTime = neededTime[i - 1]
        minTime += maxTime
        while (i < colors.length && colors[i] === rule) {
            const currTime = neededTime[i]
            minTime += currTime
            maxTime = Math.max(maxTime, currTime)
            i++
        }
        minTime -= maxTime
        i++
    }
    return minTime
};

console.log(minCost("aaabb", [1,2,3,4,5]))