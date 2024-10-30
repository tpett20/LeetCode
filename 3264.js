// 3264. Final Array State After K Multiplication Operations I
/*
You are given an integer array nums, an integer k, and an integer multiplier.
You need to perform k operations on nums. In each operation:
    Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
    Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.
*/
var getFinalState = function(nums, k, multiplier) {
    function getMinIdx(arr) {
        let low = Infinity
        let lowIdx = arr.length
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] < low) {
                low = arr[i]
                lowIdx = i
            }
        }
        return lowIdx
    }

    if (multiplier === 1) return nums
    const output = [...nums]
    for (let i = 0; i < k; i++) {
        const minIdx = getMinIdx(output)
        output[minIdx] *= multiplier
    }
    return output
};

console.log(getFinalState([2,1,3,5,6], 5, 2))