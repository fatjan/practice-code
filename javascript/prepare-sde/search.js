function searchSuggestions(repository, customerQuery) {
    // Write your code here
    let word = customerQuery[0];
    let result = [];
    const output = [];
    
    for (let i = 1; i < customerQuery.length; i++) {
        word += customerQuery[i];
        console.log('word ', word);
        
        for (let x in repository) {
            if (repository[x].slice(0, i+1).toLowerCase() === word.toLowerCase()) {
                result.push(repository[x])
            }
        }
        result.sort();
        result = [...new Set(result)];

        result.length > 3 ? output.push(result.slice(0, 3)) : output.push(result);
        result = [];
    }
    return output;
}

console.log(searchSuggestions(['bags', 'baggage', 'banner', 'box', 'cloths'], 'bags'));