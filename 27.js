function removeElement(nums, val) {
    for (let i = nums.length - 1; i >= 0; i--) {
        if (nums[i] === val) {
            nums.splice(i, 1)
        }
    }
    console.log('final answer:', nums)
    return nums.length
}

removeElement([3, 2, 2, 3], 3)
removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)