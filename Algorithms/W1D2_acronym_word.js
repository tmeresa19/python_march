// function acronymize(string) {
//     var newWord = true;
//     var acr = '';
//     for (var i = 0; i < string.length; i++) {
//         if (string[i] == ' ') {
//             newWord = true;
//         }
//         else if (string[i] !== ' ' && newWord == true) {
//             newWord = false;
//             var code = string[i].charCodeAt(0);
//             if (code > 96) {
//                 code -= 32;
//                 acr += String.fromCharCode(code)
//             }
//             else {
//                 acr += string[i];
//             }
//         }
//     }
//     return acr
// }

// console.log(acronymize('Hi my name is Joseph'))
// console.log(acronymize('    hello     world   ')) 


// or

function acronymize(str) {
    let acronym = "";
    let newArray = str.split(" ")
    console.log(newArray)
    for (let i = 0; i < newArray.length; i++) {
        let word = newArray[i];
        if (word.length > 0) {
            acronym += word[0].toUpperCase();
        }
    }
    console.log(acronym)
}

acronymize("hello worlD")