function removeDuplicates(nums) {
    for (let i = nums.length - 1; i >= 1; i--) {
        if (nums[i] === nums[i - 1]) {
            nums.splice(i, 1)
        }
    }
    console.log('final answer', nums)
    return nums.length
}

removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
removeDuplicates([1, 1, 2])
removeDuplicates([0])
removeDuplicates([])