// 786. K-th Smallest Prime Fraction
/*
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
*/

var kthSmallestPrimeFraction = function(arr, k) {
    const sorted = []
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            const quot = arr[i] / arr[j]
            sorted.push([arr[i], arr[j], quot])
        }
    }
    sorted.sort((a, b) => a[2] - b[2])
    sorted[k - 1].pop()
    return sorted[k - 1]
};

console.log(kthSmallestPrimeFraction([1,2,3,5], 3))
console.log(kthSmallestPrimeFraction([1,7], 1))