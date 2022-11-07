function pigIt(str){
    //Code here
    result = '';
    strArr = str.split(" ");
    const alphanumeric = /^[\p{L}\p{N}]*$/u;

    for (const word of strArr) {
        if (!word.match(alphanumeric)) result += word + ' ';
        else result += word.slice(1) + word[0] + 'ay ';
    }
    return result.substring(0, result.length - 1);
  }

pigIt('Hello World ! apa')
pigIt('Pig latin is cool')