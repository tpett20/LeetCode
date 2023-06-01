var searchInsert = function (nums, target) {
    let solutionIdx
    let first = 0
    let last = nums.length
    let midIdx = getMid(first, last)
    function getMid(firstNum, lastNum) {
        return Math.floor((lastNum - firstNum) / 2) + firstNum
    }
    console.log('midIdx', midIdx)
    search(midIdx, first, last)
    function search(idx, start, end) {
        if (nums[idx] === target) {
            solutionIdx = idx
        }
        else if (nums[idx] < target && nums[idx + 1] > target
            || nums[idx] < target && !nums[idx + 1]) {
            solutionIdx = idx + 1
        }
        else if (nums[idx] > target && nums[idx - 1] < target
            || nums[idx] > target && !nums[idx - 1]) {
            solutionIdx = idx
        }
        else if (nums[idx] > target) {
            end = idx
            idx = getMid(start, idx)
            search(idx, start, end)
        }
        else if (nums[idx] < target) {
            start = idx
            idx = getMid(idx, end)
            search(idx, start, end)
        }
    }
    return solutionIdx
}

// console.log(searchInsert([0,1,2,3,4,5,6,7,8,9,10,12,13,17,23,101,105,119], 11))
console.log([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 17, 23, 101, 105, 119].length)