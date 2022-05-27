class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

const printLinkedList = (head) => {
    let current = head;
    while (current !== null) {
        console.log(current.val);
        current = current.next;
    } 
}

printLinkedList(a);

const reverseList = (head) => {
    // todo
    let prev = null;
    let current = head;
    let next = null;

    while (current !== null) {
      next = current.next;
      current.next = prev;
      prev = current;
      current = next; 
    }
    return prev;
  };
  
  printLinkedList(reverseList(a));
  
  
  
  
  
  
  
  
  
  
  
  
