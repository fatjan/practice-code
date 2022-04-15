function jumpingOnClouds(c) {
    // Write your code here
    let jumps = 0;

    for (let j = 0; j < c.length - 1; j++) {
        if (c[j] === 1) {
           continue;    
        }
        if (c[j+2] !== 1 && j !== c.length - 2) {
            jumps++;
            j++;
        } else {
            jumps++;
        }
    }
    console.log('jumps ', jumps);
    return jumps;
}

// jumpingOnClouds([0, 0, 0, 1, 0, 0]);
jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]);

// 0 1 3 4 6