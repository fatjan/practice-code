function urutHuruf(string) {
    keep = {}

    for (const char of string) {
        if (char in keep) keep[char] += 1;
        else keep[char] = 1;
    }

    result = '';
    for (const key in keep) {
        result += key.repeat(keep[key])
    }

    return result;
}

console.log(urutHuruf('aeae'))
console.log(urutHuruf('ieaeaai'))
console.log(urutHuruf('abcdcbadebcfacaedbc'))

