// 383. Ransom Note
/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
*/

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
                let i = 0
                while (this.table[hash][i]) {
                    i++
                }
                this.table[hash][i] = key
            }
            else {
                this.table[hash] = [key]
            }
        }

        get(key) {
            let hash = this._hash(key)
            if (this.table[hash]) {
                let i = 0
                while (this.table[hash][i]) {
                    if (key === this.table[hash][i]) {
                        return this.table[hash][i]
                    }
                    else i++
                }
            }
        }

        remove(key) {
            let hash = this._hash(key)
            if (this.table[hash]) {
                let i = 0
                while (this.table[hash][i]) {
                    if (key === this.table[hash][i]) {
                        this.table[hash][i] = 'removed'
                        return
                    }
                    else i++
                }
            }
        }
    }
    const Table = new HashTable()
    for (let char of magazine) {
        Table.set(char)
    }
    for (let char of ransomNote) {
        if (!Table.get(char)) return false
        Table.remove(char)
    }
    return true
};

console.log(canConstruct('aa', 'aab'))