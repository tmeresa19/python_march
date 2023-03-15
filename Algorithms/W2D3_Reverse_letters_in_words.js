/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
  // Split the input string into an array of words using the space character as the separator
  var wordsArr = str.split(" ");
  // Create an empty array to store the reversed words
  var reversedWordsArr = [];

  // Loop through each word in the wordsArr array
  for (var i = 0; i < wordsArr.length; i++) {
    // Get the current word in the iteration
    var word = wordsArr[i];
    // Create an empty string to store the reversed version of the word
    var reversedWord = "";

    // Loop through each character in the word, starting from the end
    for (var j = word.length - 1; j >= 0; j--) {
      // Append the current character to the reversedWord string
      reversedWord += word[j];
    }

    // Push the reversedWord into the reversedWordsArr array
    reversedWordsArr.push(reversedWord);
  }

  // Join the reversedWordsArr array into a string, with spaces between the words
  var reversedStr = reversedWordsArr.join(" ");

  // Return the reversed string
  return reversedStr;
}


var inputStr = "Hello world, how are you?";
var reversedStr = reverseWords(inputStr);

console.log(reversedStr); // "olleH dlrow, woh era ?uoy"






