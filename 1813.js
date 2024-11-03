// 1813. Sentence Similarity III
/*
You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.
Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.
For example,
    s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
    s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.
*/

var areSentencesSimilar = function(sentence1, sentence2) {
    if (sentence1 === sentence2) {
        return true
    }
    const words1 = sentence1.split(" ")
    const words2 = sentence2.split(" ")
    if (words1.length === words2.length) {
        return false
    }
    const moreWords = (words1.length > words2.length) ? words1 : words2
    const lessWords = (words1.length > words2.length) ? words2 : words1
    let rtMore = moreWords.length - 1
    let rtLess = lessWords.length - 1
    while (moreWords[rtMore] === lessWords[rtLess]) {
        rtMore--
        rtLess--
    }
    if (rtLess === -1) {
        return true
    }
    let ltMore = 0
    let ltLess = 0
    while (moreWords[ltMore] === lessWords[ltLess]) {
        ltMore++
        ltLess++
    }
    if (ltLess === lessWords.length) {
        return true
    }
    if (ltLess <= rtLess) {
        return false
    }
    return true
};

console.log(areSentencesSimilar("My name is Thomas", "My Thomas"))
console.log(areSentencesSimilar("is", "My name is Thomas"))
console.log(areSentencesSimilar("Eating right now", "now"))
console.log(areSentencesSimilar("Pop corn corn corn corn", "corn"))