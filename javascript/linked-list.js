class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

// Create 4 different nodes using the class Node 
const a = new Node("A");
const b = new Node("B");
const c = new Node("C");
const d = new Node("D");

// create link between the nodes to create the linked-list 
a.next = b;
b.next = c;
c.next = d;

const printLinkedList = (head) => {
    let current = head;
    while (current !== null) {
        console.log(current.val);
        current = current.next;
    } 
}

printLinkedList(a);

const printLLUsingRecursive = (head) => {
    if (head === null) return;
    console.log(head.val);
    printLLUsingRecursive(head.next);
}

printLLUsingRecursive(a);

const linkListValues = (head) => {
    let current = head;
    const result = [];
    while (current !== null) {
        result.push(current.val);
        current = current.next;
    }
    return result;
}

console.log(linkListValues(a));

const llvRecursive = (head, result = []) => {
    if (head === null) return;
    result.push(head.val);
    llvRecursive(head.next, result);
}

// sum the integers in linked-list
const e = new Node(2);
const f = new Node(8);
const g = new Node(3);
const h = new Node(7);

e.next = f;
f.next = g;
g.next = h;

printLLUsingRecursive(e);

const sumOfLinkedList= (head) => {
    sum = 0;
    let current = head;
    while (current !== null) {
        sum += current.val;
        current = current.next;
    }
    return sum;
}

console.log(sumOfLinkedList(e));

const sumOfLinkedListRecursive= (head, sum = 0) => {
    console.log('sum ', sum);
    if (head === null) return sum;
    sum += head.val;
    sumOfLinkedListRecursive(head.next, sum);
}

console.log(sumOfLinkedListRecursive(e));