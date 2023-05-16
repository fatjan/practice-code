# before refactor
def process_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            square = num ** 2
            if square > 50:
                result.append(square)
    return result

# after refactor
def process_numbers(numbers):
    result = []
    for num in numbers:
        square = num ** 2
        if num % 2 == 0 and square > 50:
            result.append(square)
    return result

# before refactor
def calculate_grades(scores):
    total = 0
    count = 0
    for score in scores:
        if score >= 90:
            total += score
            count += 1
    if count != 0:
        average = total / count
    else:
        average = 0
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

# after refactor to do
def calculate_grades(scores):
    total = 0
    count = 0
    for score in scores:
        if score >= 90:
            total += score
            count += 1
    if count != 0:
        average = total / count
    else:
        average = 0
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade