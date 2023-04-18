const dataAwal = [
    {
        "uraian": "Beli Komputer", 
        "id": 1637, 
        "uraian_id": 146, 
        "anggaran_ke": 1, 
        "vol1_value": null, 
        "vol1_unit": null, 
        "vol2_value": null, 
        "vol2_unit": null, 
        "vol3_value": null, 
        "vol3_unit": null, 
        "vol4_value": null, 
        "vol4_unit": null, 
        "harga_satuan": null, 
        "total_harga": null 
    },
    {
        "uraian": "Beli Komputer", 
        "id": 1640, 
        "uraian_id": 149, 
        "anggaran_ke": 1, 
        "vol1_value": null, 
        "vol1_unit": null, 
        "vol2_value": null, 
        "vol2_unit": null, 
        "vol3_value": null, 
        "vol3_unit": null, 
        "vol4_value": null, 
        "vol4_unit": null, 
        "harga_satuan": null, 
        "total_harga": null 
    },
    {
        "uraian": "Beli Baju", 
        "id": 1638, 
        "uraian_id": 147, 
        "anggaran_ke": 2, 
        "vol1_value": null, 
        "vol1_unit": null, 
        "vol2_value": null, 
        "vol2_unit": null, 
        "vol3_value": null, 
        "vol3_unit": null, 
        "vol4_value": null, 
        "vol4_unit": null, 
        "harga_satuan": null, 
        "total_harga": null 
    },
    {
        "uraian": "Makan Pizza", 
        "id": 1639, 
        "uraian_id": 148, 
        "anggaran_ke": 3, 
        "vol1_value": null, 
        "vol1_unit": null, 
        "vol2_value": null, 
        "vol2_unit": null, 
        "vol3_value": null, 
        "vol3_unit": null, 
        "vol4_value": null, 
        "vol4_unit": null, 
        "harga_satuan": null, 
        "total_harga": null 
    },
]

const res = [];

for (const data of dataAwal) {
    const item = {
        anggaran_ke: data.anggaran_ke,
    };
    delete data.anggaran_ke;
    item.details = [data]
    res.push(item);
} 

console.log(res)