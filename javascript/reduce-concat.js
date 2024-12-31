const arr = [4, 6, 1, 3, 1, 5]

const cumCal = xs => xs.reduce((acc, cur, i, self) => {
    const head = acc.length === 0 ? 0 : acc[0]
    const item = self[self.length - (i + 1)]
    
    return [item + head , ...acc]
}, [])

console.log(cumCal(arr))