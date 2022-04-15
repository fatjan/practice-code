function arrayManipulation(n, queries) {
    // Write your code here
    const arr = Array(n).fill(0);
    let a, b, value;
    for (let x in queries) {
        a = queries[x][0];
        b = queries[x][1];
        value = queries[x][2];
        for (let i = 0; i < arr.length; i++) {
            if (i <= b-1 && i >= a-1) {
                arr[i] += value;
            }
        }
    }

    return Math.max(...arr);
}

console.log(arrayManipulation(5, [[ 1, 2, 100 ], [ 2, 5, 100 ], [ 3, 4, 100 ]]))