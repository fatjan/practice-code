const fs = require('fs');

const pageSize = 100;

const axios = require('axios');

// const userId = '6213a356d880448883775cba' // Cameron Duckett
// const userId = '617c0f9139ad1c7a0d62fb4c' // Guia Aguas
const userId = '62f276170eb2cd46b64a183a'
const cookieValue = 'token=s%3AeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBsYXRmb3JtLXNlc3Npb24ifQ.eyJqdGkiOiI1MmEwYmM2Zi00MDdjLTQxOTMtYjBhZi1hYjk3MWY1MmEzOTkiLCJpc3MiOiJwbGF0Zm9ybS1xZGFpbHkiLCJzdWIiOnsidXNlcklkIjoiNjI4ZDQwZDNiZDhkOWY3NWFhZjdhMmJmIiwidGVuYW50SWQiOjE1OSwiZ3JvdXBJZCI6IjYyOGQ0MGQyYmQ4ZDlmNzVhYWY3YTA4ZCIsImZ1bmN0aW9uYWxSb2xlcyI6WyJhZG1pbiJdLCJ0Ijp7ImhvbWVMaW5rIjoiIiwiYnJhbmRDb2xvciI6IiMxZDI1MmQiLCJicmFuZExvZ28iOiJzTVZsdXY0TlJmS3cySWZRdUhqUl9PTkVfbG9nb19MRUFQLnBuZyIsInRlbmFudENvZGVzIjpbImxlYXBzZXJ2aWNlcyJdfSwidSI6eyJfaWQiOiI2MjhkNDBkM2JkOGQ5Zjc1YWFmN2EyYmYiLCJpc0FkbWluIjp0cnVlLCJ0ZW5hbnRJZCI6MTU5LCJncm91cCI6IjYyOGQ0MGQyYmQ4ZDlmNzVhYWY3YTA4ZCIsInByb2ZpbGVJbWciOm51bGwsImZpcnN0TmFtZSI6IkNsaWVudCIsImxhc3ROYW1lIjoiQWRtaW4gVXNlciIsImVtYWlsIjoibGVhcG9uZWFkbWluQGNvbmNyZXRlLmNjIiwiZnVuY3Rpb25hbFJvbGVzIjpbImFkbWluIl0sInJlbGF0aW9ucyI6W3sicm9sZSI6eyJfaWQiOiI2MjhkNDBkMmJkOGQ5Zjc1YWFmN2EwNzciLCJuYW1lIjoiQWRtaW4ifSwiZ3JvdXAiOiI2MjhkNDBkMmJkOGQ5Zjc1YWFmN2EwOGQifV0sImZlYXR1cmVzIjpbImNoYXQiLCJmaWxlc19vdmVydmlldyIsImFkZF9mb3JtX2ZpZWxkIiwiZmlsZXNfdjIiLCJmb3JtcyIsInJlcG9ydGluZyIsImxhbmd1YWdlcyIsInN0b3JpZXMiLCJhc3NldHNfc2hhcmUiLCJzY2FuX2NvZGVfcXVlc3Rpb24iLCJldmVudHMiLCJidWxrX2Rvd25sb2FkIiwic2NvcmluZyIsImltcG9ydF9mcm9tX2ZpbGUiLCJzYXZlZF9hdWRpZW5jZXMiLCJhdWRpZW5jZV9zZW5kX3RvX2FsbCIsIndpZGdldHMiXSwicGFzc3dvcmRFeHBpcmVzQXQiOm51bGx9LCJnIjp7Il9pZCI6IjYyOGQ0MGQyYmQ4ZDlmNzVhYWY3YTA4ZCIsIm5hbWUiOiJMRUFQIiwidHlwZSI6IjYyOGQ0MGQyYmQ4ZDlmNzVhYWY3YTA2YSIsImFuY2VzdG9ycyI6W10sInJlcG9ydHNCb2FyZElkIjoiOHFXejIifX0sImlhdCI6MTcxODk2MTcyNiwiZXhwIjoxNzE4OTY1MzI2fQ.NQDEHIo732rB99s2L-0kSElFkFr1sc0PZQKTG12JY9g.4hNavJVzaWXUzCFe58mjEVMTffMlQ3ujbE32%2Fx52ehs'
// const cookieValue = 'token=s%3AeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBsYXRmb3JtLXNlc3Npb24ifQ.eyJqdGkiOiIzMDA5MTgzMi1lZTQ3LTRhMDEtYTAyMi04YjUwNmI4YWZlMzgiLCJpc3MiOiJwbGF0Zm9ybS1xZGFpbHkiLCJzdWIiOnsidXNlcklkIjoiNjE3YzBmOTEzOWFkMWM3YTBkNjJmYjQ1IiwidGVuYW50SWQiOjE0NSwiZ3JvdXBJZCI6IjYxYmI1M2ExYjM5NjMzN2JlZTNhYjE2NCIsImZ1bmN0aW9uYWxSb2xlcyI6WyJhZG1pbiJdLCJ0Ijp7ImhvbWVMaW5rIjoiaHR0cHM6Ly90dnMucmV0YWlsY2xvdWQubmV0LyIsImJyYW5kQ29sb3IiOiIjMDEyMTY5IiwiYnJhbmRMb2dvIjoiNW9Ec3RKZzhSR3FJVENyZHVWNTRfbG9nby5wbmciLCJzZXNzaW9uVGltZW91dCI6NjAsInRlbmFudENvZGVzIjpbInR2cyJdfSwidSI6eyJfaWQiOiI2MTdjMGY5MTM5YWQxYzdhMGQ2MmZiNDUiLCJpc0FkbWluIjp0cnVlLCJ0ZW5hbnRJZCI6MTQ1LCJncm91cCI6IjYxYmI1M2ExYjM5NjMzN2JlZTNhYjE2NCIsInByb2ZpbGVJbWciOm51bGwsImZpcnN0TmFtZSI6IlRoZSBWaXRhbWluIFNob3BwZSIsImxhc3ROYW1lIjoiQWRtaW4iLCJlbWFpbCI6Im9uZXR2c2FkbWluQHJldGFpbGNsb3VkLm5ldCIsImZ1bmN0aW9uYWxSb2xlcyI6WyJhZG1pbiJdLCJyZWxhdGlvbnMiOlt7InJvbGUiOnsiX2lkIjoiNjE3YzBmOGYzOWFkMWM3YTBkNjJmMzVkIiwibmFtZSI6IkFkbWluIn0sImdyb3VwIjoiNjFiYjUzYTFiMzk2MzM3YmVlM2FiMTY0In1dLCJmZWF0dXJlcyI6WyJjaGF0IiwiZmlsZXNfb3ZlcnZpZXciLCJhZGRfZm9ybV9maWVsZCIsImZpbGVzX3YyIiwiZm9ybXMiLCJyZXBvcnRpbmciLCJsYW5ndWFnZXMiLCJhc3NldHNfc2hhcmUiLCJzY2FuX2NvZGVfcXVlc3Rpb24iLCJldmVudHMiLCJidWxrX2Rvd25sb2FkIiwic2NvcmluZyIsImltcG9ydF9mcm9tX2ZpbGUiXSwicGFzc3dvcmRFeHBpcmVzQXQiOm51bGwsInRlcm1zRXhwaXJlQXQiOm51bGx9LCJnIjp7Il9pZCI6IjYxYmI1M2ExYjM5NjMzN2JlZTNhYjE2NCIsIm5hbWUiOiJBZG1pbiIsInR5cGUiOiI2MTdjMGY4ZjM5YWQxYzdhMGQ2MmYzNGUiLCJhbmNlc3RvcnMiOltdfX0sImlhdCI6MTcxODg3MzA2NywiZXhwIjoxNzE4ODc2NjY3fQ.X7sSBalraEccBaxsCtQaGAwhx52NzoWwXNmk4oDZ-pM.F00tcT%2FJR9%2FdaBeXjvHWsZzxP%2FlOfkLx3hzUvgRT4%2FA'
// const cookieValue = 'token=s%3AeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBsYXRmb3JtLXNlc3Npb24ifQ.eyJqdGkiOiI2Y2U5MmQzZS02NWY0LTQ0NDEtYTMzNy05MmMzMWIwZjBiMzUiLCJpc3MiOiJwbGF0Zm9ybS1xZGFpbHkiLCJzdWIiOnsidXNlcklkIjoiNjIwZTFmMzVjZmY2MGMwZGFiNjA0ZWNhIiwidGVuYW50SWQiOjE1MSwiZ3JvdXBJZCI6IjYzZTQ5Yzc5ZDRmMjJhYjNjMjIzNzE1YyIsImZ1bmN0aW9uYWxSb2xlcyI6WyJhZG1pbiJdLCJ0Ijp7ImhvbWVMaW5rIjoiaHR0cHM6Ly9oZnQucmV0YWlsY2xvdWQubmV0LyIsImJyYW5kTG9nbyI6InlYb1h4MmFVVG55Q2hHdERnVmo5X1RIRUhVQl9IRlRfTG9nby5qcGciLCJ0ZW5hbnRDb2RlcyI6WyJoZnQiXSwib2F1dGhFbmRTZXNzaW9uRW5kcG9pbnQiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vOWNhYzc0ODAtMTNjNi00NjM1LTk4YjYtZjlmNzUwYjg3MjAxL29hdXRoMi92Mi4wL2xvZ291dCIsInBhc3N3b3JkVFRMIjo5MH0sInUiOnsiX2lkIjoiNjIwZTFmMzVjZmY2MGMwZGFiNjA0ZWNhIiwiaXNBZG1pbiI6dHJ1ZSwidGVuYW50SWQiOjE1MSwiZ3JvdXAiOiI2M2U0OWM3OWQ0ZjIyYWIzYzIyMzcxNWMiLCJwcm9maWxlSW1nIjpudWxsLCJmaXJzdE5hbWUiOiJIYXJib3IgRnJlaWdodCBMSVZFIiwibGFzdE5hbWUiOiJBZG1pbiIsImVtYWlsIjoib25laGZ0YWRtaW5AY29uY3JldGUuY2MiLCJmdW5jdGlvbmFsUm9sZXMiOlsiYWRtaW4iXSwicmVsYXRpb25zIjpbeyJyb2xlIjp7Il9pZCI6IjYyMGUxZjM0Y2ZmNjBjMGRhYjYwNGUyZCIsIm5hbWUiOiJBZG1pbiJ9LCJncm91cCI6IjYzZTQ5Yzc5ZDRmMjJhYjNjMjIzNzE1YyJ9XSwiZmVhdHVyZXMiOlsiY2hhdCIsImZpbGVzX292ZXJ2aWV3IiwiYWRkX2Zvcm1fZmllbGQiLCJmaWxlc192MiIsImxhdW5jaHBhZCIsInJlcG9ydGluZyIsImxhbmd1YWdlcyIsInN0b3JpZXMiLCJhc3NldHNfc2hhcmUiLCJzY2FuX2NvZGVfcXVlc3Rpb24iLCJldmVudHMiLCJidWxrX2Rvd25sb2FkIiwic2NvcmluZyIsImltcG9ydF9mcm9tX2ZpbGUiLCJzYXZlZF9hdWRpZW5jZXMiLCJhdWRpZW5jZV9zZW5kX3RvX2FsbCJdLCJwYXNzd29yZEV4cGlyZXNBdCI6bnVsbCwidGVybXNFeHBpcmVBdCI6bnVsbH0sImciOnsiX2lkIjoiNjNlNDljNzlkNGYyMmFiM2MyMjM3MTVjIiwibmFtZSI6IkFkbWluIiwidHlwZSI6IjYyMGUxZjM0Y2ZmNjBjMGRhYjYwNGUyMyIsImFuY2VzdG9ycyI6W119fSwiaWF0IjoxNzE2MjU3MzE0LCJleHAiOjE3MTYyNjA5MTR9.vvoxAdEisn2hJCstByvq33gXNpnRrByLEA3F118MKmc.dW24JtODI7Wyw%2Bp9tBPHLe7TkrdlUhH2sBUeLguIzOM'
// const monica = '6213a296d8804488837675e1' // Monica Coit
// const userId = '6213a4e4d88044888378e949' // Alyssa Norman
// const userId = '6213a2f6d88044888376ec54' // Cassaundra Emerick
const tentantId = 151
// Set the authorization header with the token
const headers = {
  //   'Authorization': `Bearer ${token}`,
  'Cookie': `${cookieValue}`,
  'Content-Type': 'application/json', // Adjust the content type if neededß
};

