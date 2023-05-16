# before refactor
def calc_total_price(products, quantities):
    total = 0
    for i in range(len(products)):
        if products[i] == "apple":
            total += quantities[i] * 0.5
        elif products[i] == "banana":
            total += quantities[i] * 0.25
        elif products[i] == "orange":
            total += quantities[i] * 0.4
        elif products[i] == "grape":
            total += quantities[i] * 0.15
        elif products[i] == "watermelon":
            total += quantities[i] * 1.0
    return total

# after refactor
def total_price(products, quantities):
    total = 0
    price = {
        "apple": 0.5,
        "banana": 0.25,
        "orange": 0.4,
        "grape": 0.15,
        "watermelon": 1.0
    }
    for i in range(len(products)):
        total += quantities[i] * price[products[i]]
    return total

"""The refactored code has several notable improvements:

Dictionary for prices: You introduced a dictionary called price to map the product names to their respective prices. 
This approach simplifies the code by removing multiple if-else conditions, making it more concise and maintainable.

Improved variable names: The variable name total effectively communicates its purpose. It's clear that it's being used to calculate the total price.

Simplified calculation: By directly accessing the price from the dictionary using price[products[i]], you eliminate the need for multiple if-else conditions. 
This approach enhances code readability and maintainability."""