// 2558. Take Gifts From the Richest Pile
/*
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
    Choose the pile with the maximum number of gifts.
    If there is more than one pile with the maximum number of gifts, choose any.
    Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.
*/

var pickGifts = function(gifts, k) {
    function getInsertIdx(nums, target) {
        let flr = 0, ceil = nums.length - 1
        while (flr <= ceil) {
            const mid = Math.floor((flr + ceil) / 2)
            if (nums[mid] > target) {
                ceil = mid - 1
            } else if (nums[mid] < target) {
                flr = mid + 1
            } else {
                return mid
            }
        }
        return flr
    }

    const arr = gifts.toSorted((a, b) => a - b)
    for (let i = 0; i < k; i++) {
        const newVal = Math.floor(Math.sqrt(arr.pop()))
        const idx = getInsertIdx(arr, newVal)
        arr.splice(idx, 0, newVal)
        if (arr.at(-1) === 1) return arr.length
    }
    return arr.reduce((total, val) => {
        return total + val
    })
};

console.log(pickGifts([25, 64, 9, 4, 100], 4))
console.log(pickGifts([25, 64, 9, 4, 100], 100))