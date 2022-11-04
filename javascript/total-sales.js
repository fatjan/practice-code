const data = [
    {
        salesName: 'Udin',
        totalSales: 100,
        salesDate: 1
    },
    {
        salesName: 'Udin',
        totalSales: 20,
        salesDate: 1
    },
    {
        salesName: 'Poltak',
        totalSales: 100,
        salesDate: 1
    },
    {
        salesName: 'Poltak',
        totalSales: 50,
        salesDate: 2
    },
    {
        salesName: 'Sri',
        totalSales: 0,
        salesDate: 1
    },
    {
        salesName: 'Adi',
        totalSales: 0,
        salesDate: 1
    },
    {
        salesName: 'Budi',
        totalSales: 0,
        salesDate: 1
    },
];

const result = {}

data.forEach(item => {
    if (item.salesName in result) {
        result[item.salesName] += item.totalSales;
    } else {
        result[item.salesName] = item.totalSales;
    }
});

console.log('result ', result);