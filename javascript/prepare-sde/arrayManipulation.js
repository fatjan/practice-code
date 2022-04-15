function arrayManipulation(n, queries) {
    // Write your code here
    const matrix = new Array(n).fill(0).map(() => new Array(n).fill(0));
    let a;
    let b;
    let k;
    const biggest = [];
    
    for (let x in queries) {
        a = queries[x][0];
        b = queries[x][1];
        k = queries[x][2];
        let largest;
        for (let i=0; i < matrix.length; i++) {
            for (let j=0; j < matrix[i].length; j++) {
                if (j+1 >= a && j+1 <= b) {
                    matrix[i][j] += k;
                }
            }
            largest = Math.max(matrix[i]);
            biggest.push(largest);
        }
    }
    
    return Math.max(biggest);
}

arrayManipulation()