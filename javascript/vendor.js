const data = [
    {
        data: [
            { vendorId: 1, vendorName: 'A', team: 'TEAM_1' },
            { vendorId: 2, vendorName: 'B', team: 'TEAM_1' },
        ]
    },
    {
        data: [
            { vendorId: 1, vendorName: 'A', team: 'TEAM_2' },
            { vendorId: 2, vendorName: 'B', team: 'TEAM_1' },
        ]
    },
    {
        data: [
            { vendorId: 1, vendorName: 'A', team: 'TEAM_3' },
            { vendorId: 2, vendorName: 'B', team: 'TEAM_1' },
            { vendorId: 3, vendorName: 'C', team: 'TEAM_1' },
        ]
    }
]

const result = [];

for (const item of data) {
    for (const vendor of item.data) {
        const foundVendor = result.find((r) => r.vendorId === vendor.vendorId)
        if (!foundVendor) {
            vendor.team = [vendor.team];
            result.push(vendor);
        } else if (!(foundVendor.team.includes(vendor.team))) {
            const index = result.indexOf(foundVendor);
            foundVendor.team.push(vendor.team);
            result[index] = foundVendor;
        }
    }
}

const updatedResult = [];
for (const res of result) {
    const data = {
        vendor_id: res.vendorId,
        vendor_name: res.vendorName,
        total_team: res.team.length
    }
    updatedResult.push(data);
}

console.log(updatedResult);