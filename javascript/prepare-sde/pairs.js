function sockMerchant(n, ar) {
    // Write your code here
    const keep = [];
    let pairs = 0;
    let i;
    
    for (let x in ar) {
        if (!(keep.includes(ar[x]))) {
            keep.push(ar[x])
        } else {
            i = keep.indexOf(ar[x]);
            keep.splice(i, 1); 
            pairs++;
        }
    }
    
    return pairs;
}

sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]);