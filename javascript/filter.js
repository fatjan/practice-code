const data = [
    {
        kelas: "7A",
        nama_lengkap: "Rizky",
        status_absen: "Hadir",
        tanggal: "Jumat, 31 Maret 2023",
        waktu_scan: "07:00:00",
    },
    {
        kelas: "9A",
        nama_lengkap: "Raphael",
        status_absen: "Hadir",
        tanggal: "Jumat, 31 Maret 2023",
        waktu_scan: "07:00:00",
    },
    {
        kelas: "8C",
        nama_lengkap: "Adil",
        status_absen: "Hadir",
        tanggal: "Jumat, 31 Maret 2023",
        waktu_scan: "07:00:00",
    },
    {
        kelas: "7B",
        nama_lengkap: "Nana",
        status_absen: "Hadir",
        tanggal: "Jumat, 31 Maret 2023",
        waktu_scan: "07:00:00",
    },
]

async function handlePrint() {
    classFilter = "7A";
    let filteredData = data;
    const keys = Object.keys(data[0]);
    console.log("keys", keys)
    if (classFilter) {
      filteredData = filteredData.filter(item => {
        console.log("item", item)
        // const itemData = item[keys];
        // console.log("itemData", itemData)
        const classNumber = classFilter.trim().toLowerCase(); // menghapus spasi di awal dan akhir, lalu mengubah menjadi lowercase
        console.log("classNumber", classNumber)
        console.log(item.kelas.toLowerCase())
        return item && item.kelas.toLowerCase() === classNumber; // mengubah kelas menjadi lowercase dan membandingkan dengan classNumber yang sudah diubah menjadi lowercase
      });
    }
    console.log("filteredData", filteredData)
    date = new Date();
    const inputDate = new Date(date);
    const options = {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    };
 
    const formattedDate = inputDate.toLocaleDateString('id-ID', options);
    console.log("formattedDate", formattedDate)
 
    if (formattedDate) {
      filteredData = filteredData.filter(item => {
        // const itemData = item[keys];
        return item && item.tanggal === formattedDate;
      });
    }
 
    console.log(filteredData);
 
    let rowsHtml = '';
 
    if (filteredData.length === 0) {
      rowsHtml += `
      <tr>
        <td colspan="6" style="text-align: center;">Tidak ada kriteria data yang sesuai.</td>
      </tr>
    `;
    } else {
      filteredData.forEach((item, index) => {
        const {nama_lengkap, kelas, status_absen, tanggal, waktu_scan} =
          item;
        rowsHtml += `
        <tr>
          <td>${index + 1}</td>
          <td>${tanggal}</td>
          <td>${nama_lengkap}</td>
          <td>${kelas}</td>
          <td>${waktu_scan}</td>
          <td>${status_absen}</td>
        </tr>
      `;
      });
    }
 
    const tableHtml = `
      <!DOCTYPE html>
      <html>
        <head>
          <style>
            table {
              font-family: arial, sans-serif;
              border-collapse: collapse;
              width: 100%;
            }
 
            h2 {
              text-transform: uppercase;
                text-align: center;
            }
 
            th {
              text-align: center;
            }
 
            td, th {
              border: 1px solid #dddddd;
              padding: 8px;
 
            }
 
            tr:nth-child(even) {
              background-color: #dddddd;
            }
          </style>
        </head>
      <body>
 
        <h2>Absensi Siswa</h2>
 
        <table>
            <thead>
              <tr>
                <th>No</th>
                <th>Tanggal</th>
                <th>Nama Lengkap</th>
                <th>Kelas</th>
                <th>Waktu Absen</th>
                <th>Status Absen</th>
              </tr>
            </thead>
            <tbody>
            ${rowsHtml}
            </tbody>
        </table>
 
    </body>
    </html>
  `;
  }

  handlePrint();