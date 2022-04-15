function hilangkanDuplikat(inputList){
    let output = [];
    let keep = [];
    inputList.forEach(num => {
      if (!(keep.includes(num))) {
        keep.push(num);
        output.push(num);
      } else {
        output.push(0);
      }
    });
    return output;
  }

const intList = [1, 3, 5, 6, 2, 6, 6, 2, 9, 10];
const nums = [1, 1, 2, 2, 3, 4, 5];
const satus = [1, 1, 1, 1, 1, 1, 1];
const distinct = [1, 2, 3, 4, 5, 6, 7];

console.log(hilangkanDuplikat(distinct));