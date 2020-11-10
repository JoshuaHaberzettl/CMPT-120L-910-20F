def prime_or_composite(number):
    if number <= 3:
        if number > 1:
            return "Prime"
        else:
            return "Composite"
    if number % 2 == 0 or number % 3 == 0:
        return "Composite"
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return "Composite"
        i += 6
    return "Prime"

if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201, -7, 47055833459]
    # If you want to test the efficency of your algorithm add this number to the array above -7
    # If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)