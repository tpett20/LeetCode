// 1716. Calculate Money in Leetcode Bank
/*
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
*/

var totalMoney = function(n) {
    const fullWeeks = Math.floor(n / 7)
    const baseSum = fullWeeks * 28
    const growthSum = (fullWeeks - 1) * fullWeeks * 7 / 2
    const remainderDays = n % 7
    let remainderSum = remainderDays * (remainderDays + 1) / 2
    remainderSum += remainderDays * fullWeeks
    return baseSum + growthSum + remainderSum
};

console.log(totalMoney(4))
console.log(totalMoney(10))
console.log(totalMoney(20))
console.log(totalMoney(283))