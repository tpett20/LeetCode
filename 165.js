// 165. Compare Version Numbers
/*
Given two version numbers, version1 and version2, compare them.
Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.
To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.
Return the following:
- If version1 < version2, return -1.
- If version1 > version2, return 1.
- Otherwise, return 0.
*/

var compareVersion = function(version1, version2) {
    const v1arr = version1.split(".")
    const v2arr = version2.split(".")
    const longest = Math.max(v1arr.length, v2arr.length)
    for (let i = 0; i < longest; i++) {
        const rev1 = v1arr[i] ? parseInt(v1arr[i]) : 0
        const rev2 = v2arr[i] ? parseInt(v2arr[i]) : 0
        if (rev1 > rev2) return 1
        else if (rev1 < rev2) return -1
    }
    return 0
};

console.log(compareVersion("1.01", "1.001"))
console.log(compareVersion("1.0", "1.0.0"))
console.log(compareVersion("0.1", "1.1"))