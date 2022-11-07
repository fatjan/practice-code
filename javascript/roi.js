function calculateROI(costData, ordersData) {
    const result = {};

    for (const data of costData) {
        result[data.menu] = {
            stock: data.stock,
            investment: data.investment,
        }
    }

    for (const item of orderHistories) {
        if (result[item.menuItem].stock >= item.amount) {
            result[item.menuItem].stock -= item.amount;

            result[item.menuItem].sales = item.amount * item.price;
            result[item.menuItem].profit = result[item.menuItem].sales - result[item.menuItem].investment;
        }
    }

    const res = [];
    for (const item in result) {
        const menu = result[item];
        const roi = menu.profit / menu.investment * 100;
        const data = {
            menu: item,
            stock: menu.stock,
            investment: menu.investment,
            sales: menu.sales,
            profit: menu.profit,
            roi,
        }

        res.push(data);
    }

    console.log('res', res);
}

const costData = [{
        menu: "Bakso Spesial",
        stock: 300,
        investment: 780000
    },
    {
        menu: "Mie Ayam Combo",
        stock: 30,
        investment: 60000
    },
    {
        menu: "Mie Ayam Spesial",
        stock: 10,
        investment: 200000
    }];

const orderHistories = [{
        menuItem: "Bakso Spesial",
        price: 20000,
        amount: 260,
    },
    {
        menuItem: "Bakso Spesial",
        price: 20000,
        amount: 12,
    },
    {
        menuItem: "Mie Ayam Combo",
        price: 18000,
        amount: 20,
    },
    {
        menuItem: "Mie Ayam Spesial",
        price: 12000,
        amount: 6,
    }
]

calculateROI(costData, orderHistories);