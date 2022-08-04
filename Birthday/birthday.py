import datetime
import random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.


# Display the intro:
print('''N хүнийг санамсаргүйгээр сонгож нэг өдөр өдөр төрсөн өдөр нь
 таарах хэдэн хүн байгааг тооцоолоох туршилтийг 
 100.000 удаа хийж үзэцгээ. ''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print('Хүний тоог оруулна уу! (MAX = 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered a valid amount.
print()

# Generate and display the birthdays:
print(numBDays, 'хүний төрсөн өдөр:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('Түршилтын үр дүн: ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Ядаж хоёр хүн хамт төрсөн өдрөө тэмдэглэх огноо: ', dateText)
else:
    print("Ядаж хоёр хүн хамт төрсөн өдрөө тэмдэглэх огноо олдсонгүй.")
print()

# Run through 100,000 simulations:
print('Одоо энэхүү туршилтыг 100.000 удаа давтаж үзэцгээе.')
input('Та эхлүүлэхийн тулд Enter товчлуур дээр дарна уу ... ')

print('Тооцоолж эхэллээ!!!')
simMatch = 0  # How many simulations had matching birthdays in them.
for i in range(100000):
    # Report on the progress every 10,000 simulations:
    if i % 10000 == 0:
        print(i, 'дахь туршилт явагдаж байна...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('Туршилт явагдаж дууслаа.')

# Display simulation results:
probability = round(simMatch / 100000 * 100, 2)

print("{} хүнийг санамсаргүйгээр сонгоход нэг өдөр төрсөн өдрөө тэмдэглэх ядаж".format(numBDays))
print("хоёр хүн олдох боломжийг тооцоолох туршилтыг 100000 удаа явуулахад {} удаа".format(simMatch))
print("давтагдлаа. Иймд {} хүнийг санамсаргүйгээр сонгоход төрсөн өдрөө нэг өдөрт".format(numBDays))
print("тэмдэглэх ядаж хоёр хүн олдох магадлал {}% байна.".format(probability))
