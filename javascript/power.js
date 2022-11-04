function simFra(arr) {
    for (let i = 2;i <= arr[1];i++) {
        if (arr[0] % i == 0 && arr[1] % i == 0) {
           return [arr[0] / i,arr[1] / i]
        }
    }    
    return arr 
}

function intPow(num,pow) {
    let hasil = 1 
    
    for (let count = 1;count <= pow;count++) {
            hasil *= num;
    }
    return pow == 0 ? 0 : parseInt(hasil)
}

function decPow(num,pow) {
    multiply = intPow(10,pow.toString().split('.')[1].length)
    powFrac = simFra([pow*multiply,multiply])
    
    decision = intPow(num,powFrac[0])
    
    let result = ''
    let i = 0
    
    while (true) {
        if (intPow(i,powFrac[1]) == decision) {
            return i
        } 
        if (intPow(i,powFrac[1]) > decision) {
            result = i - 1 + '.'
            break
        }
        i++
    }
    
    let source = 0
    while (intPow(parseFloat(result),powFrac[1]) !== decision) {
        i = 0
        while (true) {
            source = intPow(parseFloat(result+i),powFrac[1])
            if (source > decision) {
                result += i - 1
                break
            }
            i += 1
        }   
    }
    return parseFloat(result)
}

console.log(decPow(9,0.5))