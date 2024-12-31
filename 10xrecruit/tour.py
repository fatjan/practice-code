import math

def min_time(max_speed, segments):
    x, y, speed, direction = segments[0], segments[1], segments[2], segments[3]

    teta = direction * 360 / (2 * math.pi)

print(min_time(50.0, [125.0, 175.0, 25.0, 1.96]))