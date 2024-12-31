def bell_tolls(n, creatures):
    bell_count = 0

    for i in range(n - 1, 0, -1):
        if creatures[i] == 'O':
            bell_count += 1
            # Turn the current ocelot into a zebra
            creatures[i] = 'Z'
            # Turn all zebras below it into ocelots
            for j in range(i - 1, -1, -1):
                if creatures[j] == 'Z':
                    creatures[j] = 'O'
                else:
                    break  # Stop when a non-zebra is encountered

    return bell_count

# Read input
n = int(input())
creatures = list(input().strip() for _ in range(n))

# Calculate and print the result
result = bell_tolls(n, creatures)
print(result)
