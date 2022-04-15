const run = (iterations, text) => {
    if (Number(iterations) && text) {
        return { data: Array.from({length: iterations}, () =>  text) };
      }
    
      return {};
}

console.log(run(3, 'ini aku'))