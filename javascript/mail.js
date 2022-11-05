const mail = {
    from: 'tokped@gmail.com',
    contacts: [],
    sendMessage: function(message, to) {
        console.log(`Sending ${message} to ${to}, from ${this.from}`);
    },
    saveContact: function(newContact) {
        this.contacts.push(newContact);
    },
    changeSender: function(sender) {
        this.from = sender;
    },
    tryPrint: function(ok) {
        console.log(`ini ${ok}`);
    }
}

mail.sendMessage('This is a test message', 'you@gmail.com');
mail.saveContact('you@gmail.com');
mail.saveContact('never@gmail.com');
console.log(mail.contacts);
mail.changeSender('sender@gmail.com');
mail.sendMessage('This is another test message', 'they@gmail.com');
mail.sendMessage('A new message', mail.contacts[1]);

mail.tryPrint('ini di print');

console.log('mail', mail);