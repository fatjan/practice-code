function solution(roman){
    // complete the solution by transforming the 
    // string roman numeral into an integer  
    total = 0;
  
    for (let i = 0; i < roman.length-1; i++) {
      const a = convert(roman[i]);
      const b = convert(roman[i+1]);
      const c = a >= b ? a + b : b - a;
      console.log(c);
      total += c;
      i += 1;
    }
    
    function convert(huruf) {
      let number = 0;
      switch(huruf) {
        case 'I':
          number = 1;
          break;
        case 'V':
          number = 5;
          break;
        case 'X':
          number = 10;
          break;
        case 'L':
          number = 50;
          break;
        case 'C':
          number = 100;
          break;
        case 'D':
          number = 500;
          break;
        case 'M':
          number = 1000;
          break;
        default:
          number = 1;
      }
     return number
    }
    
    return total;
}

console.log((solution('XXI'), 21))