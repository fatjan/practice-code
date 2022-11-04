function convertNumber(arr) {
    let result = "";
    let alpha = "abcdefghijklmnopqrstuvwxyz";

    for (const item of arr) {
        item.forEach(element => {
            result += alpha[element-1]
        });
        result += " "
    }

    return result
}

console.log(convertNumber([[9], [12, 15, 22, 5], [25, 15, 21]]))