// 1481. Least Number of Unique Integers after K Removals
// Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

var findLeastNumOfUniqueInts = function(arr, k) {
    if (arr.length === k) return 0
    const freq = {}
    for (let num of arr) {
        freq[num] = freq[num] ? ++freq[num] : 1
    }
    const u_nums = Object.keys(freq)
    u_nums.sort((a, b) => freq[a] - freq[b])
    let i = 0
    while (k) {
        if (freq[u_nums[i]] <= k) {
            k -= freq[u_nums[i]]
            i++
        } else break
    }
    return u_nums.length - i
};

console.log(findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))