import random
import time

def firework_display():
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']  # ANSI color codes for different colors
    fireworks = ['*', '+', '.', 'o']  # ASCII characters for different types of fireworks

    for _ in range(10):  # Simulate 10 fireworks
        color = random.choice(colors)
        firework = random.choice(fireworks)
        size = random.randint(5, 15)

        print(color + firework * size)
        time.sleep(0.5)

    print('\033[0m')  # Reset color to default

# Call the firework_display function
firework_display()
