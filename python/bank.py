def calculate_max_people(initial_amount, transactions, index):
    max_people = 0
    current_amount = initial_amount
    for transaction in transactions[index:]:
        if transaction > 0 and current_amount < transaction:
            break

        if transaction > 0:
            current_amount -= transaction
        else:
            current_amount += transaction

        max_people += 1
    return max_people

def max_people_served(initial_amount, transactions):
    max_people = 0
    current_amount = initial_amount
    
    for i in range(len(transactions)):
        current_max_people = calculate_max_people(current_amount, transactions, i)
        max_people = max(max_people, current_max_people)
    
    return max_people

# X = int(input())
# N = int(input())
# transactions = [int(input()) for _ in range(N)]

X = 150
transactions = [10, -20, 30, 490, 810, -40, 50, -60, 250, 70, -80, 90, -100, 145, 235]

print(max_people_served(X, transactions))