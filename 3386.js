// 3386. Button with Longest Push Time
/*
You are given a 2D array events which represents a sequence of events where a child pushes a series of buttons on a keyboard.
Each events[i] = [indexi, timei] indicates that the button at index indexi was pressed at time timei.
    The array is sorted in increasing order of time.
    The time taken to press a button is the difference in time between consecutive button presses. The time for the first button is simply the time at which it was pressed.
Return the index of the button that took the longest time to push. If multiple buttons have the same longest time, return the button with the smallest index.
*/

var buttonWithLongestTime = function(events) {
    let longestBtn = events[0][0]
    let longestTime = events[0][1]
    for (let i = 1; i < events.length; i++) {
        const curr = events[i]
        const prev = events[i - 1]
        const btn = curr[0]
        const time = curr[1] - prev[1]
        if (time > longestTime || (time === longestTime && btn < longestBtn)) {
            longestBtn = btn
            longestTime = time
        }
    }
    return parseInt(longestBtn)
};

console.log(buttonWithLongestTime([
    [7, 1], [19, 3], [9, 4], [12, 5], [2, 8], [15, 10], [18, 12], [7, 14], [19, 16]
]))