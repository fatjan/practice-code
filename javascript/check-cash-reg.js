function checkCashRegister(price, cash, cid) {
  const dict = {
    "PENNY": 0.01,
    "NICKEL": 0.05,
    "DIME": 0.1,
    "QUARTER": 0.25,
    "ONE": 1,
    "FIVE": 5,
    "TEN": 10,
    "TWENTY": 20,
    "ONE HUNDRED": 100,
  }
  const keep = {};
  let totalCid = 0;
  for (const i in cid) {
    const item = cid[i];
    keep[item[0]] = Math.round(item[1] / dict[item[0]]);
    totalCid += item[1];
  }
  let change = cash - price;
  let res;
  if (change > totalCid) {
    res = {status: "INSUFFICIENT_FUNDS", change: []};
  } else if (change == totalCid) {
    res = {status: "CLOSED", change: cid};
  } else {
    const changeValue = calculateChange(change, keep, dict);
    res = {status: "OPEN", change: changeValue};
  }
  return res;
}

// const res = checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
function calculateChange(change, keep, dict) {
  const result = [];
  for (let i = Object.keys(keep).length; i > 0; i--) {
    const entries = Object.entries(keep);
    const value = entries[i - 1][1];
    const name = entries[i - 1][0];
    console.log('change', change);
    console.log('keep[name] * dict[name]', keep[name] * dict[name]);
    if (change >= keep[name] * dict[name]) {
      const count = Math.floor(change / (value * dict[name]));
      console.log('count', count)
      if (count > value * dict[name]) {
        let howMuch = keep[name] * dict[name];
        if (name == 'NICKEL' || name == 'PENNY') {
          howMuch = howMuch.toFixed(2);
        }
        console.log('howMuch', howMuch);
        console.log('change', change);
        result.push([name, howMuch]);
        change -= dict[name] * value;
      } else {
        result.push([name, (keep[name] * dict[name])]);
        change -= dict[name] * value;
      }
    } else {
      let res = 0;
      while (change >= dict[name]) {
        res += dict[name];
        change -= dict[name];
      }
      if (res > 0) result.push([name, res]);
    }
    return result;
  }
  console.log('result', result);
  console.log('change', change);
  for (const i in keep) {
    const item = keep[i];
    if (change >= dict[i]) {
      const count = Math.floor(change / dict[i]);
      if (count > item) {
        result.push([i, (item * dict[i]).toFixed(2) * 1]);
        change -= item * dict[i];
      } else {
        result.push([i, count * dict[i]]);
        change -= count * dict[i];
      }
    }
  }
  console.log('result', result);
  console.log('change', change);
  if (change > 0) {
    return {status: "INSUFFICIENT_FUNDS", change: []};
  } else {
    return {status: "OPEN", change: result};
  }
}

let hasil = checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
console.log('hasil', hasil);

hasil = checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
console.log('hasil', hasil);