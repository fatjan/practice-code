function convertNumber(arr) {
    let result = "";
    let alpha = "abcdefghijklmnopqrstuvwxyz";

    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[i].length; j++) {
            const index = arr[i][j]
            result += alpha[index-1]
        };
        result += " "
    }

    return result
}

console.log(convertNumber([[9], [12, 15, 22, 5], [25, 15, 21]]))