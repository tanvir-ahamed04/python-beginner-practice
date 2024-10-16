days = {
    'm': 'Monday',
    't': {'u': 'Tuesday', 'h': 'Thursday'},
    'w': 'Wednesday',
    'f': 'Friday',
    's': {'a': 'Saturday', 'u': 'Sunday'}
}

first_letter = input("Enter the first letter of the day in a week: ").lower()

if first_letter in days:
    if isinstance(days[first_letter], str):
        print(days[first_letter])
    else:
        second_letter = input("Enter the second letter of the day in a week: ").lower()
        if second_letter in days[first_letter]:
            print(days[first_letter][second_letter])
        else:
            print("Invalid input for the second letter.")
else:
    print("Invalid input for the first letter.")