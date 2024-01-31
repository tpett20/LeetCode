// 739. Daily Temperatures - INCOMPLETE 🚫 Time Limit Exceeded
// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

var dailyTemperatures = function(temperatures) {
    const sorted_arr = []
    const obj = {}
    const output = new Array(temperatures.length)
    for (let i = temperatures.length - 1; i >= 0; i--) {
        const temp = temperatures[i]
        const idx = binarySearch(temp, sorted_arr)
        obj[temp] = i
        let nxt_warm_idx = Infinity
        for (let j = idx + 1; j < sorted_arr.length; j++) {
            if (sorted_arr[j] === temp) continue
            nxt_warm_idx = Math.min(obj[sorted_arr[j]], nxt_warm_idx)
        }
        output[i] = (nxt_warm_idx === Infinity) ? 0 : nxt_warm_idx - i
    }
    return output
    
    function binarySearch(item, arr) {
        if (!arr.length) {
            arr.push(item)
            return 0
        }
        let midIdx = Math.floor(arr.length / 2)
        let floor = 0
        let ceil = arr.length - 1
        while (floor <= ceil) {
            if (item === arr[midIdx] || (item > arr[midIdx] && item < arr[midIdx + 1])) {
                arr.splice(midIdx + 1, 0, item)
                return midIdx + 1
            } else if (item > arr[midIdx]) {
                floor = midIdx + 1
                midIdx = Math.floor((ceil + floor) / 2)
            } else if (item < arr[midIdx]) {
                ceil = midIdx - 1
                midIdx = Math.floor((ceil + floor) / 2)
            }
        }
        if (midIdx < 0) {
            arr.splice(0, 0, item)
            return 0
        } else if (midIdx >= arr.length - 1) {
            arr.splice(arr.length, 0, item)
            return arr.length - 1
        }
    }
};

console.log(dailyTemperatures([73,74,75,71,69,72,76,73]))
console.log(dailyTemperatures([30,40,50,60]))
console.log(dailyTemperatures([30,60,90]))