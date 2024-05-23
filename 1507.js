// 1507. Reformat Date
/*
Given a date string in the form Day Month Year, where:
- Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
- Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
- Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:
- YYYY denotes the 4 digit year.
- MM denotes the 2 digit month.
- DD denotes the 2 digit day.
*/

var reformatDate = function(date) {
    const months = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", 
        "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    const parts = date.split(" ")
    let output = ""
    output += parts[2] + "-"
    output += months[parts[1]] + "-"
    let day = "", i = 0
    while (true) {
        const code = parts[0].charCodeAt(i)
        if (code >= 48 && code <= 57) {
            day += parts[0][i]
        } else break
        i++
    }
    if (day.length === 1) {
        day = "0" + day
    }
    return output + day
};

console.log(reformatDate("20th Oct 2052"))
console.log(reformatDate("6th Jun 1933"))
console.log(reformatDate("26th May 1960"))