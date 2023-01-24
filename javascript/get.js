function multiply(a, b = 5) {
    return a * b
}

c = {
    age: 25,
    salary: 20,
}
if (!('num' in c)) c.num = 250;
const res = multiply(c.age, c.num);

console.log('res', res);