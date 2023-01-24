function totalFruit(fruit, ...data) {
    console.log('data', data);
    let total = 0;
    for (const item of data) {
        console.log('item ', item)
        total += item;
    } 

    console.log('ini fruit ', fruit);

    console.log('ini total ', total);
}

totalFruit('Mango', 12);