function foo(codeList, shoppingCart) {
    const code = [];
    const translator = {};
    let num = 0;

    for (let x in codeList) {
        for (let y in codeList[x]) {
            const number = getKeyByValue(translator, codeList[x][y]);
            if (!(number.toString() in translator)) {
                if (codeList[x][y] === 'anything') {
                    translator[num] = '*';
                } 
                num += 1;
                translator[num] = codeList[x][y];
                code.push(num);
            } else {
                console.log('number ', number);
                translator[number] = codeList[x][y];
                code.push(parseInt(number));
            }
        }
    }
    console.log('code ', code);
    console.log('translator ', translator);

}

function getKeyByValue(object, value) {
    return Object.keys(object).find(key => object[key] === value);
  }

foo([['apple', 'apple'], ['banana', 'anything', 'banana']])