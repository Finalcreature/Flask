number = 6

user_input = input("Enter 'y' if you would like to play: ").lower()

if (user_input == 'y'):
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("you guessed correctly")

    else:
        print("Sorry, it's wrong")
        print(f"You were off by {abs(number - user_number)}")
