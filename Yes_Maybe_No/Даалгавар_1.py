import random


NUM_DIGITS = 3

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.
    print(numbers)
    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    if numbers[0] == "0":
        for i in range(1, NUM_DIGITS + 1):
            secretNum += str(numbers[i])
            return secretNum
    else:

        for i in range(NUM_DIGITS):
            secretNum += str(numbers[i])
        return secretNum


print(getSecretNum())
s = random.randint(100, 999)
print(s)
