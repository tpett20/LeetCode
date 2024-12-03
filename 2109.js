// 2109. Adding Spaces to a String
/*
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.
    For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.
*/

var addSpaces = function(s, spaces) {
    let output = ""
    let j = 0
    for (let i = 0; i < s.length; i++){
        if (i === spaces[j]) {
            output += " "
            j++
        }
        output += s[i]
    }
    return output
};

console.log(addSpaces("LetsGoMets", [4,6]))
console.log(addSpaces("SPACEMAN", [0,1,2,3,4,5,6,7]))