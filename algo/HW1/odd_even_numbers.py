# Count odd and even numbers.
# Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


def count_odd_even(number):
    odds = 0
    evens = 0

    while number != 0:
        current_digit = number % 10
        if current_digit % 2:
            odds = odds + 1
        else:
            evens = evens + 1
        number = number // 10

    return ['Evens: ' + str(evens), 'Odds: ' + str(odds)]


number = int(input('Enter your number: '))
print(count_odd_even(number))