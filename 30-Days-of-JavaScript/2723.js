// 2723. Add Two Promises
// Given two promises promise1 and promise2, return a new promise. promise1 and promise2 will both resolve with a number. The returned promise should resolve with the sum of the two numbers.

var addTwoPromises = async function(promise1, promise2) {
    let sum = 0
    sum += await promise1
    sum += await promise2
    return sum
};

addTwoPromises(Promise.resolve(2), Promise.resolve(2))
    .then(console.log)