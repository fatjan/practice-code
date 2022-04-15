let angka = [1, 46, 75, 12, 89, 54, 101, 100];
let genap = [];
// for (let i in angka) {
//   console.log('ini i ', i)
//   if (angka[i] % 2 == 0) {
//     console.log(angka[i]);
//     genap.push(angka[i]);
//   }
// }

for (let i = 0; i<angka.length; i++) {
    if (angka[i] % 2 == 0) {
        genap.push(angka[i])
    }
}
console.log('ini genap ', genap)