
// function reverseString(string){
//     var reversed = ''
//     for(var i=0, j=string.length-1; i<j; i++, j--){
//         // console.log(string[i])
//             var temp = string[i]
//             string[i] = string[j]
//             string[j] = temp


//             console.log(temp)
//         }
//         reversed=string
//         return reversed
//     }


// reversed=reverseString("creature")
// console.log(reversed)

function reverseString(str) {
    let newString = "";
    for (let i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    console.log(newString)
}

reverseString("creature")