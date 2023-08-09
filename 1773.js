// 1773. Count Items Matching a Rule
/*
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
The ith item is said to match the rule if one of the following is true:
- ruleKey == "type" and ruleValue == typei.
- ruleKey == "color" and ruleValue == colori.
- ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
*/

var countMatches = function(items, ruleKey, ruleValue) {
    let count = 0
    for (let item of items) {
        let key
        if (ruleKey === 'type') key = 0
        else if (ruleKey === 'color') key = 1
        else if (ruleKey === 'name') key = 2
        if (item[key] === ruleValue) count++
    }
    return count
};

console.log(countMatches(
    [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
    "color",
    "silver"
))