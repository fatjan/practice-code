let str = "aku adalah aku";
let maxLetter = '';
let maxCount = 0;

for (let i = 0; i < str.length; i++) {
  let count = 0;
  for (let j = i; j < str.length; j++) {
    if (str[i] === str[j]) {
      count++;
    }
  }
  if (count > maxCount) {
    maxCount = count;
    maxLetter = str[i];
  }
}
console.log(maxLetter);