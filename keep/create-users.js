const fs = require('fs');

function readCSVFile(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (error, data) => {
      if (error) {
        reject(error);
        return;
      }

      const lines = data.split('\n');
      const csvData = [];
      const headers = lines[0].split(';');

      for (let i = 1; i < lines.length; i++) {
        const row = lines[i].split(';');
        if (row.length === headers.length) {
          const entry = {};
          for (let j = 0; j < headers.length; j++) {
            const header = headers[j].trim();
            const value = row[j].trim();
            entry[header] = value;
          }
          csvData.push(entry);
        }
      }

      resolve(csvData);
    });
  });
}

const coreUrl = 'https://alfa-core-eu-central-1.web.quinyx.com/api/WBUsers/addToTeam'
const cookieValue = 'this-is-cookie-value';
const filePath = 'users.csv';

readCSVFile(filePath)
  .then(async data => {
    for (const user of data) {
      const bodyData = {
          name: user.name,
          email: user.email,
          hasConsoleAccess: true,
          hasProgrammaticAccess: false,
          role: 'client',
          teamId: 'f0ed9576-e1a9-4884-940d-44cbb4e2940f',
          appId: 30
        }

      await fetch(coreUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Cookie': cookieValue
        },
        body: JSON.stringify(bodyData)
      })
        .then(response => response.json())
        .then(responseData => {
          console.log(responseData);
          // Process the response data
        })
        .catch(error => {
          console.error(error);
        });
    }
  })
  .catch(error => {
    console.error(error);
  });




