import requests

def get_package_dependencies(package_name):
    url = f"http://registry.npmjs.org/{package_name}/latest"
    response = requests.get(url)
    data = response.json()
    dependencies = data.get("dependencies", {})
    
    # Recursively fetch dependencies
    all_dependencies = []
    for dep_name, dep_version in dependencies.items():
        all_dependencies.append(dep_name)
        all_dependencies.extend(get_package_dependencies(dep_name))
    print(all_dependencies)
    return list(set(all_dependencies))  # Remove duplicates

# Example usage:
package_name = "forever"
dependencies = get_package_dependencies(package_name)
print(len(dependencies))