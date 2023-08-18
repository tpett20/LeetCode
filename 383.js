// 383. Ransom Note
/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
*/

var canConstruct = function (ransomNote, magazine) {
    const map = {}
    for (let char of magazine) {
        map[char] ? map[char]++ : map[char] = 1
    }
    for (let char of ransomNote) {
        if (map[char]) {
            map[char]--
        } else return false
    }
    return true
}

console.log(canConstruct('aa', 'aab'))


/* Solution with HashTable Class
var canConstruct = function (ransomNote, magazine) {
    class HashTable {
        constructor() {
            this.table = new Array(26)
        }

        _hash(key) {
            let hash = key.charCodeAt()
            return hash % this.table.length
        }

        set(key) {
            let hash = this._hash(key)
            if (this.table[hash]) {
                this.table[hash]++
            }
            else this.table[hash] = 1
        }

        check(key) {
            let hash = this._hash(key)
            if (this.table[hash]) {
                this.table[hash]--
                return true
            }
        }
    }
    const Table = new HashTable()
    for (let char of magazine) {
        Table.set(char)
    }
    for (let char of ransomNote) {
        if (!Table.check(char)) return false
    }
    return true
};
*/
