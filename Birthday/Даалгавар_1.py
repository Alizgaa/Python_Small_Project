import datetime
import random
def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)
        print(startOfYear)
        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        print(randomNumberOfDays)
        birthday = startOfYear + randomNumberOfDays
        print(birthday)
        birthdays.append(birthday)
    return birthdays

print(getBirthdays(3))