// 1436. Destination City
// You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
// It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

var destCity = function(paths) {
    const map = {}
    for (let path of paths) {
        map[path[0]] = true
        if (!map[path[1]]) {
            map[path[1]] = false
        }
    }
    for (let key in map) {
        if (!map[key]) {
            return key
        }
    }
};

console.log(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))