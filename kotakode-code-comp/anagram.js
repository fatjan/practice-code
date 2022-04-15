function membuatAnagram(str1,str2){
    let output = 0
    let kata1 = str1
    let kata2 = str2
    str1.split('').forEach(char => {
     if (!(str2.includes(char))) {
        kata1 = kata1.replace(char, '')
        output++
     }   
    });
    str2.split('').forEach(char => {
        if (!(str1.includes(char))) {
           kata2 = kata2.replace(char, '')
           output++
        }   
       });
    return output
}

const str1 = 'skeuo'
const str2 = 'woiub'

console.log(membuatAnagram(str1, str2))