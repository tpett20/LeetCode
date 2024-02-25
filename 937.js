// 937. Reorder Data in Log Files
/*
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
There are two types of logs:
- Letter-logs: All words (except the identifier) consist of lowercase English letters.
- Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:
- The letter-logs come before all digit-logs.
- The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
- The digit-logs maintain their relative ordering.
Return the final order of the logs.
*/

var reorderLogFiles = function(logs) {
    let ltrLogs = []
    const digLogs = []
    for (let log of logs) {
        if (checkIfLtrLog(log)) {
            const logParts = separateLog(log)
            const ltrLog = [log, logParts[0], logParts[1]]
            ltrLogs.push(ltrLog)
        } else {
            digLogs.push(log)
        }
    }
    ltrLogs.sort((a, b) => {
        if (a[1] > b[1]) return 1
        if (a[1] < b[1]) return -1
        else {
            if (a[2] > b[2]) return 1
            if (a[2] < b[2]) return -1
        }
        return 0
    })
    ltrLogs = ltrLogs.map(log => log[0])
    return [...ltrLogs, ...digLogs]

    function checkIfLtrLog(logStr) {
        const idx = logStr.indexOf(" ") + 1
        if (isNaN(logStr[idx])) {
            return true
        } else {
            return false
        }
    }

    function separateLog(logStr) {
        const idx = logStr.indexOf(" ")
        const id = logStr.slice(0, idx)
        const content = logStr.slice(idx + 1)
        return [content, id]
    }
};

console.log(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
console.log(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))