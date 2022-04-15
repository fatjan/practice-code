function kasihPerangko(arr1){
  let output = 0; 
  let given = 1;
  for (let i = 0; i < arr1.length; i++) {
    if (i === 0) {
      given = 1;
    } else if (arr1[i] > arr1[i-1]) {
      given += 1;
    } else if (arr1[i] < arr1[i-1]) {
      if (i !== arr1.length-1 && arr1[i] > arr1[i+1]) {
        given = 2;
      } else {
        given = 1;
      }
    } else if (arr1[i] === arr1[i-1]) {
      given = 1;
    }
    output += given;
  };
  return output
}

const perangko = [4, 6, 4, 5, 6, 2];
const per2 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1];
const per3 = [2, 4, 3, 5, 2, 6, 4, 5];
const per4 = [2, 3, 3, 4];

console.log(kasihPerangko(per4));