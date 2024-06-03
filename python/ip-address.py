import ipaddress

def find_city(ip, ranges):
    ip = ipaddress.ip_address(ip)
    for start, end, city in ranges:
        start_ip = ipaddress.ip_address(start)
        end_ip = ipaddress.ip_address(end)
        if start_ip <= ip <= end_ip:
            return city
    return None

# Define the ranges and cities
ranges = [
    ("1.0.0.1", "1.0.0.10", "LA"),
    ("5.0.0.255", "7.0.1.0", "NY"),
    ("200.0.0.0", "210.1.2.3", "DC")
]

# Test the function
test_ip = "1.0.0.5"
city = find_city(test_ip, ranges)
print(f"The city for IP {test_ip} is {city}")

test_ip = "6.0.0.0"
city = find_city(test_ip, ranges)
print(f"The city for IP {test_ip} is {city}")

test_ip = "205.0.0.1"
city = find_city(test_ip, ranges)
print(f"The city for IP {test_ip} is {city}")

print()
# without using ipaddress module

def ip_to_int(ip):
    parts = list(map(int, ip.split('.')))
    return parts[0] * (255 ** 3) + parts[1] * (255 ** 2) + parts[2] * 255 + parts[3]

def find_the_city(ip, ranges):
    ip_int = ip_to_int(ip)
    for start, end, city in ranges:
        start_int = ip_to_int(start)
        end_int = ip_to_int(end)
        if start_int <= ip_int <= end_int:
            return city
    return None

# Define the ranges and cities
ranges = [
    ("1.0.0.1", "1.0.0.10", "LA"),
    ("5.0.0.255", "7.0.1.0", "NY"),
    ("200.0.0.0", "210.1.2.3", "DC")
]

# Test the function
test_ips = ["1.0.0.5", "6.0.0.0", "205.0.0.1"]
for test_ip in test_ips:
    city = find_the_city(test_ip, ranges)
    print(f"The city for IP {test_ip} is {city}")
