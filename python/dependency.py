# There is NPM JSON API for getting NPM packages info. For example the 
# following URL allows for getting information about the latest version of
#  "forever" package:
 
# http://registry.npmjs.org/forever/latest
 
# This request will result in a JSON, containing many fields, including 
# dependencies field:
# dependencies:
# {
#  cliff: "~0.1.9",
#  clone: "^1.0.2",
#  colors: "~0.6.2",
#  flatiron: "~0.4.2",
#  forever-monitor: "~1.7.0",
#  ...
# }
# This is a list of direct dependencies of an NPM package.
 
# Write a function getAllDependencies(packageName) which takes in 
# packageName parameter as a string and returns an array of strings of 
# both direct and all indirect (recursive) dependencies of the given 
# package, fetched from the API described above. For example, if A depends
#  on B, and B depends on C and D, getAllDependencies('A') should return 
# ['B', 'C', 'D']. The result should not contain duplicates.
 
# In a correct implementation, getAllDependencies("forever") should return
#  an array with length about 200+ (as of the time we wrote this question 
# and might be different in the future).
 
# Bonus points for:
# Use of concurrency
# import requests

def getAllDependencies(packageName, result = []):
    url = f"http://registry.npmjs.org/{packageName}/latest"
    response = requests.get(url)
    if "dependencies" in response.json():
        deps = response.json()["dependencies"]
        for dep in deps:
            if dep not in result:
                result.append(dep)
                getAllDependencies(dep, result)

    return len(result)

print(getAllDependencies("forever"))