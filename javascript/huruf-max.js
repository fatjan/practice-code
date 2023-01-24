let word = "Aku adalah Aku";
word = word.toLowerCase().split(' ').join('');
const huruf = {};

for (const element of word) {
    const char = element;
    if (!(char in huruf)) {
        huruf[char] = 1;
    } else {
        huruf[char] += 1;
    }
}


console.log('huruf ', huruf);

let max = 0;
let hurufMax;

for (const char in huruf) {
    if (huruf[char] > max) {
        max = huruf[char];
        hurufMax = char;
    }
}

console.log(`huruf terbanyak adalah ${hurufMax} ======> total : ${max} `);
