// 2363. Merge Similar Items
/*
You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:
- items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
- The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.
Note: ret should be returned in ascending order by value.
*/

var mergeSimilarItems = function(items1, items2) {
    const ret = []
    const map = {}
    for (let item of items1) {
        map[item[0]] = item[1]
    }
    for (let item of items2) {
        if (map[item[0]] === undefined) {
            map[item[0]] = item[1]
        } else {
            map[item[0]] += item[1]
        }
    }
    for (let key in map) {
        ret.push([parseInt(key), map[key]])
    }
    return ret
};

console.log(mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))