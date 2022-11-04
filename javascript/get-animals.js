function getAnimals(arr) {
    let kar = '';
    let her = '';
    let om = '';

    for (const item of arr) {
        const [animal, code] = item.split(":");

        if (code === 'K' && animal.length > kar.length) {
            kar = animal
        } else if (code === 'H' && animal.length > her.length) {
            her = animal
        } else if (code === 'O' && animal.length > om.length) {
            om = animal
        }
    }

    return [kar, her, om]
}

console.log(getAnimals(['Singa:K', 'Kuda:H', 'Monyet:O']))
// ['Singa', 'Kuda', 'Monyet']

console.log(getAnimals(['Macan:K', 'Ayam:O', 'Gajah:H', 'Monyet:O', 'Kerbau:H', 'Musang:O', 'Burung:H', 'Hiu:K']))
// ['Macan', 'Kerbau', 'Monyet']

console.log(getAnimals(['Tikus:O', 'Merpati:H', 'Beruang:O', 'Elang:K', 'Perkutut:H', 'Harimau:K']))
// ['Harimau', 'Perkutut', 'Beruang']
