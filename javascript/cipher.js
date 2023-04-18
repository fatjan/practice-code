function nextLetterInAlphabet(letter) {
    return String.fromCharCode(letter.charCodeAt(0) + 13);
}

function rot13(str) {
  let result = '';
  for (let char of str) {
    console.log('before',char);
    if (RegExp(/^\p{L}/,'u').test(char)) {
      char = nextLetterInAlphabet(char);
      console.log('after',char);
    };
    result += char;
  }
  return result;
}

rot13("SERR PBQR PNZC");