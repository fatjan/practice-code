function birthdayCakeCandles(candles) {
    // Write your code here
    const max = Math.max(...candles);
    return candles.filter(x => x === max).length
}

console.log(birthdayCakeCandles([3, 2, 1, 3]))