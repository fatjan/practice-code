const e = {
    message: "{\"message\":\"list index out of range\",\"name\":\"IndexError\",\"code\":500,\"stack\":\"Traceback (most recent call last):\\n  File \\\"/tmp/sls-py-req/wbpeanuts/listeners/handlers/faas_handler.py\\\", line 26, in listen\\n    (err, res) = self.handle_call(event)\\n  File \\\"/tmp/sls-py-req/wbpeanuts/listeners/handlers/faas_handler.py\\\", line 61, in handle_call\\n    return self.handle_postback(body)\\n  File \\\"/tmp/sls-py-req/wbpeanuts/listeners/handlers/faas_handler.py\\\", line 70, in handle_postback\\n    response = self.handler(body)\\n  File \\\"/var/task/wb__runner.py\\\", line 36, in run\\n    output = execute(body)\\n  File \\\"/var/task/wb__runner.py\\\", line 134, in execute\\n    return execute_with_metadata(body)\\n  File \\\"/var/task/wb__runner.py\\\", line 145, in execute_with_metadata\\n    return executeFn(**mapping)\\n  File \\\"/var/task/main.py\\\", line 22, in search\\n    bucket_size = get_bucket_size(entries)\\n  File \\\"/var/task/lib/preprocess_data.py\\\", line 27, in get_bucket_size\\n    return int(unique_bucket_sizes[0])\\nIndexError: list index out of range\\n\"}"
}
e.message =  "{\"message\":\"<class 'ValueError'>: The number of samples in the training data is smaller than the number of samples in the test set.\"}";
// const e = {
//     message:  "{\"message\":\"<class 'ValueError'>: The number of samples in the training data is smaller than the number of samples in the test set.\"}"
// }
const obj = JSON.parse(e.message);
if (obj.stack) {
    obj.stack = obj.stack.replace(/(\r\n|\n|\r)/gm, '');
  }
e.messageParsed = JSON.stringify(obj, null, 2);

console.log(e.messageParsed);