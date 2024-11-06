// 3011. Find if Array Can Be Sorted
/*
You are given a 0-indexed array of positive integers nums.
In one operation, you can swap any two adjacent elements if they have the same number of set bits. You are allowed to do this operation any number of times (including zero).
Return true if you can sort the array, else return false.
*/

var canSortArray = function(nums) {
    function getSetBits(num) {
        let n = num
        let count = 0
        while (n >= 1) {
            let r = n % 2
            if (r === 1) {
                count++
            }
            n = Math.floor(n / 2)
        }
        return count
    }

    const arr = [...nums]
    const sbRef = {}
    for (let i = 0; i < arr.length; i++) {
        let change = false
        for (let j = 0; j < arr.length - i; j++) {
            const lt = arr[j]
            const rt = arr[j + 1]
            if (lt > rt) {
                if (sbRef[lt] === undefined) {
                    sbRef[lt] = getSetBits(lt)
                }
                if (sbRef[rt] === undefined) {
                    sbRef[rt] = getSetBits(rt)
                }
                const lSetBits = sbRef[lt]
                const rSetBits = sbRef[rt]
                if (lSetBits !== rSetBits) {
                    return false
                }
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
                change = true
            }
        }
        if (change === false) {
            return true
        }
    }
    return true
};

console.log(canSortArray([8, 4, 2, 30, 15]))
console.log(canSortArray([3, 16, 8, 4, 2]))