function minimumMoves(s) {
    let a = '';
    let moves = 0;
    for (let i = 0; i < s.length; i+=3) {
        if (s.slice(i, i+3).includes('X')) {
            a += 'OOO';
            moves++;
        } else {
            a += s.slice(i, i+3)
        }
    }
    return moves;
};

// console.log(minimumMoves('XXX'));
// console.log(minimumMoves('XXOX'));
minimumMoves('XXOX');