// Function to log to a text file
function logToFile(objects, fileName) {
  const jsonString = objects.map(object => JSON.stringify(object, null, 2)).join('\n');
  fs.appendFileSync(fileName, jsonString + '\n');
}


// Make a GET request with the token
const result = [];
function requestUsers(url) {
  return axios.get(url, { headers })
    .then(response => response.data.items)
    .catch(error => {
      console.error(error?.message);
      return []; // Return an empty array if there's an error
    });
}


let found = false
for (let i = 0; i < (14453 / pageSize); i++) {
  if (found) break
  const url = `https://api-gateway-preprod.retailcloud.net/admin/users?isArchived=false&page=${i}&pageSize=${pageSize}`;
  requestUsers(url).then(items => {
    for (const item of items) {
      if (item._id === userId) {
        console.log('Found');
        found = true;
        console.log(item);
        break
      }
    }
  });
}

// logToFile(result, 'sample.txt');

// axios.get(url, { headers })
//   .then(response => {
//     const data = response.data;
//     console.log(data.items.length);
//     for (let i = 0; i < data.items.length; i++) {
//         if (data._id == userId) {
//             console.log('Found');
//             console.log(data[i]);
//         }
//     }
//   })
//   .catch(error => {
//     // Handle errors
//     console.error(error);
//   });
