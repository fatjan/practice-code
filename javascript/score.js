function scoreChecker(score) {
    let result;
  
    // TODO
    if (score >= 90) {
      result = 'Selamat! Anda mendapatkan nilai A.'
    } else if (score >= 80 && score < 90) {
      result = 'Selamat! Anda mendapatkan nilai B.'
    } else if (score >= 70 && score < 80) {
      result = 'Selamat! Anda mendapatkan nilai C.'
    } else if (score >= 60 && score < 70) {
      result = 'Selamat! Anda mendapatkan nilai D.'
    } else if (score < 60) {
      result = 'Selamat! Anda mendapatkan nilai E.'
    }
  
  
    // Jangan hapus kode ini
    return result;
  }

  console.log(scoreChecker(88))
  console.log(scoreChecker(78))
  console.log(scoreChecker(68))
  console.log(scoreChecker(58))
