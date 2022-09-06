class Mathematic{
	constructor(angka1,angka2){
    	this.angka1= angka1;
      	this.angka2= angka2;
    }
  	penjumlahan(){
    	console.log(this.angka1 + this.angka2); 
      return this
    }
    pengurangan(){
    	console.log(this.angka1 - this.angka2); 
      return this
    }
    perkalian(){
    	console.log(this.angka1 * this.angka2); 
      return this
    }
    pembagian(){
    	console.log(this.angka1 / this.angka2); 
      return this
    }
    akarPangkat(){
      let angka1 = this.angka1
      let angka2 = this.angka2
      console.log(angka1**2);
      console.log(angka2**2); 
      return this
    }
    kelilingLingkaran() {
      let diameter = this.angka1 // diameter lingkaran
      console.log(Math.round((2 * 3.14) * diameter));
    }
}

let classmate = new Mathematic(21,8);

classmate.penjumlahan().pengurangan().perkalian().pembagian().akarPangkat().kelilingLingkaran()