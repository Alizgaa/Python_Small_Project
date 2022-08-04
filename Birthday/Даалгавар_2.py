import datetime
import random

birthdays = [datetime.date(2001, 5, 29), datetime.date(2001, 4, 9), datetime.date(2001, 12, 7)]


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.

print(getMatch(birthdays))