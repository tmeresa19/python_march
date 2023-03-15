/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
const expected1 = "test a is This";

const str2 = "hello";
const expected2 = "hello";

const str3 = "   This  is a   test  ";
const expected3 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */

function reverseWordOrder(str) {
    // Split the string into an array of words
    var words = str.split(" ");

    // Create a new array to hold the reversed words
    var reversedWords = [];

    // Loop through the words in reverse order and add them to the new array
    for (var i = words.length - 1; i >= 0; i--) {
        reversedWords.push(words[i]);
    }

    // Join the reversed words back together into a string
    var reversedStr = reversedWords.join(" ");

    // Return the reversed string
    return reversedStr;
}

var str = "Hello world, how are you?";
var reversedStr = reverseWordOrder(str);
console.log(reversedStr); // "you? are how world, Hello"
