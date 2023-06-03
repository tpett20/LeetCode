/* 
1672. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
*/

var maximumWealth = function(accounts) {
    return accounts.reduce((largestAccount, eachAccount) => {
        let sum = eachAccount.reduce((total, eachBank) => {
            return total + eachBank
        }, 0) 
        return sum > largestAccount ? sum : largestAccount
    }, 0)
};

console.log(maximumWealth(([[1,2,3], [3,2,1]])))
console.log(maximumWealth([[1,5], [7,3], [3,5]]))
console.log(maximumWealth([[2,8,7], [7,1,3], [1,9,5]]))
console.log(maximumWealth([[2], [3], []]))
console.log(maximumWealth([[0], [0]]))
console.log(maximumWealth([[10]]))