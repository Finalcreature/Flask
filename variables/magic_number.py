number = 6


game_over = False
while (game_over == False):
    user_input = input("Enter 'y' if you would like to play? (Y/n) ").lower()

    if (user_input == "n"):
        game_over = True
        break

    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("you guessed correctly")
        game_over = True

    else:
        print("Sorry, it's wrong")
        print(f"You were off by {abs(number - user_number)}")
