// 706. Design HashMap
/*
Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
- MyHashMap() initializes the object with an empty map.
- void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
- int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
*/

var MyHashMap = function() {
    this.arr = new Array(1000000)
};

MyHashMap.prototype.put = function(key, value) {
    this.arr[key] = value
};

MyHashMap.prototype.get = function(key) {
    return this.arr[key] === undefined ? -1 : this.arr[key]
};

MyHashMap.prototype.remove = function(key) {
    this.arr[key] = undefined
};

const obj = new MyHashMap()
console.log(obj)
let key = 2
let value = 5
obj.put(key,value)
const param_2 = obj.get(key)
console.log(param_2)
obj.remove(key)
console.log(obj)