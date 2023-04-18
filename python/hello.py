print("hello world")
name = input("what's your name? ")
name = name.strip().title()
print("hello " + name)
pokemon = input("what's your favorite pokemon? ")
fruit = input("what's your favorite fruit? ")
print(name, pokemon, fruit)

x = float(input("x: "))
y = float(input("y: "))

z = x/y
print(f"{z:.2f}")

def hello():
    print("hello world")

name = input("what's your name? ")
hello()
print("hello " + name)